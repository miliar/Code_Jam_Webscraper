#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define X first
#define Y second
#define ft first
#define sc second

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long double ld;
typedef pair<ld, ld> ptd;
typedef pair <int, int> pt;
typedef long long li;
typedef unsigned char byte;

const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-9;
const int INF = 1000 * 1000 * 1000;

const int ALP = 30;
const int N = 100 + 13;

int n;
char s[N];
char rules[ALP][ALP];
bool hasRule[ALP][ALP];
bool hasClear[ALP][ALP];

string solve ()
{
	string res = "";
	
	forn(i, n)
	{
		res.pb(s[i]);
	
		bool flag = false;
	
		while (sz(res) >= 2 && hasRule[res[sz(res) - 1] - 'A'][res[sz(res) - 2] - 'A'])
		{
			char c1 = res[sz(res) - 1], c2 = res[sz(res) - 2];
			res.erase(sz(res) - 2);
			res.pb(rules[c1 - 'A'][c2 - 'A']);
			flag = true;
		}
		
		if (flag)
			continue;
			
		forn(j, sz(res) - 1)
			if (hasClear[res[j] - 'A'][res[sz(res) - 1] - 'A'])
			{
				res.clear();
				break;
			}
	}
	
	string ans = "[";
	
	forn(i, sz(res))
	{
		ans.pb(res[i]);
		
		if (i < sz(res) - 1)
			ans += ", ";
	}
	
	ans.pb(']');
	
	return ans;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int testCount;
	cin >> testCount;
	
	forn(test, testCount)
	{
		memset(hasRule, false, sizeof(hasRule));
		memset(hasClear, false, sizeof(hasClear));
	
		int cntRules;
		scanf("%d", &cntRules);
		
		forn(i, cntRules)
		{
			char buf[10];
			scanf("%s", buf);
			
			hasRule[buf[0] - 'A'][buf[1] - 'A'] = true;
			hasRule[buf[1] - 'A'][buf[0] - 'A'] = true;
			rules[buf[0] - 'A'][buf[1] - 'A'] = buf[2];
			rules[buf[1] - 'A'][buf[0] - 'A'] = buf[2];
		}
			
		int cntClears;
		scanf("%d", &cntClears);
		
		forn(i, cntClears)
		{
			char buf[10];
			scanf("%s", buf);
			
			hasClear[buf[0] - 'A'][buf[1] - 'A'] = true;
			hasClear[buf[1] - 'A'][buf[0] - 'A'] = true;
		}
			
		scanf("%d", &n);
		
		scanf("%s", s);
		
		printf("Case #%d: %s\n", test + 1, solve().c_str());
	}

	return 0;
}
























































