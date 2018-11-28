#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <memory.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
using namespace std;

#define FOR(i, n)		for (int i = 0; i < (int) (n); i++)
#define RFOR(i, n)		for (int i = (int) (n) - 1; i >= 0; i--)
#define CL(x)			memset(x, 0, sizeof(x))
#define CLX(x, v)		memset(x, v, sizeof(x))
#define ALL(x)			(x).begin(), (x).end()
#define PB				push_back
#define MP				make_pair

typedef long long LL;
typedef unsigned long long UL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;

//////////////////////////////////////////////////////////////////////////

const int N = 1001;

int n;
char m[N][N];

void Scan()
{
	scanf("%d", &n);
	FOR(i, n) scanf("%s", m[i]);
}

double FF(double A, double B, double C)
{
	return 0.25 * A + 0.50 * B + 0.25 * C;
}

double CalcA(int i)
{
	int tot = 0, win = 0;
	FOR(j, n)
		if (m[i][j] != '.')
		{
			if (m[i][j] == '1') win++;
			tot++;
		}
	return (double) win / tot;
}

double CalcB(int i)
{
	double sum = 0;
	int cnt = 0;
	FOR(j, n) if (i != j && m[i][j] != '.')
	{
		int tot = 0, win = 0;
		FOR(k, n) if (k != i)
			if (m[j][k] != '.')
			{
				if (m[j][k] == '1') win++;
				tot++;
			}
		sum += (double) win / tot;
		cnt++;
	}
	return sum / cnt;
}

double CalcC(int i)
{
	double sum = 0;
	int cnt = 0;
	FOR(j, n) if (i != j && m[i][j] != '.')
	{
		sum += CalcB(j);
		cnt++;
	}
	return sum / cnt;
}

void Solve()
{
	FOR(i, n)
	{
		double A = CalcA(i);
		double B = CalcB(i);
		double C = CalcC(i);
		printf("%.10lf\n", FF(A, B, C));
	}
}

int main()
{
//#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
//#else
	/*{
		string s = "";
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}*/
//#endif

	int tt;
	scanf("%d", &tt);
	FOR(i, tt)
	{
		Scan();
		printf("Case #%d:\n", i + 1);
		Solve();
	}
	
	return 0;
}
