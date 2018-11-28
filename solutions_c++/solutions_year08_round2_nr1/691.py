#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
const int NMAX = 1024;
__int64 res;
struct Node
{
	unsigned __int64 x,y;
}Tree[NMAX];
unsigned __int64 num[3][3];
bool judge( Node a, Node b, Node c)
{
	int tmp = (c.x - a.x )*(b.y - a.y ) - (b.x - a.x) * (c.y -a.y);
	return tmp == 0 ;
}
void init()
{
	int n, A,B,C,D,x0,y0,M;
	scanf("%d %d %d %d %d %d %d %d",&n,&A,&B,&C,&D,&x0,&y0,&M);
	int i;
	Tree[ 0 ].x = x0  ;
	Tree[ 0 ].y = y0  ;
//	printf("%d %d\n",Tree[0].x,Tree[0].y);
	for( i  = 1 ;i  < n ; i ++ )
	{
		Tree[ i ].x = ( (__int64)A * Tree[i-1].x % M + B) % M ;
		Tree[ i ].y = ( (__int64)C * Tree[i-1].y % M + D) % M ;
		//printf("%d %d\n",Tree[i].x,Tree[i].y);
	}
	res = 0;
	int j,k;
	/*	memset( num , 0, sizeof( num )) ;
	for( i = 0 ; i < n ; i ++ )
	{
	int xx = Tree[i].x % 3;
	int yy = Tree[i].y % 3;
	//	printf("%I64d %I64d\n",Tree[i].x,Tree[i].y);
	num[xx][yy] ++ ;
	}
	
	  for( i = 0 ; i < 9 ; i ++ )
	  {
	  for( j = i + 1 ; j < 9 ; j ++ )
	  {
	  for( k = j + 1 ; k < 9;  k ++ )
	  {
	  int xx = (i/3 + j/3 + k/3)%3;
	  int yy = (i%3 + j%3 + k%3)%3;
	  if( !xx && !yy )
	  {
	  res += (num[i/3][i%3] * num[j/3][j%3] * num[k/3][k%3]);
	  }
	  }
	  }
	  }
	*/
	for( i = 0 ; i < n ; i ++ )
	{
		Tree[i].x %= 3;
		Tree[i].y %= 3;
	}
	for( i = 0 ; i < n ; i ++ )
	{
		for( j = i + 1 ; j < n ; j ++ )
		{
			for( k = j + 1 ; k < n ; k ++  )
			{
				int tmpx,tmpy;
				tmpx = Tree[i].x + Tree[j].x + Tree[k].x;
				tmpy = Tree[i].y + Tree[j].y + Tree[k].y;
	//			printf("%d %d %d\n",Tree[i].x,Tree[j].x,Tree[k].x);
	//			printf("%d %d %d\n",Tree[i].y,Tree[j].y,Tree[k].y);
	//			puts("");
				//	judge( Tree[i],Tree[j],Tree[k] );
				if( tmpx % 3 == 0 && tmpy % 3 == 0  )
					res ++ ;
			}
		}
	}
	
	
	
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
	while ( T-- )
	{
		cnt ++ ;
		init();
		printf("Case #%d: %I64d\n",cnt,res);
	}
	return 0;
}