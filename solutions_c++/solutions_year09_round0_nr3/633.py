#include<cstring>
#include<cstdio>



char buf[1024];
char now[1024];

int dp[24][1024];

char wel[] = "welcome to code jam"; //19

int main()
{
	int cases , Case = 0;

	scanf("%d" , &cases);
	gets(buf);

	int idx;
	int len; 
	int ans = 0;
	int i , j;


	while(cases-- )
	{
		gets(buf);
		memset( dp , 0 , sizeof(dp));
		len = strlen( buf);
		
		for(i=0;i<len;i++)
		{
			if( buf[i] == 'w' )
			{
				dp[0][i] = 1;
			}
			if(i) dp[0][i] += dp[0][i-1];
		}

		
 		for(j = 1;j<19;j++)
		{
			for(i=j;i<len;i++)
			{

				dp[j][i] = dp[j][i-1];

				if( buf[i] == wel[j] ) 
				{
					dp[j][i] += dp[j-1][i-1];
					
				}
				dp[j][i] %= 10000;
			}
		}


		printf("Case #%d: %04d\n" , ++Case , dp[18][len-1]% 10000 );

	}



	return 0;
}