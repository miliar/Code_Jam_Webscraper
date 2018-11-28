#include <cstdio>
#include <cstring>

bool check( int a, int b )
{
	bool win = 1;
	while ( a && b )
	{
		if( a > b ) {
			int tmp = a; a = b; b = tmp;
		}
		int d = b / a;
		if( d > 1 ) return win ;
		b = b % a;
		
		win = !win;
	}
}

int main ()
{
	int cases,index; scanf("%d",&cases);
	for(index = 0; index < cases; index ++ )
	{
		int a1, a2, b1, b2;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		int ans = 0;
		for(int i = a1; i <= a2; i ++ )
		for(int j = b1; j <= b2; j ++ )
		{
			if( check( i, j ) ) ans ++ ;
		}
		printf("Case #%d: %d\n", index+1, ans);
	}
}
