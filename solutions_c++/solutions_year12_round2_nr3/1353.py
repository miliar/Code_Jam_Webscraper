#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cmath>

void solveOne();

void main()
{
	int T;
	scanf("%d\n", &T);
	for ( int i = 1; i <= T; ++i )
	{
		printf("Case #%d: ", i);
		solveOne();
	}
}

#include <algorithm>

using namespace std;

bool used[512];
int set1[512], idx1[512];
int set2[512], idx2[512];
int sum1, sum2, N, n[512];

bool select2(int l1, int cnt, int l2, int start)
{
	if ( l2 == cnt ) {
		if ( sum1 == sum2 ) {
			printf("\n%d", set1[0]);
			for ( int i = 1; i < l1; ++i )
				printf(" %d", set1[i]);
			printf("\n%d", set2[0]);
			for ( int i = 1; i < l2; ++i )
				printf(" %d", set2[i]);
			printf("\n");
			return true;
		} else {
			return false;
		}
	}

	for ( int i = start; i < N; ++i )
	{
		if ( used[i] )
			continue;
		idx2[cnt] = i;
		set2[cnt] = n[i];
		sum2 += n[i];
		used[i] = true;

		if ( select2(l1, cnt+1, l2, i+1) )
			return true;

		used[i] = false;
		sum2 -= n[i];
	}
	return false;
}

bool select1(int cnt, int l1, int start)
{
	if ( cnt == l1 ) {
		for ( int l2 = 1; l2 < N/2; ++l2 ) {
			if ( select2(l1, 0, l2, 0) )
				return true;
		}
		return false;
	}

	for ( int i = 0; i < N; ++i )
	{
		if ( used[i] )
			continue;
		set1[cnt] = n[i];
		sum1 += n[i];
		used[i] = true;

		if ( select1(cnt+1, l1, i+1) )
			return true;

		used[i] = false;
		sum1 -= n[i];
	}
	return false;
}

void solveOne()
{
	scanf("%d", &N);
	for ( int i = 0; i < N; ++i )
		scanf(" %d", n+i);
	getchar();

	int l1;
	for ( l1 = 2; l1 < N/2; ++l1 )
	{
		for ( int i = 0; i < N; used[i++] = false );
		sum1 = sum2 = 0;
		if ( select1(0, l1, 0) )
			break;
	}
	if ( l1 == N ) {
		printf("Impossible\n");
	}
}
