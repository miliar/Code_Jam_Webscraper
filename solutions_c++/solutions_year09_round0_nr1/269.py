#include<stdio.h>
#include<algorithm>
using namespace std;
char str[5005][16];
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int len,n,m,i,j,k,ans;
	bool u[16][128];
	char our[30*16];
	scanf("%d%d%d",&len,&n,&m);
	for(i=0;i<n;i++)
		scanf("%s",str[i]);
	for(i=0;i<m;i++)
	{
		scanf("%s",our);
		memset(u,0,sizeof(u));
		k=0;
		for(j=0;j<len;j++)
			if(our[k]=='(')
			{
				while(true)
				{
					k++;
					if(our[k]==')')
						break;
					u[j][our[k]]=true;
				}
				k++;
			}
			else
			{
				u[j][our[k]]=true;
				k++;
			}
		ans=0;
		for(j=0;j<n;j++)
		{
			for(k=0;k<len;k++)
				if(!u[k][str[j][k]])
					break;
			if(k==len)
				ans++;
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
