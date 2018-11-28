#include <cstdio>
using namespace std;
int main()
{
	int iTests;
	scanf("%d", &iTests);
	for(int iTestCnt=1; iTestCnt<=iTests; iTestCnt++)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		const int a_n = (1<<N)-1;
		if( K < a_n )
			printf("Case #%d: OFF\n", iTestCnt);
		else
		{
			const int w = (K-a_n)/(a_n+1)+1;
			if( K == w*a_n+w-1 )
				printf("Case #%d: ON\n", iTestCnt);
			else
				printf("Case #%d: OFF\n", iTestCnt);
		}
	}
	return 0;
} 
