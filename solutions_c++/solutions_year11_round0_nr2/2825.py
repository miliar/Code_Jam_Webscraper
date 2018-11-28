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
#define MAX 150

int N,C,D;
char com[ MAX ][ MAX ];
bool opp[ MAX ][ MAX ];
bool c[ MAX ][ MAX ];
int test_case;
vector< char > ans;
string inp;

void cmp(){
    int n = ans.size();
    if( n <= 1 ) return ;
    char a = ans[ n - 1 ];
    char b = ans[ n - 2 ];
    if( c[ a ][ b ] ) {
        char r = com[ a ][ b ] ;
        ans.pop_back();
        ans.pop_back();
        ans.pb( r );
    }

}

void des( ){
    int n = ans.size();
    if( n <= 1 ) return ;
    char a = ans[ n - 1 ];
    for( int i = 0; i < n - 1; i ++ ){
        if( opp[ ans[ i ] ][ a ] ){
            ans.clear();
            break;
        }
    }


}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int i,j;
    scanf("%d", &test_case);
    for( int caseId = 1; caseId <= test_case; caseId ++ ){
        ans.clear();
        scanf("%d", &C);
        memset( c, false, sizeof( c ) );
        memset( opp, false, sizeof( opp ) ) ;
        for( i = 0; i < C; i ++ ){
            cin >> inp;
            c[ inp[ 0 ] ][ inp[ 1 ] ] = c[ inp[ 1 ] ][ inp[ 0 ] ] = true;
            com[ inp[ 0 ] ][ inp[ 1 ] ] = com[ inp[ 1 ] ][ inp[ 0 ] ] = inp[ 2 ];
        }

        scanf("%d", &D);
        for( i = 0; i < D; i ++ ){
            cin >> inp;
            opp[ inp[ 0 ] ][ inp[ 1 ] ] = opp[ inp[ 1 ] ][ inp[ 0 ] ] = true;
        }

        scanf("%d", &N);
        cin >> inp;
        for( i = 0; i < N; i ++ ){
            ans.pb( inp[ i ] );
            cmp();
            des();
        }


        printf("Case #%d: [", caseId );
        for( i = 0; i < ans.size(); i ++ ){
            if( i ) printf(", ");
            printf("%c", ans[ i ]);

        }

        printf("]\n");
    }

	return 0;
}
