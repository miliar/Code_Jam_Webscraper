#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <utility>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iomanip>

#define INF (INT_MAX / 2)
#define X first
#define Y second
#define ft first
#define sc second
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define pb push_back
#define mp(a, b) make_pair((a), (b))
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forl(i, n) for(int i = 1; i <= int(n); i++)
#define sqr(a) ((a) * (a))
#define PI 3.1415926535897932384626433832795

using namespace std;

typedef pair<__int64, __int64> pt;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	__int64 t;
	cin >> t;

	forn(test, t)
	{
		string s;
		cin >> s;

		vector<__int64> z(256, -1);
		z[s[0]] = 1;
		__int64 idx = 0;
		vector<__int64> ans;
		ans.pb(1);

		forl(i, s.length() - 1)
		{
			if(z[s[i]] == -1)
			{
				if(idx != 1)
					z[s[i]] = idx, idx++;
				else
					z[s[i]] = idx + 1, idx += 2;
			}
			ans.pb(z[s[i]]);
		}
		idx = *max_element(all(z)) + 1;
		reverse(all(ans));

		__int64 res = 0;
		vector<__int64> pos;
		pos.pb(1);
		forn(i, s.length() + 200)
			pos.pb(pos[i] * idx);

		forn(i, ans.size())
			res += ans[i] * pos[i];

		cout << "Case #" << test + 1 << ": " << res << endl;
	}

    return 0;
}