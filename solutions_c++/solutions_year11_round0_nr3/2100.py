#include <stdio.h>

int main()	{

    freopen("C:\\Users\\MadFroG\\Downloads\\C-large.in" , "r" , stdin);
    freopen("C:\\Users\\MadFroG\\Downloads\\C-large.out" , "w" , stdout);
    int T;
    int n , v;
    int minv;

    scanf("%d" , &T);
    for ( int cas = 1;cas <= T;cas ++ )	{
	scanf("%d" , &n);

	int res = 0;
	int sum = 0;
	minv = -1;
	for ( int i = 0;i < n;i ++ )	{
	    scanf("%d" , &v);
	    res ^= v;
	    sum += v;
	    if ( minv==-1 || v < minv) minv = v;
	}
	printf("Case #%d: " , cas);
	if ( res != 0 )	{
	    puts("NO");
	}	else	{
	    printf("%d\n" , sum-minv);
	}
    }
    return 0;
}
