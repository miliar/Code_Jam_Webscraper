#include<iostream>
#include<algorithm>
#include<cmath>

using namespace std;

#define N 55

int x[N],v[N],f[N];

int main()
{
	int t,cas=1,n,m,dis,time,i,j,k,coun,tt,ans;
	freopen("in.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d%d",&n,&m,&dis,&time);
		for(i=0;i<n;i++)
			scanf("%d",&x[i]);
		for(i=0;i<n;i++)
			scanf("%d",&v[i]);
		printf("Case #%d: ",cas++);
		for(coun=i=0;i<n;i++)
		{
			tt=dis-x[i];
			if(tt%v[i]==0&&tt/v[i]<=time||tt%v[i]&&tt/v[i]<time)
			{
				coun++;
				f[i]=1;
			}
			else f[i]=0;
		}
		if(coun<m)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		for(ans=j=k=0,i=n-1;i>=0;i--)
		{
			if(f[i]==1)
			{
				k++;
				ans+=j;
				if(k==m)
					break;
			}
			else j++;
		}
		printf("%d\n",ans);
	}
	return 0;
}


	