#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <algorithm>
#include <utility>
#include <sstream>
#include <cmath>
#include <complex>

using namespace std;

#define forn(i,n) for(int i=0; i<n; i++)
#define vi vector<int>
#define mii map<int,int>
#define i64 long long int
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define all(x) x.begin(), x.end()
#define vi64 vector<i64,i64>
#define pi acos(-1)

vi prime;
void criba(){
    prime.pb( 2 );
    const int limit = 1000000;
    
    while ( prime[ prime.size()-1 ] < limit ){
	bool isprime = false;
	int sz = prime.size();
	int n = prime[ sz-1 ];
	
	while ( !isprime ){
	    n++;
	    isprime = true;
	    forn(i,sz){
		if ( prime[i]*prime[i] > n ) break;
		if ( n%prime[i] == 0 ){
		    isprime = false;
		    break;
		}
	    }
	}
	
	prime.pb( n );
    }
}

int M[150][150];

void solveTest(){
    int R;
    int x1, x2, y1, y2;
    
    cin >> R;
    
    memset( M, 0, sizeof M );
    
    forn(i,R){
	cin >> x1 >> y1 >> x2 >> y2;
	
	if ( x1 > x2 ){
	  swap( x1, x2 );
	}
	if ( y1 > y2 ){
	  swap( y1, y2 );
	}
	
	while ( x1<=x2 ){
	  int y = y1;
	  while (y <= y2){
	    M[x1][y] = 1;
	    y++;
	  }
	  x1++;
	}
    }
    
    int cont = 0;
    forn(i,101)
      forn(j,101)
	if ( M[i][j] )
	  cont++;
    
    int ans = 0;
    while ( cont  ){
      for (int i=100; i>=0; i--){
	for (int j=100; j>=0; j--)
	  if ( i && j ){
	    if ( M[i][j] ){
	      M[i][j] = ( M[i-1][j]==0 && M[i][j-1]==0 ) ? 0 : 1;
	      if ( !M[i][j] ) cont--;
	    }
	    else{
	      M[i][j] = ( M[i-1][j]==1 && M[i][j-1]==1 ) ? 1 : 0;
	      if ( M[i][j] ) cont++;
	    }
	  }
	  else{
	    if ( M[i][j] ){
	      if ( !i && !j ){
		M[i][j] = 0;
		cont--;
	      }
	      else if ( i ){
		M[i][j] = M[i-1][j];
		if ( !M[i][j] ) cont--;
	      }
	      else if ( j ){
		M[i][j] = M[i][j-1];
		if ( !M[i][j] ) cont--;
	      }
	    }
	  }
      }
      ans++;
    }
    
    cout << ans << endl;
}

int main(){
  int T;
  
  cin >> T;
  
  forn( i, T ){
      cout << "Case #" << i+1 << ": ";
      solveTest();
  }
  
  return 0;
}
