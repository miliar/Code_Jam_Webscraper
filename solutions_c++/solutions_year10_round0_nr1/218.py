
#include<cstdlib>
#include<cstring>
#include<cstdio>

int T , n , k , mask;

int main()
{
//	freopen("input.txt" , "r" , stdin);
//	freopen("output.txt" , "w" , stdout);
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);
	int cas = 0;
	for ( scanf("%d" , &T) ; T-- ; )
	{
		scanf("%d%d" , &n , &k);
		printf("Case #%d: " , ++cas);
		mask = 1 << n;
		puts( mask-1==k % mask ? "ON" : "OFF" );
	}
	return 0;
}

