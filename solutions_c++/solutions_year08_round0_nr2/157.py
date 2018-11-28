#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<n; ++i)
#define FOR(var,pocz,koniec) for (int var=pocz; var<=koniec; ++var)
#define FORD(var,pocz,koniec) for (int var=pocz; var>=koniec; --var)
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

typedef struct tita{int at,dt;} tt;

int ta,an,bn;
VI a,b;

bool operator<(const tt &t1,const tt &t2)
{
	return t1.at < t2.at;
}

vector<tt> at,bt;

void main()
{
	int probnum,numtest;
	string ins;
	cin>>numtest;
	for(probnum=0;probnum<numtest;probnum++)
	{
		int i,j,k;
		printf("Case #%d: ",probnum+1);
		cin>>ta;
		cin>>an>>bn;
		at.clear();bt.clear();a.clear();b.clear();
		for(i=0;i<an;i++)
		{
			tt t;
			char b[1000];
			cin>>b;
			t.at = ((b[0]-'0')*10+(b[1]-'0'))*60+((b[3]-'0')*10+(b[4]-'0'));
			cin>>b;
			t.dt = ((b[0]-'0')*10+(b[1]-'0'))*60+((b[3]-'0')*10+(b[4]-'0'));
			at.push_back(t);
		}
		for(i=0;i<bn;i++)
		{
			tt t;
			char b[1000];
			cin>>b;
			t.at = ((b[0]-'0')*10+(b[1]-'0'))*60+((b[3]-'0')*10+(b[4]-'0'));
			cin>>b;
			t.dt = ((b[0]-'0')*10+(b[1]-'0'))*60+((b[3]-'0')*10+(b[4]-'0'));
			bt.push_back(t);
		}
		sort(ALL(at));
		sort(ALL(bt));

		int ai=0,bi=0,nta=0,ntb=0,ct=0;
		while(ai!=an&&bi!=bn)
		{
			if(at[ai].at<bt[bi].at)
			{
				ct=at[ai].at;
				int tf=0;
				for(j=0;j<a.size();j++)if(a[j]<=ct){tf=1;a.erase(a.begin()+j);break;}
				if(!tf)nta++;
				b.push_back(at[ai].dt+ta);
				ai++;
			}
			else
			{
				ct=bt[bi].at;
				int tf=0;
				for(j=0;j<b.size();j++)if(b[j]<=ct){tf=1;b.erase(b.begin()+j);break;}
				if(!tf)ntb++;
				a.push_back(bt[bi].dt+ta);
				bi++;
			}
		}
		if(bi==bn)
		{
			while(ai!=an)
			{
				ct=at[ai].at;
				int tf=0;
				for(j=0;j<a.size();j++)if(a[j]<=ct){tf=1;a.erase(a.begin()+j);break;}
				if(!tf)nta++;
				ai++;
			}
		}
		if(ai==an)
		{
			while(bi!=bn)
			{
				ct=bt[bi].at;
				int tf=0;
				for(j=0;j<b.size();j++)if(b[j]<=ct){tf=1;b.erase(b.begin()+j);break;}
				if(!tf)ntb++;
				bi++;
			}
		}

		cout<<nta<<" "<<ntb<<endl;
	}
}