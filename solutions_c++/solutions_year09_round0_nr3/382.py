#include "iostream"
#include "string"
#include "algorithm"
#include "vector"
using namespace std;

#define min(a, b) ((a)<(b)?(a):(b))
#define min3(a, b, c) ((a)<(b)?((a)<(c)?(a):(c)):((b)<(c)?(b):(c)))
#define max(a, b) ((a)>(b)?(a):(b))
#define max3(a, b, c) ((a)>(b)?((a)>(c)?(a):(c)):((b)>(c)?(b):(c)))


int dp[510][30];
char ch[510];
int len;

void wuming()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

int main()
{
	wuming();

	int i, j, k;
	char wel[30]="welcome to code jam";
	int lenWel=strlen(wel);

	int T;
	scanf("%d\n", &T);
	int test=0;
	while(T--)
	{
		gets(ch);
		len=strlen(ch);

		
		memset(dp, 0, sizeof(dp));
		if(ch[0]=='w')
			dp[0][1]=1;
		dp[0][0]=1;

		for(i=1; i<len; ++i)
		{
			dp[i][0]=1;
			for(j=1; j<=lenWel; ++j)
			{
				dp[i][j]=dp[i-1][j];
				if(ch[i]==wel[j-1])
				{
					dp[i][j] += dp[i-1][j-1];
					dp[i][j]%=10000;
				}
			}
		}
		printf("Case #%d: %04d\n", ++test, dp[len-1][lenWel]);
		
	}

	return 0;
}