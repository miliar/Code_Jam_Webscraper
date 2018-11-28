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

string minCycled(int x)
{
	string s;
	while(x)
	{
		s += (x%10) + '0';
		x /= 10;
	}
	reverse(ALL(s));
	string res = s;
	string cur;
	FOR(i, 1, s.size())
	{
		cur.resize(s.size());
		REP(j, s.size())
			cur[j] = s[(i + j) % s.size()];
		if (cur < res)
			res = cur;
	}
	return res;
}

string AA[2048000];
int main()
{
	freopen("c-input.txt", "r", stdin);
	freopen("c-output.txt", "w", stdout);

	int tests;
	cin >> tests;

	FOR(i, 1, 2000000)
		AA[i] = minCycled(i);

	FOR(TEST, 1, tests)
	{
		map<string, ll> mp;
		int A, B;
		cin >> A >> B;
		mp.clear();
		FOR(i, A, B)
		{
			string ss = AA[i];
			mp[ss] += 1;
		}

		ll ans = 0;
		ll sum = 0;
		for (map<string, ll>::iterator it = mp.begin(); it != mp.end(); ++it)
		{
			ans += (it->second) * (it->second - 1) / 2;
			sum += it->second;
		}
	
		printf("Case #%d: %d\n", TEST, ans);
	}
}