#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h> 

#ifdef USE_TESTING_SYSTEM
#include "TestHelpers.h"
PROBLEM_BEGIN(GCJ9-R2C,"Code Jam 2009-R2 C")
#endif

template <typename T> T min(T a, T b) { return a < b ? a : b; }
template <typename T> T abs(T a) { return a > 0 ? a : -a; }

const int MAX_N = 100;
const int MAX_LEN = 25;

int N, K;
int P[MAX_N][MAX_LEN];
bool M[MAX_N][MAX_N];
bool Mask[MAX_N];
int temp[MAX_N];
bool CanPlaceTogether(int i, int j)
{
	if( P[i][0] == P[j][0]) return false;
	bool low = P[i][0] < P[j][0];
	for(int l=0; l < K; l++)
	{
		if( P[i][l] == P[j][l] ) return false;
		if( (P[i][l] < P[j][l] ) != low ) return false;
	}
	return true;
}

void Paint(int i)
{
	Mask[i] = true;
	temp[0] = i;
	int nT = 1;
	while(true)
	{
		int m = -1;
		int mm = -1;
		for(int i=0; i < N; i++)
		{
			if( Mask[i] ) continue;
			bool bCan = true;
			for(int k=0; k < nT; k++)
			{
				if( !M[temp[k]][i] )
				{
					bCan = false;
					break;
				}
			}
			if( bCan )
			{
				int v= 0;
				for(int j=0; j < N; j++)
				{
					if( Mask[j] ) continue;
					if( !M[i][j] )
						v += 1;
				}
				if( v > mm )
				{
					mm = v;
					m = i;
				}
			}
		}
		if( m != -1 )
		{
			Mask[m] = true;
			temp[nT++] = m;
		}
		else
			break;
	}

}

#ifdef USE_TESTING_SYSTEM
TESTING_FUNCTION()
#else
int main()
#endif
{
	int TestCases;
	scanf("%d", &TestCases);
	for(int test=1; test<=TestCases; test++)
	{
		scanf("%d %d", &N, &K);
		for(int i=0; i < N; i++)
		{
			for(int l=0; l < K; l++)
				scanf("%d", &P[i][l]);
		}
		for(int i=0; i < N; i++)
		{
			for(int j=0; j < N; j++)
				M[i][j] = CanPlaceTogether(i, j);
		}
		for(int i=0; i < N; i++) Mask[i] = false;
		int res = 0;
		while(true)
		{
			int m = -1;
			int mm = -1;
			for(int i=0; i < N; i++) 
			{
				if( Mask[i] ) continue;
				int v = 0;
				for(int j=0; j < N; j++)
				{
					if( Mask[j] ) continue;
					if( !M[i][j] )
						v += 1;
				}
				if( v > mm )
				{
					mm = v;
					m = i;
				}
			}
			if( m != -1 )
			{
				res += 1;
				Paint(m);
			}
			else
				break;
		}
		printf("Case #%d: %d\n", test, res);
	}
	return 0;
}
#ifdef USE_TESTING_SYSTEM
PROBLEM_END()
#endif