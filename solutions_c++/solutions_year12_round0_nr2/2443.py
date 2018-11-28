#pragma comment(linker, "/STACK:25600000")
#define _CRT_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <cstring>
#include <map>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define REP(i, n) for(int i=0; i<n; i++)
#define FOR(i, x, y) for(int i=x; i<=y; i++)
#define RFOR(i, x, y) for(int i=x; i>=y; i--)
#define ALL(a) (a).begin(),(a).end()
#define pb push_back
#define PII pair<int, int>
const double pi=acos(-1.0);

int main()
{
	freopen("b-input.txt", "r", stdin);
	freopen("b-output.txt", "w", stdout);

	int tests;
	cin >> tests;
	FOR(TEST, 1, tests)
	{
		int n, s, p;
		cin >> n >> s >> p;
		vector<int> a(n);
		vector<int> u(n);
		REP(i, n)
			cin >> a[i];
		sort(ALL(a));
		reverse(ALL(a));

		int need = p*3 - 2;
		REP(i, n)
			if (a[i] >= need && a[i] >= p)
				u[i] = true;

		need -= 2;
		REP(i, n)
			if (a[i] >= need && s && !u[i] && a[i] >= p)
			{
				--s;
				u[i] = true;
			}
		int ans = 0;
		REP(i, n)
			ans += u[i];
		printf("Case #%d: %d\n", TEST, ans);
	}

}