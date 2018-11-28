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

const double MAX = 1e13;
const double EPS = 1e-12;
const int N = 200 + 5;

int c;
double d;
int p[N];
int v[N];

bool Ok(double t)
{
	double left = -MAX;
	vector<double> pers;
	FOR(i, c) FOR(j, v[i])
	{
		double cur = left + d;
		cur = max(cur, p[i] - t);
		cur = min(cur, p[i] + t);
		pers.PB(cur);
		left = cur;
	}
	FOR(i, pers.size() - 1) if (fabs(pers[i + 1] - pers[i]) < d - EPS) return false;
	return true;

}

double Solve()
{
	double l = 0.0, r = MAX;
	while (fabs(r - l) > EPS)
	{
		double c = (l + r) / 2.0;
		if (Ok(c))
			r = c;
		else
			l = c;
	}
	return (l + r) / 2.0;
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	/*{
		string s = "";
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}*/
#endif
	
	int tt;
	scanf("%d", &tt);
	FOR(i, tt)
	{
		scanf("%d %lf", &c, &d);
		FOR(i, c) scanf("%d %d", &p[i], &v[i]);
		printf("Case #%d: %.15lf\n", i + 1, Solve());
	}
	
	return 0;
}
