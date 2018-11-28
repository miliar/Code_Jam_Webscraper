#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int BT[32];
int TEMP[32];
int CA[16];

int rec(int n, int size)
{
//	printf("REC : %d %d\n", n, size);
	if( n <= (size-1)/2 )
	{
		if( TEMP[n]==1 )
		{
			if( rec(2*n, size)==1 && rec(2*n+1, size)==1 )
				return 1;
			else
				return 0;
		}
		else
		{
			if( rec(2*n, size)==0 && rec(2*n+1, size)==0 )
				return 0;
			else
				return 1;
		}
	}
	else
	{
		return TEMP[n];
	}
	
}

int main()
{
	int i, j, k;
	int n, N;
	int M, V;
	int min, cnt;
	bool find;

	scanf("%d", &N);
	for(n=1;n<=N;n++)
	{
		scanf("%d %d", &M, &V);
		
		for(i=1;i<=M;i++)
		{
			scanf("%d", &BT[i]);
			if( i <= (M-1)/2)
				scanf("%d", &CA[i]);
		}

		min = 1000000000;
		find = false;
		for(i=0;i<1<<((M-1)/2);i++)
		{
			cnt = 0;
			for(j=1;j<=M;j++)
				TEMP[j] = BT[j];
			for(j=0;j<=(M-1)/2;j++)
			{
				if( ((1<<j) & i) == (1<<j) )
				{
					if( CA[j+1]==1 )
					{
						cnt++;
						TEMP[j+1] = TEMP[j+1]==1 ? 0 : 1;
					}
				}
			}
			if( rec(1, M)==V )
			{
				find = true;
				if( min > cnt )
					min = cnt;
			}
		}
		if( find )
			printf("Case #%d: %d\n", n, min);
		else
			printf("Case #%d: IMPOSSIBLE\n", n);
	}
	return 0;
}
