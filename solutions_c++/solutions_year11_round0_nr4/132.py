#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
inline int Rint(){ int x; scanf("%d", &x); return x; }
int n;
int main()
{
    int Tcase = Rint();
    while( Tcase -- )
    {
           n = Rint();
           int ans = 0;
           for( int i = 1; i <= n; ++ i )
                if( Rint() != i ) ans ++ ;
           static int o = 1;
           printf("Case #%d: %f\n", o ++, (double)ans);
    }
    return 0;
} 
