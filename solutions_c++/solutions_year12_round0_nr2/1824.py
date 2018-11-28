#include<stdio.h>


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("pb.txt","w",stdout);
    int T,N,S,P,n,cnt,s,tmp;
    scanf(" %d",&T);
    for( int x = 1; x <= T; x++ ){
        scanf(" %d %d %d",&N,&S,&P);
        cnt = s = 0;
        for( int i = 0; i < N; i++ ){
            scanf(" %d",&n);
            tmp = n;
            if( n % 3 == 0 )    n = n / 3;
            else                n = ( n / 3 ) + 1;
            if( n >= P ){
                cnt++;
                continue;
            }
            n = tmp;
            if( n < 2 || s >= S ) continue;
            n -= 2;
            n = ( n / 3 ) + 2;
            if( n >= P ){
                cnt++;
                s++;
            }
        }
        printf("Case #%d: %d\n",x,cnt);
    }
    return 0;
} 
