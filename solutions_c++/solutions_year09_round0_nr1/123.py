#include <iostream>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <string>

using namespace std;

#define FOR(i,a,b) for(int i(a), _n(b); i<=_n; i++)
#define FR(i,b) FOR(i,0,b-1)
#define REP(i,a,b) for(int i(a), _n(b); i >= _n; i--)
#define _M(a) memset(a,0,sizeof(a))
#define IN scanf
#define OUT printf
#define sqr(q) ((q)*(q))
#define ll long long
#define ul unsigned ll
#define INF 1000000000

int KT, L, D;
char dic[6000][20];
char cur[10000];
set <char> S;
list <int> ls;

void sett(int &p)
{
	S.clear();
	if (cur[p] != '(') S.insert(cur[p]); 
	else for(p++; cur[p] != ')'; p++) S.insert(cur[p]);
	p++;
}

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	IN("%d%d%d\n",&L, &D, &KT);
	FR(i,D) gets(dic[i]);
	
	FOR(test, 1, KT)
	{
		gets(cur);
		int p = 0;
		sett(p);
		ls.clear();
		FR(i,D) if (S.find(dic[i][0]) != S.end()) ls.push_back(i);
		
		FOR(i,1,L-1)
		{
			sett(p);
			for(list<int>::iterator c = ls.begin(); c != ls.end();)
			{
				if (S.find(dic[*c][i]) == S.end()) 
				{
					list<int>::iterator t = c;
					c++;
					ls.erase(t);
				} else c++;
			}
		}
		
		OUT("Case #%d: %d\n", test, ls.size());
	}
	
	return 0;
}
