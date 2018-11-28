#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#include<cstdio>
#include<list>
#include<cctype>
#include<complex>
#include<sstream>
#include<numeric>

using namespace std;

typedef long long i64;
typedef vector< int > vi;
typedef vector< vi > vii;
typedef map< int , string > mis;
typedef map< string, int > msi;
typedef vector< string > vs;
typedef pair<int,int> pii;
typedef map<int,int> mii;

#define mem(a,i) memset(a,i,sizeof(a))
#define pb push_back
#define Inf ( 1 << 30 )
#define MAX 10005
#define S 10005

int test_case;
int N,L,H;
int note[ MAX ];
bool taken[ S ];

i64 gcd( int a, int b ){
    if( b == 0 ) return a;
    else return gcd( b, a % b );
}

i64 ok(){
    if( !taken[ 1 ] && L == 1 ) return 1;
    i64 g = note[ 0 ];
    i64 s = note[ 0 ];
    for( int i = 1; i < N; i ++ ){
        g = gcd( g, note[ i ] );
        s *= note[ i ];
    }

    if( !taken[ g ] && g >= L && g <= H ) return g;
    i64 l = s / g;
    bool flag = true;
    for( int k = 0; k < N; k ++ ){
        if( note[ k ] == l ) {
            flag = false;
            break;
        }
    }

    if( flag && l >= L && l <= H ) return l;

    return -1;


}

bool can( int n ){
    for( int i = 0; i < N; i ++ ){
        if( note[ i ] % n == 0 ) continue;
        if( n % note[ i ] == 0 ) continue;
        return false;
    }

    return true;
}



int main(){
    freopen("C-small-attempt5.in", "r", stdin );
    freopen("outC.txt", "w", stdout);
  //freopen("a.txt", "r", stdin);
    int i;
    scanf("%d", &test_case);
    for( int caseId = 1; caseId <= test_case; caseId ++ ){
        scanf("%d %d %d", &N, &L, &H);
        if( L > H ) swap( L, H );
        memset( taken, false, sizeof( taken ) );
        for( int i = 0; i < N; i ++ ){
            scanf("%d", &note[ i ] );
            taken[ note[ i ] ] = true;
        }


        int ans = -1;
        for( int k = L; k <= H; k ++ ){
            if( can( k ) ){
                ans = k;
                break;
            }
        }

        if( ans == -1 ) printf("Case #%d: NO\n", caseId );
        else printf("Case #%d: %d\n", caseId, ans );
    }
	return 0;
}
