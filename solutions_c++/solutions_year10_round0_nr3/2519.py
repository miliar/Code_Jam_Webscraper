#include<cstdio>
#include<cstring>
#include<cstdlib>
#define MAXNUM 1010
#define int64 long long
int tail[MAXNUM];
int sum[MAXNUM*2];
int group[MAXNUM];
int rN , kN , nN;

inline int sumcord( int i )
{
    return i < 0 ? 0 : sum[i];
}

void initial()
{
    int i , j , k;
    scanf( "%d%d%d" , &rN , &kN , &nN );
    memset( group , 0 , sizeof( group ) );
    memset( sum , 0 , sizeof( sum ) );
    for( i = 0; i < nN; ++i ){
        scanf( "%d" , &group[i] );
    }
    for( i = 0; i < nN*2; ++i ){
        sum[i] += sumcord(i-1)+group[i%nN];
    }
    for( i = 0; i < nN; ++i ){
        for( j = i; j < i + nN - 1; ++j ){
            if( sum[j+1] - sumcord(i-1) > kN ){
                tail[i] = j;
//                printf( "tail[%d] = %d\n" , i , tail[i] );
                break;
            }
        }
        if( j == i + nN - 1 ){
            tail[i] = j;
        }
    }
}

void findRst()
{
    int i , j;
    int loops , loope;
    int s[MAXNUM] , e[MAXNUM];
    int64 m[MAXNUM];
    int pos[MAXNUM];
    int64 rst;
    memset(s , -1 , sizeof( s ) );
    memset( e , -1 , sizeof( e ) );
    memset( m , 0 , sizeof( m ) );
    memset( pos , -1 , sizeof( pos ) );
    s[0] = 0;
    pos[0] = 0;
    for( i = 0; i < nN; ++i ){
        e[i] = tail[s[i]];
        if( i > 0 ) m[i] = sum[e[i]] - sumcord(s[i]-1) + m[i-1];
        else m[i] = sum[e[i]] - sumcord(s[i]-1);
        s[i+1] = ( e[i] + 1 ) % nN;
        if( pos[s[i+1]] != -1 ){
            loops = pos[s[i+1]];
            loope = i+1;
            break;
        }else{
            pos[s[i+1]] = i+1;
        }
    }
    rst = 0;
    int64 mPerLoop , rLen , loopLen , remain;
//    printf( "%d %d\n" , loops , loope );
    if( loops > 0 ){
        rst += m[loops-1];        
        mPerLoop = m[loope-1] - m[loops-1];
        rLen = rN - (loops);
    }else{
        mPerLoop = m[loope-1];
        rLen = rN;
    }
    loopLen = loope - loops;
    rst += ( rLen / loopLen ) * mPerLoop;
    remain = rLen % loopLen;
    if( loops > 0 ){
        rst += m[loops+remain-1] - m[loops-1];
    }else{
        if( remain > 0 ) rst += m[remain-1];
    }
    printf( "%I64d" , rst );
}

int main()
{
    freopen( "C-small-attempt0.in" , "r" , stdin );
    freopen( "quali_3_small.out" , "w" , stdout );
    int iCase , nCase;
    scanf( "%d" , &nCase );
    for(iCase = 0;iCase < nCase; ++iCase){
        initial();
        printf( "Case #%d: " , iCase + 1 );
        findRst();
        printf( "\n" );
    }
    return 0;
}





