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
#include <bitset>
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
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
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

const int N = 1000 + 3;

int k;
char s[N];

char lets[10] = {'o', 'i', ' ', 'e', 'a', 's', ' ', 't', 'b', 'g'};
char to[300];

int degin[N], degout[N];

void solve (int test)
{
	set <string> u;
	int n = strlen(s);
	
	forn(i, n - 1)
	{
		string tmp;
		tmp.pb(s[i]);
		tmp.pb(s[i + 1]);
		u.insert(tmp);
	}
	
	set <string> res;
	
	for (set <string> :: iterator it = u.begin(); it != u.end(); it++)
	{
		string cur = *it;
		
		res.insert(cur);
		
		if (to[cur[0]] != -1)
		{
			string cur2 = cur;
			cur2[0] = to[cur2[0]];
			res.insert(cur2);
		}
		
		if (to[cur[1]] != -1)
		{
			string cur2 = cur;
			cur2[1] = to[cur2[1]];
			res.insert(cur2);
		}
		
		if (to[cur[0]] != -1 && to[cur[1]] != -1)
		{
			string cur2 = cur;
			cur2[0] = to[cur2[0]];
			cur2[1] = to[cur2[1]];
			res.insert(cur2);
		}
	}
	
	memset(degin, 0, sizeof(degin));
	memset(degout, 0, sizeof(degout));
	
	map <char, int> nums;
	
	for (set <string> :: iterator it = res.begin(); it != res.end(); it++)
	{
		char c1 = (*it)[0], c2 = (*it)[1];
		
		if (!nums.count(c1))
		{
			int sz = sz(nums);
			nums[c1] = sz;
		}
		
		if (!nums.count(c2))
		{
			int sz = sz(nums);
			nums[c2] = sz;
		}
	}
	
	int ans = sz(res) + 1;
	
	for (set <string> :: iterator it = res.begin(); it != res.end(); it++)
	{
		//cerr << *it << endl;
		char c1 = (*it)[0], c2 = (*it)[1];
		degin[nums[c2]]++;
		degout[nums[c1]]++;
	}
	
	int add = 0;
	
	forn(i, sz(nums))
		add += abs(degin[i] - degout[i]);
	
	assert(add % 2 == 0);
	add = max(0, add - 2);
	
	ans += add / 2;
		
	printf("Case #%d: %d\n", test + 1, ans);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	memset(to, -1, sizeof(to));
	forn(i, 10)
		to[lets[i]] = '0' + i;
	
	int testCount;
	cin >> testCount;
	
	forn(test, testCount)
	{
		scanf("%d%s", &k, s);
		solve(test);
	}

	return 0;
}
























































