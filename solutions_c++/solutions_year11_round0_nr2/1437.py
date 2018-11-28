/* by Ashar Fuadi [fushar] */

#include <cstdio>
#include <cstring>

#include <vector>
#include <string>
#include <stack>
#include <list>
#include <map>
#include <utility>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i = 0; i < (int)n; i++)
#define FOR(i, a, b) for (int i = (int)a; i <= (int)b; i++)
#define REPE(i,c) for (typeof((c).end()) i = (c).begin(); i != (c).end(); ++i)
#define RESET(c,v) memset(c, v, sizeof(c))

#define pb push_back
#define mp make_pair
#define DEBUG 1
#define PRINT(x...) DEBUG && printf(x)

int T;
int C, D, N;
int main()
{
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	
	cin >> T;
	REP(tc, T)
	{
		char comb[256][256] = {};
		bool oppo[256][256] = {};
		cin >> C;
		REP(i, C)
		{
			string s;
			cin >> s;
			comb[s[0]][s[1]] = comb[s[1]][s[0]] = s[2];
		}
		cin >> D;
		REP(i, D)
		{
			string s;
			cin >> s;
			oppo[s[0]][s[1]] = oppo[s[1]][s[0]] = true;
		}
		cin >> N;
		string s;
		cin >> s;
		
		vector<char> elem;
		REP(i, N)
		{
			elem.pb(s[i]);
			
			// combine
			while (elem.size() >= 2 && comb[elem[elem.size()-1]][elem[elem.size()-2]])
			{
				char lho = comb[elem[elem.size()-1]][elem[elem.size()-2]];
				elem.pop_back();
				elem.pop_back();
				elem.pb(lho);
			}
			
			// oppose
			if (!elem.empty())
			REP(j, (int)elem.size()-1)
				if (oppo[elem[j]][elem.back()])
				{
					elem.clear();
					break;
				}
		}
		cout << "Case #" << tc+1 << ": [";
		REP(i, elem.size())
		{
			if (i)
				cout << ", ";
			cout << elem[i];
		}
		cout << "]" << endl;
	}
}
