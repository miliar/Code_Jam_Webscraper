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

int n;
int a[100][100];
int most[110];
int p[110];
int per[110];

void Load()
{
	cin >> n;
	int i, j;
	nextLine();
	int c;
	for (i = 1; i <= n; i++)
	{
		per[i] = i;
		for (j = 1; j <= n; j++)
		{
			c = getchar();
			a[i][j] = c - '0';
		}
		nextLine();
	}
}

void Solve(int Test)
{
	cout << "Case #" << Test << ": ";
	int i, j;
	for (i = 1; i <= n; i++)
	{
	p[i] = 0;
		for (j = 1; j <= n; j++)
		{
			if (a[i][j] == 1)
				p[i] = j;
		}
	}
	int rj;
	LL res = 0;
	for (i = 1; i < n; i++)
	{
		rj = INF;
		for (j = i; j <= n; j++)
		{
			if (p[per[j]] <= i)
			{
				rj = min(rj, j);
			}
		}
		if (rj == INF)
		{
			cerr << Test;
		}
		res += rj - i;
		for (j = rj; j > i; j--)
		{
			swap(per[j], per[j - 1]);
		}
	}
	cout << res << "\n";
}


#define file "a"
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