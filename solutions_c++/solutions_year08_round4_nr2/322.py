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
void test(int __case) { 
	cout<<"Case #"<<__case<<": "; 
	int N, M; 
	long long A; 
	cin>>N>>M>>A; 
	
	FOR(x2, N+1) FOR(x3,N+1) FOR(y1, M+1) FOR(y3, M+1) { 
		long long ar = -x2*y1 + y1*x3 +x2*y3; 
		if ( ar < 0 ) ar = -ar ; 
		if ( ar == A ) { 
			cout<<0<<" "<<y1<<" "<<x2<<" "<<0<<" "<<x3<<" "<<y3<<endl;
			return; 
		}
	}

	cout<<"IMPOSSIBLE\n";
}
int main() {

	int t; 
	cin>>t; 
	FOR(i,t) test(i+1);
  return 0;
}
