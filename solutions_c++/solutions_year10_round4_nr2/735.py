#include <iostream>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#define ldb long double
#define LL long long
#define sqr(a) (a) * (a)
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
const ldb LDINF = 9128739847123.00;
const ldb eps = 1e-9;
const int INF = 2147483647 / 2;
using namespace std;


#define file "b"

int cost[13][1 << 13];
int d[13][1 << 13];
int will[1 << 13];
int was[13][1 << 13];
int p;

void Load()
{
	cin >> p;
	int i;
	for (i = 0; i < (1 << p); i++)
	{
		scanf("%d", &will[i]);
	}
	int j;
	for (i = 0; i < p; i++)
	{
		for (j = 0; j < (1 << (p - i - 1)); j++)
		{
			cin >> cost[i][j];
		}
	}
}

int GetMin(int r, int c)
{
	if (r == 0) return min(will[2 * c], will[2 * c + 1]);
	if (d[r][c] != -1) return d[r][c];
	d[r][c] = min(GetMin(r - 1, 2 * c), GetMin(r - 1, 2 * c + 1));	
	return d[r][c];
}

int f(int r, int c)
{
	if (r == 0) return cost[r][c];
	int m1 = GetMin(r - 1, 2 * c);
	int m2 = GetMin(r - 1, 2 * c + 1);
	int t = INF;
	int res = INF;
	if (r <= min(m1, m2)) res = cost[r][c];
	if (r <= m1) res = min(res, cost[r][c] + f(r - 1, 2 * c + 1));
	if (r <= m2) res = min(res, cost[r][c] + f(r - 1, 2 * c));
	res = min(res, f(r - 1, 2 * c) + f(r - 1, 2 * c + 1));
	cerr << r << " " << c << " " << res << "\n";
	return res;

}

void Go(int r, int c, int up)
{
	if (up > 0) Go(r + 1, c / 2, up - 1);
	else if (r == p) return;
	else 
	{
		was[r][c] = 1; 
		Go(r + 1, c / 2, up);
	}
}

void Solve(int Test)
{
	cout << "Case #" << Test << ": "; 
	int i, j;
	//memset(d, 0xFF, sizeof(d));
	//cout << f(p - 1, 0) << "\n";
	int res = 0;
	memset(was, 0, sizeof(was));
	for (i = 0; i < (1 << p); i++)
	{
		Go(0, i / 2, will[i]);
	}
	for (i = 0; i < p; i++)
	{
		for (j = 0; j < (1 << (p - i - 1)); j++)
		{
			if (was[i][j]) res += cost[i][j];
		}
	}
	cout << res << "\n";
	//cerr << "\n\n";
}


int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	int i;
	for (i = 1; i <= T; i++)
	{
		Load();
		Solve(i);
	}
	return 0;
}