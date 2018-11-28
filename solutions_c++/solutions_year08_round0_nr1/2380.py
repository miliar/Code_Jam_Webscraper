#include<iostream>
using namespace std;
int flag[300];
char query[300];
char a[300][300];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int count;
	int ans;
    int n,i,j,k;
	int S,querynum;
	char temp[100];
	int e;
	scanf("%d",&n);
	for(e=1;e<=n;e++)
	{
		memset(flag,0,sizeof(flag));
		count=0;
		ans=0;
		scanf("%d",&S);
		gets(temp);

		for(i=0;i<S;i++)
			gets(a[i]);

		scanf("%d",&querynum);
		gets(temp);

		for(i=0;i<querynum;i++)
		{
			gets(query);
			for(j=0;j<S;j++)
				if(strcmp(a[j],query)==0)
				{
					if(flag[j]==0)
					{
						flag[j]=1;
						count++;
						if(count==S)
						{
							ans++;
							count=1;
							for(k=0;k<=S;k++)
							  if(k!=j)
								flag[k]=0;
							  else 
								flag[k]=1;
						}
						else
							;
					}
					break;
				}
				
		}
		printf("Case #%d: %d\n",e,ans);
	}
	return 0;
}