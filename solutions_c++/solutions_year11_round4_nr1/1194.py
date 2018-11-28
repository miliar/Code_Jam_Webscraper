#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define eps 1e-8
int T,X,S,R,N;
double t;
typedef struct
{
	int st,end,speed;
}Edge;
Edge e[3005];
int cmp1(Edge a,Edge b)
{
	return a.st<b.st;
}
int cmp2(Edge a,Edge b)
{
	return a.speed<b.speed;
}
int main()
{
	freopen("yy.in","r",stdin);
	freopen("yy.out","w",stdout);
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		int i,j;
		scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);
		for(int i=1;i<=N;i++)
		{
			scanf("%d%d%d",&e[i].st,&e[i].end,&e[i].speed);
			e[i].speed+=S;
		}
		sort(e+1,e+1+N,cmp1);
		int num=0;
		if(e[1].st>0)
		{
			num++;
			e[N+num].st=0;
			e[N+num].end=e[1].st;
			e[N+num].speed=S;
		}
		for(i=2;i<=N;i++)
			if(e[i].st>e[i-1].end)
			{
				num++;
				e[N+num].st=e[i-1].end;
				e[N+num].end=e[i].st;
				e[N+num].speed=S;
			}
		if(e[N].end<X)
		{
			num++;
			e[N+num].st=e[N].end;
			e[N+num].end=X;
			e[N+num].speed=S;
		}
		N=N+num;
		sort(e+1,e+1+N,cmp2);
		double ans=0;
		for(i=1;i<=N;i++)
		{
			if(t*(e[i].speed-S+R)>=e[i].end-e[i].st)
			{
				double temp=1.0*(e[i].end-e[i].st)/(e[i].speed-S+R);
				ans+=temp;
				t-=temp;
			}
			else if(t>0)
			{
				double temp1=1.0*t*(e[i].speed-S+R);
				double temp2=e[i].end-e[i].st-temp1;
				ans+=1.0*temp2/e[i].speed+t;
				t=0;
			}
			else ans+=1.0*(e[i].end-e[i].st)/e[i].speed;
		}
		printf("Case #%d: %.7lf\n",cas,ans);
	}
	return 0;
}
			
		
		
		
		
		
		
		
		
	
