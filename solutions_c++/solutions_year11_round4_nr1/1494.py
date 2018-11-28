#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<ctime>
#include<map>
#include<vector>
#include<queue>
#include<sstream>
#include<stack>
using namespace std;

#define INF 0x7fffffff
#define EPS 1e-8

typedef long long LL;

void init(int mode,string problem)
{
	string infile="C:\\Users\\LaiLi\\Desktop\\GCJ\\";
	string outfile="C:\\Users\\LaiLi\\Desktop\\GCJ\\";
	if(mode==0)
		return;
	if(mode==1)
	{
		infile+=problem+"-small.in";
		outfile+=problem+"-small.out";
	}
	if(mode==2)
	{
		infile+=problem+"-large.in";
		outfile+=problem+"-large.out";
	}
	freopen(infile.c_str(),"r",stdin);
	freopen(outfile.c_str(),"w",stdout);
}

struct node
{
	int b,e,w;
}p[1005];

bool cmp(node p,node q)
{
	return p.w<q.w;
}

void solve()
{
	int N,i,j;
	int X,S,R,t,m;
	double st;
	scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
	m=X;
	st=t;
	for(i=0;i<N;i++)
	{
		scanf("%d%d%d",&p[i].b,&p[i].e,&p[i].w);
		m-=p[i].e-p[i].b;
	}
	sort(p,p+N,cmp);
	double ans=0.0;
	if(m>R*st)
	{
		ans+=st+(m-R*st)/double(S);
		st=0.0;
	}
	else
	{
		ans+=m/double(R);
		st-=ans;
	}
	for(i=0;i<N;i++)
	{
		int d=p[i].e-p[i].b;
		if(st<=EPS)
		{
			ans+=d/double(S+p[i].w);
		}
		else
		{
			if(st*(R+p[i].w)>=d)
			{
				ans+=d/double(R+p[i].w);
				st-=d/double(R+p[i].w);
			}
			else
			{
				ans+=st+(d-st*(R+p[i].w))/(S+p[i].w);
				st=0.0;
			}
		}
	}
	printf("%.8lf\n",ans);
}

int main()
{
	init(1,"A");

	int T,cs;
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		printf("Case #%d: ",cs);
		solve();
		fflush(stdout);
	}
}