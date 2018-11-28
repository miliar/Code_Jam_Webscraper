#include <cstdio>
#include <cstring>
#include <algorithm>
#define LL long long
#define MAX 5005
using namespace std;
		
int L,N,C;
double t;
int a[MAX];
int dist[1000000];
bool b[MAX];

// one booster
double solve()
{
	double time=0;

	for(int i=0;i<N;)
	{
		if(b[i]) // there is a booster at i	
		{
			if(time>=t) // completed
				time+=dist[i++];
			else
			{
				// more t-time is required to get boost
				// In that time ship will cover 'd'
				double d=(t-time)/2;
				while(i<N && d-dist[i]>=0)
				{
					d-=dist[i];
					i++;
				}
				time+=(t-time);
				time+=(dist[i++]-d);
			}
		}
		else time+=(2*dist[i++]);
	}
	return time;
}

int main()
{
	int cases;
	
	scanf("%d",&cases);
	
	for(int iD=1;iD<=cases;iD++)
	{
		printf("Case #%d: ",iD);
		scanf("%d %lf %d %d",&L,&t,&N,&C);
		for(int i=0;i<C;i++)
			scanf("%d",&a[i]);
		for(int i=0;i<=N;i++)
			for(int j=0;j<C;j++)
				dist[i*C+j]=a[j];
		
		memset(b,0,sizeof b);
		double ans=solve();

		if(L==1)
		{
			for(int i=0;i<N;i++)
			{
				b[i]=1;
				ans=min(ans,solve());
				b[i]=0;
			}			
		}
		if(L==2)
		{
			for(int i=0;i<N;i++)
			{
				for(int j=i+1;j<N;j++)
				{
					b[i]=1;b[j]=1;
					ans=min(ans,solve());
					b[i]=0;b[j]=0;
				}
			}		
		}
		printf("%.0lf\n",ans);
	}

	return 0;
}

