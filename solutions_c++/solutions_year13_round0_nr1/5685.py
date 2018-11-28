#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <cctype>
#include <queue>
#include <numeric>
#include <cmath>
#define repn(a,x,y) for (int a=x; a<y; a++)
#define rep(a, n ) repn( a , 0 , n ) 
#define fd(a,x,y) for (int a=x; a>=y; a--)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define vint vector<int>
#define pb push_back
#define FOR(it,A) for (typeof A.begin() it=A.begin(); it!=A.end(); it++)
#define ones(x) __builtin_popcountll(x)
#define clr(A,x) memset (A, x, sizeof A)
#define eps (1e-9)
#define cua(x) (x)*(x)
#define fst first
#define snd second
#define pii pair<int,int>
#define debug(x) cout << #x << " = " << x <<endl
typedef long long ll;
using namespace std;

string a[4],b[4];


bool win( char ant ){
	bool dot = false;
    for( int i = 0; i < 4; i++) {
        if ( a[i][0] == '.' ) break;
        bool c = false;
        for( int j = 0; j < 4; j++){
			if ( a[i][j] == 'T') continue;
            if ( a[i][j] !=  ant ) c = true;
        }
        if ( !c ) return true;
    }
    for( int i = 0; i < 4; i++) {
        if ( a[0][i] == '.' ) break;
        bool c = false;
        for( int j = 0; j < 4; j++){
			if ( a[i][j] == 'T') continue;
            if ( a[j][i] !=  ant ) c = true;
        }
        if ( !c ) return true;
    }
	bool c= false;
	for( int i = 0; i < 4; i++){
		for( int j = 0; j < 4; j++){
			if ( i == j ){
				if ( a[i][j] == 'T') continue;
				if ( a[i][j] != ant ) c = true;
			}		
		}
	}
	if (!c) return true;
	c = false;
	for( int i = 0; i < 4; i++){
		for( int j = 3; j >= 0; j--){
			if ( i + j == 3){
				if ( a[i][j] == 'T') continue;
				if ( a[i][j] != ant ) c = true;
			}		
		}
	}

	if (!c) return true;
    return false;

}


int main(){
    int R;
    cin >> R;
	for( int r = 1; r <= R;r++){
        for( int i = 0; i < 4; i++) cin >> a[i] ;

        vector<pair<int,int> > x, o;    

        for( int i = 0; i < 4; i++){
            for( int j = 0; j < 4; j++){
                if ( a[i][j] == 'X' ) x.push_back( make_pair( i , j ) );
                else if ( a[i][j] != '.') o.push_back( make_pair( i , j ) );
            }
        }

        bool xx = win('X');
        bool oo = win('O');
		printf("Case #%d: ",r);
		if ( xx ) puts("X won");
		else if ( oo ) puts("O won");
		else if ( !xx and !oo and o.size()+x.size() == 16) puts("Draw");
		else puts("Game has not completed");
    }
    return 0;

}
