#include<iostream>
using namespace std;

int pos[50];
int v[50];
int lefttime[50];
int canreach[50];

int main()
{
	int tcase,ncase,n,k,b,t,i,j,h,ans;
	scanf("%d",&ncase);
	for(tcase=1;tcase<=ncase;tcase++)
	{
		printf("Case #%d: ",tcase);
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for(i=0;i<n;i++)
		{
			scanf("%d",&pos[i]);
		}
		j=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&v[i]);
			if((b-pos[i])<=v[i]*t)
			{
				j++;
				canreach[i]=1;
			}
			else
			{
				canreach[i]=0;
			}
		}
		if(j<k)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		ans=0;
		for(i=n-1;i>=0&&k>0;i--)
		{
			if(canreach[i]==1)
			{
				k--;
				h=0;
				for(j=i+1;j<n;j++)
					if(canreach[j]==0)
						ans++;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}