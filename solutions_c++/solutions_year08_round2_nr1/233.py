#include<iostream>
#include<algorithm>
#include<set>
#include<queue>
#include<list>
#include<vector>
#include<string>
#include<utility>
using namespace std;
#define OO (1<<30)
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;
typedef pair<LL,LL> PLL;
#define REP(i,n) for(int i=0;i<n;++i)
#define SIZE(x) (int)x.size()
#define ALL(x) x.begin(),x.end()
#define VAR(v,n) __typeof(n) v=(n)
#define FOREACH(it,x) for(VAR(it,(x).begin());it!=(x).end();it++)
const bool dbg=0;

long long tab[3][3];
LL N,A,B,C,D,x0,y0,M;
set<vector<PII> > perm;
vector<PII> allPairs()
{
	vector<PII> r;
	for(int i=0;i<3;i++)
		for(int j=0;j<3;j++)
			r.PB(MP(i,j));
	return r;
}
bool ok(vector<PII> v)
{
	return (((v[0].ST+v[1].ST+v[2].ST)%3==0)&&((v[0].ND+v[1].ND+v[2].ND)%3==0));
}
void initPerm()
{
	perm.clear();
	vector<PII> pairs=allPairs();
	FOREACH(it,pairs)
		FOREACH(jt,pairs)
			FOREACH(kt,pairs)
			{
				vector<PII> v;
				v.PB(*it);
				v.PB(*jt);
				v.PB(*kt);
				sort(ALL(v));
				if(ok(v))
					perm.insert(v);
			}
	if(dbg)
	{
		FOREACH(vt,perm)
		{
			printf("[(%d,%d),(%d,%d),(%d,%d)]\n",(*vt)[0].ST,(*vt)[0].ND,(*vt)[1].ST,(*vt)[1].ND,(*vt)[2].ST,(*vt)[2].ND);
		}
	}
}
LL tbl(PII p)
{return tab[p.ST][p.ND];}
LL computePerm(vector<PII> v)
{
	if(v[0]==v[1] && v[1]==v[2])
	{
		return ( tbl(v[0] )*( tbl(v[0])-1 )*( tbl(v[0])-2 ) )/6;
	}
	if(v[0]==v[1])
	{
		return (tbl(v[0])*( tbl(v[0])-1 )*tbl(v[2]))/2;
	}
	if(v[1]==v[2])
	{
		return ( tbl(v[0])*tbl(v[1])*( tbl(v[1])-1 ) )/2;
	}
	return tbl(v[0])*tbl(v[1])*tbl(v[2]);
}

void init()
{
	REP(i,3)
		REP(j,3)
			tab[i][j]=0;
}
void read()
{
	init();
	scanf("%lld%lld%lld%lld%lld%lld%lld%lld",&N,&A,&B,&C,&D,&x0,&y0,&M);
	LL X=x0,Y=y0;
	for(int i=0;i<N;i++)
	{
		if(dbg)printf("%lld %lld\n",X,Y);
		tab[X%3][Y%3]++;
		X=(A*X+B)%M;
		Y=(C*Y+D)%M;
	}
	if(dbg)
	{
		REP(i,3)
		{
			REP(j,3)
				printf("%lld ",tab[j][i]);
			printf("\n");
		}
	}
}

void compute(int cas)
{
	LL res=0;
	FOREACH(per,perm)
	{
		res+=computePerm(*per);
	}
	printf("Case #%d: %lld\n",cas+1,res);
}

int main()
{
	initPerm();
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		read();
		compute(i);
	}
	return 0;
}
