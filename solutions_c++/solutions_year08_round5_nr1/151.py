#include<cstdio>
#include<algorithm>
#include<iostream>
#include<string>
#include<cmath>
#include<vector>
#include<list>
#include<queue>
#include<utility>
#include<set>
using namespace std;
#define ST first
#define ND second
#define PB push_back
#define MP make_pair
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
const int OO=(1<<30);
const bool dbg=0;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); ––x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define MAXN 6010

set<int> hor[MAXN];
set<int> ver[MAXN];
set<PII> pts;
int l;
vector<string> s;
VI t;

void init()
{
	for(int i=0;i<MAXN;i++)
	{
		hor[i].clear();
		ver[i].clear();
	}
	s.clear();
	t.clear();
	pts.clear();
}
void readCase()
{
	init();
	cin>>l;
	for(int i=0;i<l;i++)
	{
		string ss;
		int tt;
		cin>>ss>>tt;
		s.PB(ss);
		t.PB(tt);
	}
}
#define N 0
#define E 1
#define S 2
#define W 3

void computeCase(int cas)
{
	int x=MAXN/2,y=MAXN/2;
	int dir=N;
	for(int i=0;i<l;i++)
		for(int j=0;j<t[i];j++)
			for(int k=0;k<s[i].size();k++)
			{
				if(s[i][k]=='R'){dir++;dir%=4;}
				if(s[i][k]=='L'){dir+=3;dir%=4;}
				if(s[i][k]=='F')
				{
					if(dir==N)
					{	hor[y].insert(x);y++;}
					if(dir==S)
					{	hor[y-1].insert(x);y--;}
					if(dir==E)
					{	ver[x].insert(y);x++;}
					if(dir==W)
					{	ver[x-1].insert(y);x--;}
					if(dbg)printf("%d",dir);
				}
			}
	if(dbg)printf("\n");

	for(int x=0;x<MAXN;x++)
	{
		bool in=1;
		int poprz=0;
		for(set<int>::iterator it=ver[x].begin();it!=ver[x].end();it++)
		{
			if(dbg)printf("%d %d, %d\n",x-MAXN/2,*it-MAXN/2,(int)in);
			if(poprz==0){poprz=*it;continue;}
			if(!in)for(int y=poprz;y<*it;y++)
			{
				pts.insert(MP(x,y));
			}
			poprz=*it;
			in=!in;
		}
	}
	if(dbg)printf("\n");
	for(int y=0;y<MAXN;y++)
	{
		bool in=1;
		int poprz=0;
		for(set<int>::iterator it=hor[y].begin();it!=hor[y].end();it++)
		{
			if(dbg)printf("%d %d, %d\n",*it-MAXN/2,y-MAXN/2,(int)in);
			if(poprz==0){poprz=*it;continue;}
			if(!in)for(int x=poprz;x<*it;x++)
			{
				pts.insert(MP(x,y));
			}
			poprz=*it;
			in=!in;
		}
	}

	printf("Case #%d: %d\n",cas,(int)pts.size());
	if(dbg)FOREACH(p,pts)
	{
		printf("%d %d\n",p->ST-MAXN/2,p->ND-MAXN/2);
	}


}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		readCase();
		computeCase(i+1);
	}
	return 0;
}

