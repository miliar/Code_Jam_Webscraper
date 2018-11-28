#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath>
#include <cstdio>
#include <string>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#include <set>
#include <iomanip>
#include <ctime>
#include <iostream>
#include <sstream>
#include <deque>
#pragma comment(linker, "/STACK:256000000")

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
template<class T> inline T sqr(T a) {return a * a;}
#define INF 123456789
#define MOD 1000000007
#define PRIME 1103
#define TEST "A-small-attempt0"
#define EPS 1e-6
#define sz(c) (int)c.size()
#define mp make_pair
#define all(c) (c).begin(), (c).end()
//------------------------------------

vector<int64> d, l;
int n;
vector<int> cash;
int64 D;

/*bool canMove(int u, int v, double curl)
{
	return d[v] - d[u] <= curl && l[v] >= d[v] - d[u];
}
bool f(int k, double curl)
{
	if(cash[k] != -1) return cash[k];
	if(d[k] + curl > D || fabs(d[k] + curl - D) < EPS)
		return cash[k] = 1;
	int res = 0;
	for(int i = k + 1; i < n; ++i)
	{
		//if(!canMove(k, i, curl) || res) break;
		///res = f(i, d[i] - d[k]);//min(sqrt(sqr(curl) + sqr(d[i] - d[k])), l[i] + .0));
		if(res) break;
		int64 x2 = sqr(d[k] - d[i]) + sqr(l[i]);
		if(x2 <= sqr(curl))
		{
			curl = sqrt(x2 + .0);
			res = f(i, l[i]);
			continue;
		}
		if(curl < d[i] - d[k]) continue;
		res = f(i, min(l[i] + .0, sqrt(sqr(curl) + sqr(d[i] - d[k]))));
	}
	return cash[k] = res;
}*/
bool canMove(int u, int v, int curl)
{
	return d[v] - d[u] <= curl ;//l[v] >= d[v] - d[u];
}

bool f(int k, int64 curl)
{
	//if(cash[k] != -1) return cash[k];
	if(d[k] + curl >= D) return cash[k] = 1;
	int res = 0;
	for(int i = k + 1; i < n; ++i)
	{
		if(res) break;
		if(!canMove(k, i, curl)) continue;
		/*int64 x2 = sqr(d[k] - d[i]) + sqr(l[i]);
		if(x2 <= sqr(curl))
		{
			if(d[i] - d[k] > l[i]) continue;
			res = f(i, d[i] - d[k]);
			continue;
		}*/
		//if(sqr(curl) - 2 * sqr(d[i] - d[k]) < 0) continue;
		res = f(i, min(d[i] - d[k], l[i]));
	}
	return cash[k] = res;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen(TEST ".in", "r", stdin);
	freopen(TEST ".out", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int test = 0; test < t; ++test)
	{
		scanf("%d", &n);
		d.assign(n, 0);
		l.assign(n, 0);
		cash.assign(n, -1);
		for(int i = 0; i < n; ++i)
			cin >> d[i] >> l[i];
		cin >> D;
		int res = f(0, d[0]);
		printf("Case #%d: ", test + 1);
		if(res) cout << "YES\n";
		else cout << "NO\n";
	}

	return 0;
}