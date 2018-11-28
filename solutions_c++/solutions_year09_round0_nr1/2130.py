#include<stdio.h>
#include<string.h>
#include<stdlib.h>
char word[5100][17];
bool dp[550][16][26];
int len,c,n;
char input[10000];
int res[10000];
int main()
{
	freopen("fuckk.in","r",stdin);
	freopen("ff.out.txt","w",stdout);
	int i,j,k;
	char ch,ch2;;
	int cnt,flag;
	int case_cnt=1;
	while(scanf("%d%d%d",&len,&c,&n)!=EOF)
	{
		memset(res,0,sizeof(res));
		getchar();
		memset(dp,0,sizeof(dp));
		for(i=1;i<=c;i++)
			gets(word[i]);
		for(i=1;i<=n;i++)
		{
			flag=0;
			gets(input);
			cnt=0;
			for(j=0;input[j];j++)
			{
				if(input[j]=='(')
				{
					flag=1;
					for(k=j+1;input[k]!=')';k++)
					{
						dp[i][cnt][input[k]]=1;
					}
					cnt++;
					j=k;
				}
				else if(input[j]>='a'&&input[j]<='z')
				{
					//cnt++;
					dp[i][cnt][input[j]]=1;
					cnt++;
				}
			}
		}
		int s;
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=c;j++)
			{
				for(k=0;k<len;k++)
				{
					if(dp[i][k][word[j][k]]==0)
						break;
				}
				if(k==len)
					res[i]++;
			}
		}
		for(i=1;i<=n;i++)
		{
			printf("Case #%d: ",case_cnt++);
			printf("%d\n",res[i]);
		}
	}
}