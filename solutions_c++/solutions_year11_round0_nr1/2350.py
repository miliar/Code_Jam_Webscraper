#include <stdio.h>
#include <stdlib.h>

int main()
{
	char robot;
	int T, N, i, j, k, O, B, bt;
	long long sumO, sumB;
	bool isCrying = false;

	int dp[4][120] = {0};
	int ptrO, ptrB, ptrC;
	int temp;

	scanf(" %d", &T);

	for(i=0 ; i<T ; i++)
	{
		dp[0][0] = 0; // temp
		dp[1][0] = 0; // ans
		dp[2][0] = 1; // O
		dp[3][0] = 1; // B
		ptrO = 0;
		ptrB = 0;
		ptrC = 1;
		scanf(" %d", &N);
		for(j=0 ; j<N ; j++)
		{
			scanf(" %c", &robot);
			scanf(" %d", &bt);

			if(robot == 'O')
			{
				dp[2][ptrC] = bt;
				dp[3][ptrC] = dp[3][ptrC-1];
				

				temp = abs(dp[2][ptrC] - dp[2][ptrC-1]) + 1;

				if(ptrO + 1 == ptrC )
				{
					dp[0][ptrC] = temp;
					ptrO++;
				}
				else
				{
					for(k = ptrO+1 ; k<ptrC ; k++)
					{
						temp -= dp[0][k];
					}
					dp[0][ptrC] = (temp > 0) ? temp : 1;
					ptrO = ptrC;
				}

				dp[1][ptrC] = dp[1][ptrC-1] + dp[0][ptrC];

				ptrC++;
			}
			else if(robot == 'B')
			{
				dp[2][ptrC] = dp[2][ptrC-1];
				dp[3][ptrC] = bt;
				

				temp = abs(dp[3][ptrC] - dp[3][ptrC-1]) + 1;

				if(ptrB + 1 == ptrC )
				{
					dp[0][ptrC] = temp;
					ptrB++;
				}
				else
				{
					for(k = ptrB+1 ; k<ptrC ; k++)
					{
						temp -= dp[0][k];
					}
					dp[0][ptrC] = (temp > 0) ? temp : 1;
					ptrB = ptrC;
				}

				dp[1][ptrC] = dp[1][ptrC-1] + dp[0][ptrC];

				ptrC++;
			}
		}
		
		printf("Case #%d: %d\n", i+1, dp[1][ptrC-1]);
	}
	return 0;
}