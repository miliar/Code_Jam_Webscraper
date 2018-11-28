#include<cstdio>
#include<cstring>
using namespace std;

int t,n,w[25],a,sum,minn;
bool pos;

void count(int k)
{
	int j=1,c=0;
	while(j<=k)
	{
		if ((j&k)!=0) w[c]++;
		j<<=1;
		c++;
	}
}

int main()
{
	freopen("text.in","r",stdin);
	freopen("text.out","w",stdout);
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		scanf("%d",&n);
		minn=9999999;
		sum=0;
		memset(w,0,sizeof(w));
		for(int i=0;i<n;i++) 
		{
			scanf("%d",&a);
			sum+=a;
			if (a<minn) minn=a;
			count(a);
		}
		pos=true;
		for(int i=0;i<=20;i++)
		{
			if (w[i]%2==1)
			{
				pos=false;
				break;
			}
		}
		printf("Case #%d: ",cas);
		if (pos) printf("%d\n",sum-minn);
		else printf("NO\n");
	}
	return 0;
}
