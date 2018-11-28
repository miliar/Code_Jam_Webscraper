#define _CRT_SECURE_NO_DEPRECATE

#include <sstream>
#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int n, m;

int main( )
{
	int i, j, k, t, tt;
	//localhost/Users/Chen/Downloads/A-small-practice(1).in
	freopen( "/Users/Chen/Downloads/A-large(1).in", "r", stdin );

//	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	scanf( "%d\n", &tt );
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d:", t );

        int r = ni();
        int c = ni();
		char sq[r][c];
		fi(r){
			vector< char > v;
			string s = ns();
			fj(c){
				sq[i][j] = s[j];
			}
		}

//		cout<< "\n";
//		fi(r){
//			fj(c){
//				cout<< sq[i][j];
//			}
//			cout<< "\n";
//		}
		
		fi(r){
			fj(c){
				if(sq[i][j] == '#'){
					if(i+1 < r && j+1 < c &&
						   sq[i][j+1] == '#' &&
						   sq[i+1][j] == '#' &&
						   sq[i+1][j+1] == '#')
					{
						sq[i][j] = '/';
						sq[i][j+1] = '\\';
						sq[i+1][j] = '\\';
						sq[i+1][j+1] = '/';
					}
				}
			}
		}

		stringstream ss;
		fi(r){
			if(i>0)
						ss<< "\n";
			fj(c){
				ss<< sq[i][j];
			}
		}
		
//		cout<< "===\n";
//		cout<< ss.str();
		

		bool imp = false;
		fi(r){
			fj(c){
				if(sq[i][j] == '#'){
					imp = true;
					break;
				}
			}
			if(imp){
				break;
			}
		}
		
		if(!imp){
			printf("\n%s\n", ss.str().c_str());
		}else{
			printf("\nImpossible\n");
		}
	}
	return 0;
}
