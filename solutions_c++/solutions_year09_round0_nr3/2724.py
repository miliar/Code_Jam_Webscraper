#include<iostream>
#include<cstring>
#include<string>
char str[505];
int dp[505][5]; 
const int MOD=10000;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j;
	int n;
	scanf("%d",&n);
	getchar();
	int cas=1;
	for(cas=1;cas<=n;cas++)
	{
		gets(str);
		memset(dp,0,sizeof(dp));
		int len=strlen(str);

		int res=0;
		for(i=0;i<len;i++)
		{
			if(str[i]=='w')
			{
				dp[i][0]=1;
			}
			else if(str[i]=='e')
			{
				for(j=0;j<i;j++)
				{
					if(str[j]=='w'&&dp[j][0])
						dp[i][0]=(dp[i][0]+dp[j][0])%MOD;
					if(str[j]=='m'&&dp[j][0])
						dp[i][1]=(dp[i][1]+dp[j][0])%MOD;
					if(str[j]=='d'&&dp[j][0])
						dp[i][2]=(dp[i][2]+dp[j][0])%MOD;
				}
			}
			else if(str[i]=='l')
			{
				for(j=0;j<i;j++)
				{
					if(str[j]=='e'&&dp[j][0])
						dp[i][0]=(dp[i][0]+dp[j][0])%MOD;
				}
			}
			else if(str[i]=='c')
			{
				for(j=0;j<i;j++)
				{
					if(str[j]=='l'&&dp[j][0])
						dp[i][0]=(dp[i][0]+dp[j][0])%MOD;
					if(str[j]==' '&&dp[j][1])
						dp[i][1]=(dp[i][1]+dp[j][1])%MOD;
				}
			}
			else if(str[i]=='o')
			{
				for(j=0;j<i;j++)
				{
					if(str[j]=='c'&&dp[j][0])
						dp[i][0]=(dp[i][0]+dp[j][0])%MOD;
					if(str[j]=='t'&&dp[j][0])
						dp[i][1]=(dp[i][1]+dp[j][0])%MOD;
					if(str[j]=='c'&&dp[j][1])
						dp[i][2]=(dp[i][2]+dp[j][1])%MOD;
				}
			}
			else if(str[i]=='a')
			{
				for(j=0;j<i;j++)
				{
					if(str[j]=='j'&&dp[j][0])
						dp[i][0]=(dp[i][0]+dp[j][0])%MOD;
				}
			}
			else if(str[i]=='j')
			{
				for(j=0;j<i;j++)
				{
					if(str[j]==' '&&dp[j][2])
						dp[i][0]=(dp[i][0]+dp[j][2])%MOD;
				}
			}
			else if(str[i]=='t')
			{
				for(j=0;j<i;j++)
				{
					if(str[j]==' '&&dp[j][0])
						dp[i][0]=(dp[i][0]+dp[j][0])%MOD;
				}
			}
			else if(str[i]==' ')
			{
				for(j=0;j<i;j++)
				{
					if(str[j]=='e'&&dp[j][1])
						dp[i][0]=(dp[i][0]+dp[j][1])%MOD;
					if(str[j]=='o'&&dp[j][1])
						dp[i][1]=(dp[i][1]+dp[j][1])%MOD;
					if(str[j]=='e'&&dp[j][2])
						dp[i][2]=(dp[i][2]+dp[j][2])%MOD;
				}
			}
			else if(str[i]=='d')
			{
				for(j=0;j<i;j++)
				{
					if(str[j]=='o'&&dp[j][2])
						dp[i][0]=(dp[i][0]+dp[j][2])%MOD;
				}
			}
			else if(str[i]=='m')
			{
				for(j=0;j<i;j++)
				{
					if(str[j]=='o'&&dp[j][0])
						dp[i][0]=(dp[i][0]+dp[j][0])%MOD;
					if(str[j]=='a'&&dp[j][0])
					{
						dp[i][1]=(dp[i][1]+dp[j][0])%MOD;
					}
				}
				res+=dp[i][1];
			}
		}
		if(res<10)
			printf("Case #%d: 000%d\n",cas,res);
		else if(res>=10&&res<100)
			printf("Case #%d: 00%d\n",cas,res);
		else if(res>=100&&res<1000)
			printf("Case #%d: 0%d\n",cas,res);
		else
			printf("Case #%d: %d\n",cas,res);
	}
	return 0;
}