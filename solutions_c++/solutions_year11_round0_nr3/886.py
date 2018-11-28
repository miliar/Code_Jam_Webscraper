#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<fstream>
#include<queue>
#include<algorithm>
#define MAXSIZE 1100
using namespace std;

int number[MAXSIZE] = {0}, n;

int main()
{
	freopen("C-large.in","r", stdin );
	freopen("C-large.out","w", stdout );
	int datacase, t = 0;
	scanf("%d", &datacase );
	while( datacase-- )
	{
		int sum = 0, bit = 0;
		scanf("%d", &n );
		for( int i = 0; i < n; i++ )
		{
			scanf("%d", &number[i] );
			sum += number[i];
			bit = bit ^ number[i];
		}
		sort( number, number + n );
		printf("Case #%d: ", ++t );
		if( bit )
			printf("NO\n");
		else
			printf("%d\n", sum - number[0] );
	}

	return 0;
}
