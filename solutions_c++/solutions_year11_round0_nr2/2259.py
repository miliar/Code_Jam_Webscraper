#include <stdio.h>
#include <string.h>
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,i,j,k;
	int c,d,n;
	char  compose[30][30];
	char  deleting[30][30];
	scanf("%d",&t);
	char cmd[20];
	char str[200];

	for (i=1;i<=t;i++)
	{
		memset(deleting,0,sizeof(deleting));
		memset(compose,0,sizeof(compose));
		scanf("%d",&c);
		for (j=1;j<=c;j++)
		{
			scanf("%s",&cmd);
			compose[cmd[0]-'A'][cmd[1]-'A']=cmd[2];
			compose[cmd[1]-'A'][cmd[0]-'A']=cmd[2];
		}		
		scanf("%d",&d);
		for (j=1;j<=d;j++)
		{
			scanf("%s",&cmd);
			deleting[cmd[0]-'A'][cmd[1]-'A']=1;
			deleting[cmd[1]-'A'][cmd[0]-'A']=1;
		}
		scanf("%d",&n);
		scanf("%s",&str);
		int ans=0;
		for (j=1;j<n;j++)
		{
			char tmp;
			for(k=j-1;k>=ans;k--)if (str[k]!=0)
			{
				tmp=str[k];
				break;
			}
			if (compose[str[j]-'A'][tmp-'A']!=0)
			{
				str[k]=0;
				str[j]=compose[str[j]-'A'][tmp-'A'];
			}
			for (k=j-1;k>=ans;k--)
			{
				if (str[k]!=0&&deleting[str[j]-'A'][str[k]-'A']!=0)
				{
					ans=j+1;
					j++;
					break;
				}
			}			
		}
		bool yes=true;
		printf("Case #%d: [",i);
		for (k=ans;k<n;k++)
		{
			if (str[k]!=0)
			{
				if (yes)
				{
					yes=false;
					printf("%c",str[k]);
				}
				else printf(", %c",str[k]);
			}
		}
		printf("]\n");
	}
	return 0;
}