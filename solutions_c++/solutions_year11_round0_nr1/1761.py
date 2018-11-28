#pragma comment(linker, "/STACK:10000000")
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>
#include <cstdio>
#include <cassert>
#include <string>
#include <cstring>
#define ldb long double
#define LL long long
#define fi first
#define se second
#define fill(a, c) memset(a, c, sizeof(a))
#define sqr(a) ((a) * (a))
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
#define getBit(mask, k) (((mask) / pw[k]) % pw[1])
#define setBit(mask, k, l) (((mask) / pw[k + 1] * pw[1] + (l)) * pw[k] + ((mask) % pw[k]))
#define debug(a) cerr << #a << " = " << a << " ";
#define debugl(a) cerr << #a << " = " << a << "\n";
const ldb LDINF = 9128739847123.00;
const ldb eps = 1e-9;
const int INF = 1 << 28;
const ldb pi = fabsl(atan2(0.0, -1.0));
using namespace std;

int b[1000];
int type[1000];
int n;
int d[102][102][102];
int calced[102][102][102];
int used;
pair<int, pair<int, int> > q[2000000];


void Load()
{
	cin >> n;
	int i;
	char c;
	for (i = 0; i < n; i++)
	{
		cin >> c >> b[i];
		b[i] --;
		if (c == 'B') type[i] = 0;
		else type[i] = 1;
	}
}

bool can(int k, int i, int j)
{
	return i >= 0 && j < 100 && i < 100 && j >= 0;
}

void Solve(int Test)
{
	cout << "Case #" << Test << ": ";
	used++;
	int head = 0, tail = 0;
	q[head] = make_pair(0, make_pair(0, 0));
	calced[0][0][0] = used;
	d[0][0][0] = 0;
	int k, i, j, t1, t2, t;
	while (head <= tail)
	{
		k = q[head].first, i = q[head].second.first, j = q[head].second.second;
		head++;
		if (k == n)
		{
			cout << d[k][i][j] << "\n";
			return;
		}
		if (type[k] == 0 && b[k] == i)
			for (t = -1; t <= 1; t++)
				if (can(k + 1, i, j + t) && calced[k + 1][i][j + t] != used)
				{
					q[++tail] = make_pair(k + 1, make_pair(i, j + t));
					d[k + 1][i][j + t] = d[k][i][j] + 1;
					calced[k + 1][i][j + t] = used; 
				}
		
		if (type[k] == 1 && b[k] == j)
			for (t = -1; t <= 1; t++)
				if (can(k + 1, i + t, j) && calced[k + 1][i + t][j] != used)
				{
					q[++tail] = make_pair(k + 1, make_pair(i + t, j));
					d[k + 1][i + t][j] = d[k][i][j] + 1;
					calced[k + 1][i + t][j] = used; 
				}

		for (t1 = -1; t1 <= 1; t1++)
		{
			for (t2 = -1; t2 <= 1; t2++)
			{
				if (can(k, i + t1, j + t2) && calced[k][i + t1][j + t2] != used)	
				{
					q[++tail] = make_pair(k, make_pair(i + t1, j + t2));
					d[k][i + t1][j + t2] = d[k][i][j] + 1;
					calced[k][i + t1][j + t2] = used;
				}
			}
		} 
		
	}
}

#define file "a"
int main()
{
	freopen(file".in", "rt", stdin);
	freopen(file".out", "wt", stdout);
	int T;
	cin >> T;
	int i;
	used = 0;
	for (i = 0; i < T; i++)
	{
		Load();
		Solve(i + 1);
	}
	return 0;
}
