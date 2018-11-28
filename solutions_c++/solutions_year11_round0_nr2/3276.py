#include<stdio.h>

int c,d,n;
int cp[40][3];
int dp[40][2];
int ans[110];
char tstr[110];
int main(int argc,char* argv[])
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	scanf("%d",&T);
	int cas=1;
	while(T--)
	{
	scanf("%d",&c);
	char str[5];
	for(int i=0;i<c;i++)
	{
		scanf("%s",str);
		cp[i][0]=str[0]-'A';
		cp[i][1]=str[1]-'A';
		cp[i][2]=str[2]-'A';
	}
	scanf("%d",&d);
	for(int i=0;i<d;i++)
	{
		scanf("%s",str);
		dp[i][0]=str[0]-'A';
		dp[i][1]=str[1]-'A';
	}
	scanf("%d",&n);
	scanf("%s",tstr);
	int len=0;
	int flag[30];
	for(int i=0;i<30;i++)
		flag[i]=0;
	for(int i=0;i<n;i++)
	{
		if(len==0)
		{
			ans[len++]=tstr[i]-'A';
			flag[tstr[i]-'A']++;
		}
		else
		{
			int tmp=tstr[i]-'A';
			int y=0;
			for(int j=0;j<c;j++)
			{
				if((cp[j][0]==ans[len-1]&&cp[j][1]==tmp)||(cp[j][0]==tmp&&cp[j][1]==ans[len-1]))
				{
					flag[ans[len-1]]--;
					y=1;
					ans[len-1]=cp[j][2];
					flag[cp[j][2]]++;
					break;
				}
			}
			if(0 == y )
			{
				flag[tmp]++;
				for(int j=0;j<d;j++)
				{
					if(flag[dp[j][0]]>0&&flag[dp[j][1]]>0)
					{
						for(int ii=0;ii<30;ii++)
							flag[ii]=0;
						len=0;
						y=1;
						break;
					}
				}
				if(0==y)
					flag[tmp]--;
			}
			if(0==y)
			{
				flag[tmp]++;
				ans[len++]=tmp;
			}
				
		}

	}
	printf("Case #%d: [",cas++);
	for(int i=0;i<len;i++)
	{
		if(i>0)
			printf(", ");
		printf("%c",'A'+ans[i]);
	}
	printf("]\n");
}
	return 0;
}
