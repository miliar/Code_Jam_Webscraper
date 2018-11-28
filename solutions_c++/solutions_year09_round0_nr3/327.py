#include<iostream>
#include<string.h>
using namespace std;
#define N 505
int dp[N][25];
char s[N];
int main()
{
	int i,j,t,count=0;
	char ch;
	FILE *in,*out;
	in=fopen("inc2.in","r");
	out=fopen("outc2.txt","w");
	fscanf(in,"%d",&t);
	fscanf(in,"%c",&ch);
	while(t>0)
	{
		t--;
		fgets(s,505,in);
		count++;
		int len=strlen(s);
		memset(dp,0,sizeof(dp));
		for(i=0;i<len;i++)
			dp[i][0]=1;
		if(s[0]=='w')
			dp[0][1]=1;
		for(i=1;i<len;i++)
		{
			for(j=0;j<25;j++)
				dp[i][j]=dp[i-1][j];
			if(s[i]=='w')
				dp[i][1]+=dp[i-1][0];
			else if(s[i]=='e')
			{
				dp[i][2]+=dp[i-1][1];
				dp[i][7]+=dp[i-1][6];
				dp[i][15]+=dp[i-1][14];
			}
			else if(s[i]=='l')
				dp[i][3]+=dp[i-1][2];
			else if(s[i]=='c')
			{
				dp[i][4]+=dp[i-1][3];
				dp[i][12]+=dp[i-1][11];
			}
			else if(s[i]=='o')
			{
				dp[i][5]+=dp[i-1][4];
				dp[i][10]+=dp[i-1][9];
				dp[i][13]+=dp[i-1][12];
			}
			else if(s[i]=='m')
			{
				dp[i][6]+=dp[i-1][5];
				dp[i][19]+=dp[i-1][18];
			}
			else if(s[i]==' ')
			{
				dp[i][8]+=dp[i-1][7];
				dp[i][11]+=dp[i-1][10];
				dp[i][16]+=dp[i-1][15];
			}
			else if(s[i]=='t')
				dp[i][9]+=dp[i-1][8];
			else if(s[i]=='j')
				dp[i][17]+=dp[i-1][16];
			else if(s[i]=='a')
				dp[i][18]+=dp[i-1][17];
			else if(s[i]=='d')
				dp[i][14]+=dp[i-1][13];
			for(j=0;j<25;j++)
				dp[i][j]%=10000;
		}
		dp[len-1][19]%=10000;
		fprintf(out,"Case #%d: %04d\n",count,dp[len-1][19]);
	}
	return 0;
}