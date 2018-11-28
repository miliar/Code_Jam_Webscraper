#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
const int NMAX = 1024;
__int64 x[NMAX],y[NMAX];
__int64 res;
int index[NMAX];
int p[NMAX];
int n;
void init()
{
	int i;
	scanf("%d",&n);
	for( i = 0 ; i < n ; i ++ )
	{
		scanf("%I64d", x + i);
		index[i] = i;
	}
	for( i = 0 ; i <n ; i ++ )
	{
		scanf("%I64d",y + i);
	}
	sort(x, x + n);
	reverse(x,x + n);
	sort(y, y + n);
	res = 0 ;
	for( i = 0 ; i < n ; i ++ )
		res += x[i] * y[i] ;
/*	res = 0 ;
	for( i = 0 ; i < n ; i ++)
	{
		res += x[index[i]] * y[i];
		p[i] = x[index[i]];
	}
	while( next_permutation( index ,index+n))
	{
		int tmp = 0 ;
		for( i = 0 ; i < n ; i ++)
		{
	//		printf("%d ", index[i]);
			tmp += x[index[i]] * y[i];
		}
//		printf("\n");
		if( res > tmp )
		{
			res = tmp ;
			for( i = 0 ; i < n ; i ++)
				p[i] = x[index[i]];
		}
	}
	for( i = 0 ; i < n ; i ++ )
	{
		printf("%d %d\n",p[i],y[i]);
	}
	*/
}
int main()
{
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int T;
	scanf("%d",&T);
	int cnt = 0 ;
	//printf("%I64d\n",0xffffffff);
	while ( T-- )
	{
		cnt ++ ;
		init();
		printf("Case #%d: %I64d\n",cnt,res);
	}
	return 0;
}








































