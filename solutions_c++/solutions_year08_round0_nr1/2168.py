#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <sstream>
#include <limits.h>
#include <cassert>
#include <stack>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <complex>
#include <cstring>
#include <map>
using namespace std;

#define FOR(i,n) for(int i = 0 ; i < n ; i++)
#define FOZ(i,v) FOR(i,int(v.size()))
#define FOT(it,v) for(typeof(v.begin()) it = v.begin(); it != v.end(); it++)
#define rep(i,x,y) for(int i=(x);   \
	( i )<=( (y)); i ++)
typedef vector<vector< int> > vvi;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define vv(T) vector< vector < T > >
#define Sort(v) sort(v.begin(),v.end());

void test(int casenum) { 
	int s, q; 
	scanf("%d\n", &s);
	char buf[200] ;
	
	map<string, bool> reached; 
	FOR(i,s) { 
		fgets(buf, 200, stdin) ;
		assert(strlen(buf) != 0);
		reached[buf] = false ;
	}
	

	int count = 0 ;
	int tc = 0 ;
	scanf("%d\n", &q) ;

	FOR(i,q) { 
		fgets(buf, 200, stdin) ;
		assert(strlen(buf) != 0);
		if ( reached.count(buf) == 0 or reached[buf]  ) continue; 
		else { 
			tc ++ ;
			reached[buf] = true; 
		}
		if ( tc == s ) { /* careful */ 
			count ++ ;
			FOT(it, reached) 
				it->second = false ; 
			reached[buf] = true ; 
			tc = 1 ; 
		}
	}

	
	printf("Case #%d: %d\n", casenum, count) ;
	
}
int main() {

	int n ; 
	scanf("%d\n", &n) ;
	for(int i = 1; i <= n ; i++)  test(i) ; 
	return 0;
}
