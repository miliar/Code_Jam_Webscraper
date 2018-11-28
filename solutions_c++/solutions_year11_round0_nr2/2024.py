//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
using namespace std;

int t,x;
string s,st;
bool ktmu;

int main()
{
	scanf("%d",&t);
	FORN(i,t)
	{
		scanf("%d",&x);
		vector<PCC> co[26];
		FORN(j,x)
		{
			cin >> s;
			co[(int)s[0]-'A'].pb(mp(s[1],s[2]));
			co[(int)s[1]-'A'].pb(mp(s[0],s[2]));
		}
		scanf("%d",&x);
		vector<char> opp[26];
		FORN(j,x)
		{
			cin >> s;
			opp[(int)s[0]-'A'].pb(s[1]);
			opp[(int)s[1]-'A'].pb(s[0]);
		}
		scanf("%d",&x);
		cin >> st;
		s = "";
		FORN(j,st.sz())
		{
			s += st[j];
			if (s.sz() >= 2)
				FORN(k,co[(int)s[s.sz()-1]-'A'].sz())
					if (co[(int)s[s.sz()-1]-'A'][k].fi == s[s.sz()-2])
					{
						s += co[(int)s[s.sz()-1]-'A'][k].se;
						s.del(s.sz()-3,2);
						break;
					}
			ktmu = false;
			FORN(k,s.sz()-1)
			{
				FORN(l,opp[(int)s[s.sz()-1]-'A'].sz())
					if (s[k] == opp[(int)s[s.sz()-1]-'A'][l])
					{
						ktmu = true;
						s = "";
						break;
					}
				if (ktmu)
					break;
			}
		}
		printf("Case #%d: [",i+1);
		FORN(j,s.sz())
			if (j == 0)
				cout << s[j];
			else
				cout << ", " << s[j];
		printf("]\n");
	}
}
