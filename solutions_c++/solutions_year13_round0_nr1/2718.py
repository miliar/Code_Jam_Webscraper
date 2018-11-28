#pragma comment(linker, "/STACK:16777216")

#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<ctype.h>
#include<time.h>
#include<iostream>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<string>
#include<utility>
#include<algorithm>
#include<list>
using namespace std;

#define pb push_back
#define MS( a ) memset( a,0,sizeof(a))
#define MSV( a,v ) memset( a,v,sizeof(a))

typedef long long Long;

#define MAX 1007

char B[7][7];
long Cnt[MAX+7];

int main( void )
{
    long i,j,k,u,v,Icase,Kase = 0;;

    //freopen("text1.txt","r",stdin );
    freopen("A.in","r",stdin );
    freopen("A.out","w",stdout );

    scanf("%ld",&Icase );
    while( Icase-- ){
        for( i=1;i<=4;i++ ){
            for( j=1;j<=4;j++ ){
                scanf(" %c",&B[i][j] );
            }
        }
        bool All = true;
        bool WonX = false,WonO = false;
        for( i=1;i<=4;i++ ){
            for( j=1;j<=4;j++ ){
                if( B[i][j] == '.' ){
                    All = false;
                    continue;
                }
                Cnt['T'] = Cnt['X'] = Cnt['O'] = Cnt['.'] = 0;
                for( k=0;k<4;k++ ) Cnt[B[i-k][j+k]]++;
                if( Cnt['T']+Cnt['X'] == 4 ) WonX = true;
                if( Cnt['T']+Cnt['O'] == 4 ) WonO = true;

                Cnt['T'] = Cnt['X'] = Cnt['O'] = Cnt['.'] = 0;
                for( k=0;k<4;k++ ) Cnt[B[i][j+k]]++;
                if( Cnt['T']+Cnt['X'] == 4 ) WonX = true;
                if( Cnt['T']+Cnt['O'] == 4 ) WonO = true;

                Cnt['T'] = Cnt['X'] = Cnt['O'] = Cnt['.'] = 0;
                for( k=0;k<4;k++ ) Cnt[B[i+k][j+k]]++;
                if( Cnt['T']+Cnt['X'] == 4 ) WonX = true;
                if( Cnt['T']+Cnt['O'] == 4 ) WonO = true;

                Cnt['T'] = Cnt['X'] = Cnt['O'] = Cnt['.'] = 0;
                for( k=0;k<4;k++ ) Cnt[B[i+k][j]]++;
                if( Cnt['T']+Cnt['X'] == 4 ) WonX = true;
                if( Cnt['T']+Cnt['O'] == 4 ) WonO = true;
            }
        }
        printf("Case #%ld: ",++Kase );
        if( WonX ) printf("X won\n");
        else if( WonO ) printf("O won\n");
        else if( All ) printf("Draw\n");
        else printf("Game has not completed\n");
    }


    return 0;
}
