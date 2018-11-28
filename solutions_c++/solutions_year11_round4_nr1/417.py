#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>
using namespace std;

typedef struct
{
	int s,e;
	int pre,cur;
	int type;
}Segment;
Segment s[2005];
int sCnt;
int L,N,walk,run,T;

bool cmp(const Segment &P,const Segment &Q)
{
	return (P.cur-P.pre)*Q.cur*Q.pre>(Q.cur-Q.pre)*P.cur*P.pre;
}

int fcmp(double a,double b)
{
	if(fabs(a-b)<1E-9) return 0;
	if(a>b) return 1;
	return -1;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("lowesy.out","w",stdout);
	int _,cases=1;
	scanf("%d",&_);
	while(_--)
	{
		scanf("%d%d%d%d%d",&L,&walk,&run,&T,&N);
		for(int i=0;i<N;i++)
		{
			int w;
			scanf("%d%d%d",&s[i].s,&s[i].e,&w);
			s[i].type=0;
			s[i].pre=w+walk,s[i].cur=w+run;
		}
		s[N].s=s[N].e=0;
		s[N].pre=walk,s[N].cur=run,s[N].type=1;
		if(s[0].s!=0) s[N].e+=s[0].s;
		for(int i=1;i<N;i++) s[N].e+=s[i].s-s[i-1].e;
		if(s[N-1].e!=L) s[N].e+=L-s[N-1].e;
		sort(s,s+N+1,cmp);
		double t=T;
		int id=0;
		double res=0.0;
		for(int i=0;i<=N;i++)
			res+=(s[i].e-s[i].s+0.0)/(s[i].pre+0.0);
		while(fcmp(t,0.0)>0&&id<=N)
		{
			double l=s[id].cur*t;
			if(fcmp(l,s[id].e-s[id].s)<=0)
			{
				res=res-(s[id].e-s[id].s+0.0)/(s[id].pre+0.0)+t+(s[id].e-s[id].s-l)/(s[id].pre);
				t=0.0;
			}
			else
			{
				double t0=(s[id].e-s[id].s+0.0)/(s[id].cur+0.0);
				t-=t0;
				res=res-(s[id].e-s[id].s+0.0)/(s[id].pre+0.0)+t0;
			}
			id++;
		}
		printf("Case #%d: %.7f\n",cases++,res);
	}
	return 0;
}