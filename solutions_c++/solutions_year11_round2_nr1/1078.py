#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <cmath>
#include <sstream>
#include <numeric>

#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define EPS 1e-9
#define INF INT_MAX
#define SQR(X) (X) * (X)
#define round(x) (int)floor((x) + 0.5 + EPS)

using namespace std;

typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long LL;

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <uint> vu;
typedef vector <ull> vull;
typedef vector <pii> vpii;
typedef vector <vpii> vvpii;
typedef vector <string> vs;

int d[300][300];


int main()
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int z = 1; z <= t; z++)
	{
		printf("Case #%d:\n", z);
		memset(d, -1, sizeof(d));
		int n;
		scanf("%d", &n);
		vector<double> wp(n, 0), owp(n, 0), oowp(n, 0);
		vi a(n);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
			{
				char c;
				scanf(" %c", &c);
				if (c == '.') continue;
				if (c == '1') d[i][j] = 1;
				else d[i][j] = 0;
			}
		for (int i = 0; i < n; i++)
		{
			int won = 0, all = 0;
			for (int j = 0; j < n; j++)
			{
				if (d[i][j] == -1) continue;
				all++;
				if (d[i][j]) won++;
			}
			wp[i] = (double)won / (double)all;
			a[i] = all;
		}
		for (int i = 0; i < n; i++)
		{
			int all = 0;
			double sum = 0;
			for (int j = 0; j < n; j++)
			{
				if (d[i][j] == -1) continue;
				all++;
				sum += ((wp[j] - (double)d[j][i] / (double)a[j])) * a[j] / (a[j] - 1);
			}
			owp[i] = sum / all;
		}
		for (int i = 0; i < n; i++)
		{
			int all = 0;
			double sum = 0;
			for (int j = 0; j < n; j++)
			{
				if (d[i][j] == -1) continue;
				all++;
				sum += owp[j];
			}
			oowp[i] = sum / all;
		}
		for (int i = 0; i < n; i++)
			printf("%.9lf\n", 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
	}
	return 0;
}