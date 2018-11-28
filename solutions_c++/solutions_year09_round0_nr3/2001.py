#include <cstdio>
#include <cstring>
using namespace std;
const int NMAX = 505;
const char *phrase = "welcome to code jam";
char str[NMAX];
int dp[20][NMAX];

int main()
{
	const int MODD = 10000;
	freopen("input.txt", "rt", stdin);
	freopen("output1.txt", "wt", stdout);

	int numTests;
	//cin >> numTests;
	
	scanf("%d", &numTests);

	for(int it=0; it<numTests; it++)
	{
		//cin.getline(str,NMAX);
		gets(str);
		if( 0==str[0] ) 
		{
			it--;
			continue;
		}

		int len = strlen(str);
		for(int d=0; d<20; d++)
		{
			for(int i=0;i<NMAX;i++)
			{
				dp[d][i] = 0;
			}
		}

		dp[0][0] = (str[0]==phrase[0]);
		for(int i=1;i<NMAX;i++)
		{
			dp[0][i] = dp[0][i-1];
			if( str[i]==phrase[0] )
				dp[0][i]++;
			dp[0][i] %= MODD;
		}

		for(int d=1; d<20; d++)
		{
			dp[d][0] = 0;
			for(int i=1;i<NMAX;i++)
			{
				dp[d][i] = dp[d][i-1];
				if( str[i]==phrase[d] )
				{
					dp[d][i] += dp[d-1][i-1];
				}
				dp[d][i] %= MODD;
			}
		}

		//cout << dp[19][len] << endl;
		printf("Case #%d: %04d\n", it+1, dp[19][len]);

	}
	return 0;
}