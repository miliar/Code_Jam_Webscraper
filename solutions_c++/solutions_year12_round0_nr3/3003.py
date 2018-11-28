#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
using namespace std;

int i,j,k;
int T;
int ans;
int A, B;
int nd;
int tmp;
int z[10] = {0,1,10,100,1000,10000,100000,1000000,10000000,100000000};
bool hascount[5000000];

int res(int X)
{
	int m, n;
	int rs = 0;
	int y, x;
	
	x = X;
	memset(hascount,false,sizeof(hascount));

	for(m = 1; m < nd; m ++)
	{
		n = x % 10;
		if(n == 0)
		{	
			y = x / 10;
		}
		else
		{
			y = x / 10 + n * z[nd];
		}

		if( y > X && y <= B && !hascount[y])
		{
			rs ++;
			hascount[y] = true;
			//printf("%d %d\n",X,y);
		}
		x = y;
	}
	return rs;
}

int main( )
{
	freopen( "C-small.in", "r", stdin );
	freopen( "C-small.out", "w", stdout );


	scanf("%d",&T);

	for(i=1;i<=T;i++)
	{
		ans = 0;

		scanf("%d%d",&A,&B);
		
		tmp = A;
		nd = 0;
		while(tmp)
		{
			nd ++;
			tmp = tmp / 10;
		}

		for(j=A;j<=B;j++)
			ans += res(j);
		
		printf("Case #%d: %d\n",i,ans);
		
	}

	return 0;
}
