#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <cstring>

#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <utility>
#include <queue>

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

int main(){
	ios_base::sync_with_stdio(false);
	
	int test, t=1, r, c, i, j;
	char pic[100][100];
	bool poss;
	
	cin >> test;
	while (test--){
		cin >> r >> c;
		
		poss = true; 
		fi(r){
			fj(c){
				cin >> pic[i][j];
			}
		}
		
		fi(r){
			fj(c){
				if (pic[i][j] == '#'){
					if ( ( (j+1) >= c )
						|| ( (i+1) >= r )
						|| ( pic[i][j+1] != '#')
						|| ( pic[i+1][j] != '#')
						|| ( pic[i+1][j+1] != '#') ){
						poss = false;
						break;
					}
					else{
						pic[i][j] = pic[i+1][j+1] = '/';
						pic[i][j+1] = pic[i+1][j] = '\\';
					}
				}
			}
		}
		
		cout << "Case #" << t++ << ":\n";
		if (poss){
			fi(r){
				fj(c){
					cout << pic[i][j];
				}
				cout << "\n";
			}
		}
		else cout << "Impossible\n";
		/*
		fi(r){
				fj(c){
					cout << pic[i][j];
				}
				cout << "\n";
			}
		}
		*/
	}
	
	return 0;
}