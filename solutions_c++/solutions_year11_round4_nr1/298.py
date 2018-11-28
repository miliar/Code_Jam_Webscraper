#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int T;
int X,S,R,N;
double t;
pair<double,double> a[1005];
int B[1005],E[1005],w[1005];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);
		for(int i=0;i<N;i++)
		{
			scanf("%d%d%d",&B[i],&E[i],&w[i]);
			a[i].second=E[i]-B[i];
			a[i].first=w[i];
			X-=a[i].second;
		}
		a[N].second=X;
		a[N].first=0;
		sort(a,a+N+1);
		double ans=0;
		bool flag=false;
		for(int i=0;i<=N;i++)
		{
			if(a[i].second<=(a[i].first+R)*t)
			{
				a[i].first+=R;
				t-=a[i].second/(a[i].first);
			}
			else
			{
				if(!flag)
				{
					a[N+1].first=(a[i].first+R);
					a[N+1].second=a[N+1].first*t;
					a[i].second-=a[N+1].second;
					t=0;
					flag=true;
				}
				a[i].first+=S;
			}
		}
		for(int i=0;i<=N+flag;i++)
			ans+=a[i].second/a[i].first;
		printf("Case #%d: %.10f\n",test,ans);
	}
	return 0;
}
