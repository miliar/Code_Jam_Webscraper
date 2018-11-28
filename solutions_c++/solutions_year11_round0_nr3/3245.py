#include<cstdio>
#include<cmath>
#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
#define MAX 2000
using namespace std;
int main()
{
  int t;
  scanf("%d", &t);
  for( int ix = 1; ix <= t; ix++ )
  {
    int n;
	scanf("%d", &n);
	long piles[MAX];
	
	for( int i = 1; i <= n; i++ )
	  scanf("%ld", &piles[i]);
	
	vector< int >zx;

	long xorv = 0;
	long sum[MAX];
	memset(sum, 0, sizeof( sum ));
	for( int i = 1; i <= n; i++ )
	{
	  xorv ^= piles[i];
	  sum[i] = sum[i-1] + piles[i];
	  if( xorv == 0 )zx.push_back( i );
	}
	long maxi = -1;
	/*for( int i = 0; i < zx.size(); i++ )
	{
	  for( int j = 1; j < zx[i]; j++ )
	  {
		long mx = max( sum[j], sum[zx[i]] - sum[j] );
		if( mx > maxi )maxi = mx;
	  }
	}*/
	printf("Case #%d: ", ix);
	if( xorv != 0)
     printf("NO\n");
	else
	{
	  //sort(piles + 1, piles + n );
	  long mini = -1;
	  for( int i = 1; i <= n; i++ )if( mini == -1 || piles[i] < mini) mini = piles[i];
	  printf("%ld\n", sum[n] - mini );
	}
  }
  return 0;
}