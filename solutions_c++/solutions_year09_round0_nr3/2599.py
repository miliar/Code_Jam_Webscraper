#include<stdio.h>
#include<string.h>
const int MOD=10000;
int sum[19];
int main()
{
	int i,CS=1,T;
	char s[1000];
//	freopen("C-large.in","r",stdin);
//	freopen("out","w",stdout);
	scanf("%d",&T);
	getchar();
	while(T--)
	{
		
		gets(s);
		memset(sum,0,sizeof(sum));
		for(i=0;s[i];i++)
		{
			if(s[i]=='w')
			{
				sum[0]++;
				sum[0]%=MOD;
			}
			else if(s[i]=='e')
			{
				sum[1]+=sum[0];
				sum[1]%=MOD;
				sum[6]+=sum[5];
				sum[6]%=MOD;
				sum[14]+=sum[13];
				sum[14]%=MOD;
			}
			else if(s[i]=='l')
			{
				sum[2]+=sum[1];
				sum[2]%=MOD;
				
			}
			else if(s[i]=='c')
			{
				sum[3]+=sum[2];
				sum[3]%=MOD;
				sum[11]+=sum[10];
				sum[11]%=MOD;
			}
			else if(s[i]=='o')
			{
				sum[4]+=sum[3];
				sum[4]%=MOD;
				sum[9]+=sum[8];
				sum[9]%=MOD;
				sum[12]+=sum[11];
				sum[12]%=MOD;
			}
			else if(s[i]=='m')
			{
				sum[5]+=sum[4];
				sum[5]%=MOD;
				sum[18]+=sum[17];
				sum[18]%=MOD;
			}
			else if(s[i]==' ')
			{
				sum[7]+=sum[6];
				sum[7]%=MOD;
				sum[10]+=sum[9];
				sum[10]%=MOD;
				sum[15]+=sum[14];
				sum[15]%=MOD;
			}
			else if(s[i]=='t')
			{
				sum[8]+=sum[7];
				sum[8]%=MOD;
			}
			else if(s[i]=='d')
			{
				sum[13]+=sum[12];
				sum[13]%=MOD;
			}
			else if(s[i]=='j')
			{
				sum[16]+=sum[15];
				sum[16]%=MOD;
			}
			else if(s[i]=='a')
			{
				sum[17]+=sum[16];
				sum[17]%=MOD;
			}
		}
		printf("Case #%d: %04d\n",CS++,sum[18]);
	}
	return 0;
}

