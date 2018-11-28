#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <vector>
#include <iostream>

#include <conio.h>
#include <stack>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <map>
#include <cmath>

using namespace std;

const int INF = 1000*1000*1000 + 10;
const double EPS = 1E-6;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef long long ll;
typedef vector<bool> vb;
typedef vector<ll> vll;
#define all(s) s.begin(), s.end()

#define forn(i, n) for (int i = 0; i < n; ++i)


int main()
{
#ifdef _DEBUG
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
#endif

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test)
	{
		int k, n;
		string s;
		cin >> k;
		map<string, bool> used;
		set<string> eng;
		getline(cin, s);
		for (int i = 0; i < k; ++i)
		{
			getline(cin, s);
			eng.insert(s);
		}

		cin >> n;
		getline(cin, s);
		int c = 0, ans = 0;
		for (int i = 0; i < n; ++i)
		{
			getline(cin, s);
			if (eng.find(s) != eng.end())
				if (!used[s])
					used[s] = true,
					++c;
			if (c == k)
				c = 1,
				used.clear(),
				used[s] = true,
				++ans;
		}

		printf("Case #%d: %d\n", test, ans);
	}
}
