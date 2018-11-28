#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <deque>
using namespace std;

#define VAR(a, b) __typeof(b) a = b
#define FORAB(i, a, b) for(VAR(i, a); i != b; i++)
#define FOR(i, n) FORAB(i, 0, n)
#define RFOR(i, a, b) for(VAR(i, a); i != b; i--)
#define FOREACH(it, c) FORAB(i, (c).begin(), (c).end())
#define RFOREACH(it, c) FORAB(i, (c).rbegin(), (c).rend())
#define ALL(c) (c).begin(), (c).end()
#define MP(a, b) pair<__typeof(a), __typeof(b)> (a, b)
#define PB(c) push_back(c)
#define BLAH(a) cerr << a << endl
#define DBG(a) BLAH(#a << ": " << a)

#define gin int T; cin >> T; for(int gtest = 1; gtest <= T; gtest++)
#define gout cout <<"Case #" << gtest << ": "
#define gprintf(s, a...) printf(strcat("Case #%i: ", s), gtest, a)

int gcd(int a, int b)
{
	if(!b) return a;
	return gcd(b, a % b);
}

int main()
{
	gin
	{
		int c, d, n;
		char combo[26][26];
		FOR(i, 26) FOR(j, 26) combo[i][j] = 0;
		bool opp[26][26];
		FOR(i, 26) FOR(j, 26) opp[i][j] = false;
		cin >> c >> ws;
		FOR(i, c)
		{
			string s; cin >> s;
			combo[s[0]-'A'][s[1]-'A'] = s[2];
			combo[s[1]-'A'][s[0]-'A'] = s[2];
		}
		cin >> d;
		FOR(i, d)
		{
			string s; cin >> s;
			opp[s[0]-'A'][s[1]-'A'] = true;
			opp[s[1]-'A'][s[0]-'A'] = true;
		}
		cin >> n;
		deque<char> ans;
		char k, p= 0;
		cin >> k;
		ans.PB(k);
		FORAB(i, 1, n)
		{
			p = ans.empty() ? 0 : ans.back();
			cin >> k;
			bool foundOpp = false;
			if(p && combo[k-'A'][p-'A'])
			{
				foundOpp = true;
				ans.pop_back();
				ans.PB(combo[k-'A'][p-'A']);
			}
			else if(p)
				FOR(j, ans.size())
					if(opp[ans[j]-'A'][k-'A'])
					{
						foundOpp = true;
						ans.clear();
						break;
					}
			if(!foundOpp) ans.PB(k);
		}
		gout << "["; FOREACH(i, ans) cout << *i << (i - ans.begin() == ans.size() - 1 ? "": ", ");
		cout << "]" << endl;
	}
}
