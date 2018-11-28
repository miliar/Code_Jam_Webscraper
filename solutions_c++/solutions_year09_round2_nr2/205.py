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

string test()
{
	string k;
	cin >>k;
	FOR(i,20) k = string("0") + k;

	next_permutation (k.begin(), k.end());
	assert (k[0] == '0');
	FOZ(i,k) if (k[i] != '0') 
		return k.substr (i);
	return k;
}


int main() {

	int t;
	cin >>t;
	FOR(i,t) cout<<"Case #" <<i+1<<": "<<test()<<endl;
	return 0;
}
