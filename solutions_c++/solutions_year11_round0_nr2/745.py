#include "stdafx.h"
#if 1
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ios>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <algorithm>
#include <utility>
#include <functional>
using namespace std;

#define mp(x, y) make_pair(x, y)
#define sz(v) (int) ((v).size())
#define rep(i, n) for (int i = 0; i < n; i++)

void solve();
int main()
{
#ifdef __HOME__
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif
	solve();
	return 0;
}

#endif

const int KInf = 10000000;

void solve()
{
	int T;
	cin >> T;
	rep(tc, T)
	{
		cout << "Case #" << tc + 1 << ": ";

		int C;
		cin >> C;
		map<pair<char, char>, char> cre;
		
		rep(i, C)
		{
			string v;
			cin >> v;
			cre[make_pair(v[0], v[1])] = v[2];
			cre[make_pair(v[1], v[0])] = v[2];
		}

		int D;
		cin >> D;
		vector<string> del(D);
		rep(i, D) cin >> del[i];

		vector<char> st;

		int N;
		cin >> N;
		string s;
		cin >> s;

		rep(i, N)
		{
			st.push_back(s[i]);

			if (sz(st) == 1)
				continue;

			pair<char, char> v(st[sz(st) - 1], st[sz(st) - 2]);
			if (cre.count(v))
			{
				st.pop_back();
				st.pop_back();
				st.push_back(cre[v]);
				continue;
			}

			int mm = KInf;
			rep(j, D)
			{
				if (del[j][0] == s[i])
				{
					rep(k, sz(st) - 1)
					{
						if (st[k] == del[j][1])
						{
							mm = min(mm, k);
							break;
						}
					}
				}
				if (mm == KInf && del[j][1] == s[i])
				{
					rep(k, sz(st) - 1)
					{
						if (st[k] == del[j][0])
						{
							mm = min(mm, k);
							break;
						}
					}
				}
			}

			if (mm != KInf)
				st.resize(0);
		}

		cout << '[';
		rep(i, sz(st))
		{
			if (i == 0) cout << st[i];
			else cout << ',' << ' ' << st[i];
		}
		cout << ']' << '\n';
	}
}
