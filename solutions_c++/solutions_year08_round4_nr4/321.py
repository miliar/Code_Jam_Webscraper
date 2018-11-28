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

int testi(string s, const vector<int> &perm) {
	int k = perm.size();
	string ns = s ; 
	for(int start = 0 ; start < s.size() ; start += perm.size()) { 
		FOR(i,k) { 
			ns[start+i] = s[start + perm[i]];
		}
	}

//	cout<<ns<<endl;
	ns.resize((unique(ns.begin(), ns.end())) - ns.begin()) ;
	return ns.size();
}
void test(int __case) {
	cout <<"Case #"<<__case<<": ";

	int k ;
	char s[2000]; 
	scanf("%d\n%s\n", &k , s) ;
	vector<int> perm(k); 
	
	FOR(i,k) perm[i] = i ;

	int mn  = INT_MAX ; 
	do { 
		mn = min(mn, testi(s, perm) );
	}while (next_permutation(perm.begin(), perm.end())) ;
	
	
	cout<<mn<<endl;
}
int main() {
	int t;
	scanf("%d\n", &t);
	FOR(i,t) test(i+1);

  return 0;
}
