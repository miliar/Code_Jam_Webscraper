#include<iostream>
using namespace std;
int g[1011];
int main()
{
	freopen("E: \\C-small-attempt0.in","r",stdin);
	freopen("E: \\C-small-attempt0.out","w",stdout);
	int T,r,k,n,ans,temp,j,num,cnt=1;
	scanf("%d",&T);
	while(T--)
	{
		ans=0;temp=1;num=0;
		memset(g,0,sizeof(g));
		scanf("%d%d%d",&r,&k,&n);
		for(int i=1;i<=n;i++) {scanf("%d",&g[i]);num+=g[i];}
		if(num<=k) ans=num*r;
		else 
			while(r--)
			{
				int sum=0;
				for(int i=temp;;i++)
				{
					j=i%(n+1);
					sum+=g[j];
					if(sum>k )
					{
						sum-=g[j];
						temp=j;
						if(temp==0) temp=n;
						break;
					}
				}
				ans+=sum;
			}
			printf("Case #%d: %d\n",cnt,ans);
			cnt++;
	}
	return 0;
}