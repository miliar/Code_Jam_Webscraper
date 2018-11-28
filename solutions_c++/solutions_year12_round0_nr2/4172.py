

/*
 * Author: blackBird
 * Email: saketbharamberocks@gmail.com
 */
#include <cstdio>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <cmath>
#include <utility>
#include <climits>

using namespace std ;

typedef long long ll ;
typedef pair<int,int> ii ;

#define FOR(i,a,b) for(int i=(a);i<(b);i++) 
#define FOR0(i,a) for(int i=0;i<(a);i++) 
#define FOR1(i,a) for(int i=1;i<(a);i++)
#define REP(i,a,b,c) for(int i=(a);i<(b);i+=(c)) 
#define TRAVERSE(it,s) for(typeof(s.begin()) it=s.begin();it!=s.end();++it)
#define ENDL putchar(10)
#define PB push_back
#define MP make_pair
#define SZ size

#define FILL(a,x) memset(a,x,sizeof a)
#define ALL(c) (c).begin(),(c).end()
#define PRESENT(c,x) (find(ALL(c),x) != (c).end())

#define ABS(a) ((a)<0?-(a):(a))
#define SQ(x) (x)*(x)
#define INF 0xffffff00
#define ESP 1e-6

#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define MININ(a) *min_element(a.begin(), a.end())
#define MININ_A(a,n) *min_element(a, a+n)
#define MAXIN(a) *max_element(a.begin(), a.end())
#define MAXIN_A(a,n) *max_element(a, a+n)

#define P(x) cout << x 
#define PE(x) cout << x << endl 
#define SI ({int _x; scanf("%d",&_x); _x;})
#define SLL ({long long _x; scanf("%lld",&_x); _x;})
#define SLF ({double _x; scanf("%lld",&_x); _x;})
#define SC getchar()
#define SS(n) scanf("%s",n)

class Triple { 
	public:
		int x, y, z, best;
		bool surprising ; 
		Triple( int a, int b, int c ) { 
			x = a ; y = b ; z = c ; 
			surprising = (abs(x-y) == 2 || abs(x-z) == 2 || abs(y-z) == 2) ; 
			best = max(x, max(y,z)) ; 
		} 
};

vector<Triple> V [ 33 ] ;

bool foundNotSurprising( int t, int p ) { 
	FOR0(i, V[t].SZ()){
		if ( !V[t][i].surprising && V[t][i].best >= p ) { return true ; } 
	}
	return false ;
}

bool foundSurprising ( int t, int p ) { 
	FOR0(i, V[t].SZ()){
		if ( V[t][i].surprising && V[t][i].best >= p ) { return true ; } 
	}
	return false ;
}

int main () {
	for ( int i = 0 ; i < 11 ; i ++ ) { 
		for ( int j = i ; j < 11 ; j ++ )  {
			for ( int k = j ; k < 11 ; k ++ ) { 
				if ( abs(j-i) > 2 || abs(k-i) > 2 || abs(k-j) > 2 ) { } 
				else { V[i+j+k].PB(Triple(i,j,k)); }
			}
		}
	}
	int TEST = SI ;
	TEST ++ ; 
	FOR1(test, TEST) {
		int N = SI ;
		int S = SI ;
		int p = SI ;
		int m = 0 ;
		FOR0(i, N) { 
			int t = SI ; 
			if ( foundNotSurprising(t, p) ) { m ++ ; } 
			else if ( S > 0 ) { 
				if ( foundSurprising(t, p) ) {
					m ++; 
					S --;
				}
			}
		}
		cout << "Case #" << test << ": " << m << endl ;
	}
	return 0 ;
}
















