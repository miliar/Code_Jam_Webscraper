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

using namespace std;

#define FOR(i,n) for(int i = 0 ; i < n ; i++)
#define FOZ(i,v) FOR(i,int(v.size()))
#define rep(i,x,y) for(int i=(x);   \
	( i )<=( (y)); i ++)
typedef vector<vector< int> > vvi;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define vv(T) vector< vector < T > >
#define Sort(v) sort(v.begin(),v.end());
const int siz = (1<<21)+20;
const int dit = (1<<20); 

int ar[siz] ;

void insert(int n) { 

	int  t = dit+n ; 
	assert(ar[t] == 0);
	while(t) { 
		ar[t] ++ ;
		t >>= 1; 
	}
}

int _count(int s, int e, int S = 0, int E = dit-1, int seg = 1 ) { 
	if ( s == S and e == E ) return ar[seg];
	assert( s >= S and e <= E and s <= e);
	int m = (S+E) /2 ; 
	if ( e <= m) return _count(s, e, S, m, 2*seg); 
	else if ( s > m) return _count(s, e, m+1, E, 2*seg+1) ;
	else return _count(s, m, S,m, 2*seg) + _count(m+1, e, m+1, E, 2*seg+1);
}

int count(int s, int e) {
	return (e-s+1 - _count(s,e) );
}
int find(int req, int s, int e, int S = 0 , int E = dit - 1 , int seg = 1 ){

	assert( s >= S and e <= E and s <= e);

	assert( count (s,e) >= req) ;
	if ( S == E ) return S ; 
	int m = (S+E)/2 ; 

	assert ( m - S +1 == (E-S+1)/2);

	if ( s >m ) {
		return find(req, s, e, m+1, E, 2*seg+1);
	}

	if ( e <= m ) { 
		return find(req, s, e, S, m, 2*seg);
	}
	if (  count(s, m) >= req ) { 

		return find(req, s, m, S, m, 2*seg) ; 
	}

	else {
		return find(req -  count(s,m), m+1, e, m+1, E, 2*seg+1);
	}
}

void test(int __case) { 
	int k; 
	cin >> k ; 
	int p ; 
	cin>>p; 
	vector<int> d(p); 
	FOR(i,p) cin>>d[i] ;

	fill( ar, ar+siz, 0);

	vector<int> ans(k);
	int pos = 0 ;
	FOR(i,k) { 
		int req = i+1 ;
		req %= count(0, k-1);
		if ( req == 0 ) req = count(0, k-1);
		if ( count(pos, k-1) < req ) { 
			req -= count(pos,k-1) ;
			pos = 0 ;
		} 
		assert(req != 0);
		pos = find (req, pos, k-1) ;


		assert( pos < k);
		assert(ar[pos+dit] == 0);
		assert(ans[pos] == 0);
		ans.at(pos) = i+1;
		insert(pos);
		pos ++ ;
		pos %= k;
		
	} 

	printf("Case #%d: ", __case) ;
	FOR(i,p) { 
		printf("%d ", ans.at(d.at(i)-1));
	}
	printf("\n");
}
int main() {
	int t ;
	cin>> t; 
	FOR(i,t) test(i+1) ; 

	return 0;
}
