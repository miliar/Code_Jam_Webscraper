#include<cstdio>
#include<cstring>
using namespace std;

const char* gcj = "welcome to code jam";
const int gcjlen = 19;
const int Max = 500;
char buf[Max+1];
int dp[gcjlen][Max];
int main()
{
	int n,cases=0;
	scanf("%d",&n);
	while(n-- > 0)
	{
		scanf("\n%[^\n]",buf);
		int l = strlen(buf);
		for(int j=0;j<l;j++)
			dp[0][j] = buf[j] == gcj[0] ? 1 : 0;
		for(int i=1;i<gcjlen;i++)
			for(int j=i;j<l;j++)
			{
				dp[i][j] = 0;
				if(gcj[i] == buf[j])
					for(int k=0;k<j;k++)
						dp[i][j] += dp[i-1][k];
				dp[i][j] %= 10000;
			}
		int sum = 0;
		for(int j=0;j<l;j++)
			sum += dp[gcjlen-1][j];
		sum %= 10000;
		printf("Case #%d: %04d\n",++cases,sum);
	}
	return 0;
}
