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
#define MAX 55


int test_case;
int R,C;
vector< string > grid;
bool taken[ MAX ][ MAX ];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &test_case);
    for( int caseId = 1; caseId <= test_case; caseId ++ ){
        scanf("%d %d", &R, &C);
        grid.clear();
        memset( taken, false, sizeof( taken ) );
        string s;
        for( int i = 0; i < R; i ++ ) {
            cin >> s;
            grid.pb( s );

        }

        int j,k;

        for( j = 0; j < R; j ++ ){
            for( k = 0; k < C; k ++ ){
                 if( grid[ j ][ k ] == '#'  && !taken[ j ][ k ] ) {
                     if( j + 1 < R && k + 1 < C && grid[ j ][ k ] == '#' && grid[ j + 1 ][ k ] == '#' && grid[ j ][ k + 1 ] == '#' && grid[ j + 1 ][ k + 1 ] == '#' && !taken[ j ][ k ] && !taken[ j ][ k + 1 ] && !taken[ j + 1 ][ k ] && !taken[ j + 1 ][ k + 1 ] ){
                        grid[ j ][ k ] = '/';
                        grid[ j ][ k + 1] = '\\';
                        grid[ j + 1 ][ k ] = '\\';
                        grid[ j + 1 ][ k + 1 ] = '/';
                        taken[ j ][ k ] = true;
                        taken[ j ][ k + 1 ] = true;
                        taken[ j + 1][ k ] = true;
                        taken[ j + 1 ][ k + 1] = true;


                    }
                }
            }
        }

        bool flag = true;
        for( j = 0; j < R; j ++ ) {
            for( k = 0; k < C; k ++ ){
                    if( grid[ j ][ k ] == '#'){ flag = false;
                  //  printf("%d %d\t", j,k);
                }

            }
        }

        printf("Case #%d:\n", caseId);
        if( flag ) {
            for( j = 0; j < R; j ++ ){
                for( k = 0; k < C; k ++ ){
                    printf("%c", grid[ j ][ k ] );
                }

                printf("\n");
            }
        }

        else printf("Impossible\n");




    }
	return 0;
}
