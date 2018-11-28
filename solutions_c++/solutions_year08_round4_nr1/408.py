#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define V(a) vector<a>
#define fori(i, n) for(int i=0;i<n;i++)
#define rep(i, a, b) for(int i=a;i<=b;i++)
#define forv(i, a) for(int i=0;i<a.size(); i++)
#define fill(a) memset(a, 0, sizeof(a));
#define fill1(a) memset(a, -1, sizeof(a));
#define LL long long
#define PB push_back
#define SZ(x) (x.size())


vector<string> split( const string& s, const string& delim =" " ) { vector<string> res; string t; for ( int i = 0 ; i != s.size() ; i++ ) { if ( delim.find( s[i] ) != string::npos ) { if ( !t.empty() ) { res.push_back( t ); t = ""; } } else { t += s[i]; }  } if ( !t.empty() ) {  res.push_back(t); } return res; }
vector<int> splitInt( const string& s, const string& delim =" " ) { vector<string> tok = split( s, delim ); vector<int> res; for ( int i = 0 ; i != tok.size(); i++ ) res.push_back( atoi( tok[i].c_str() ) ); return res; }
template<class T> T tok(string s) {	T a; stringstream ss(s); ss>>a; return a; };
template<class T> string str(T a) {	ostringstream ss; ss<<a; return ss.str();};

int stest, n, V;
const int inf = 1000000;
const int maxn=10003;
int f[maxn][2];
int gate[maxn], change[maxn];

int cal(int a, int b, int e){
	if(e==1) return a&b; else return a|b;
}

int go(int i, int v){
	if(f[i][v]<inf) return f[i][v];

	if(i>(n-1)/2)return gate[i]==v?0:inf; else  {
		int &res=f[i][v]=inf;
		int e1[2],e2[2];
		e1[0] = go(i*2, 0);
		e1[1] = go(i*2, 1);
		e2[0] = go(i*2+1, 0);
		e2[1] = go(i*2+1, 1);

		if(change[i]==0){
			fori(r1,2)fori(r2,2) if(cal(r1,r2,gate[i])==v){
				res=min(res, e1[r1]+e2[r2]);
//				if(i==1) printf("co ra %d\n", res);
			}
		} else {
			 fori(r1,2)fori(r2,2) if(cal(r1,r2,gate[i])==v){
				res=min(res, e1[r1]+e2[r2]);
			 }
//			 printf("%d %d %d %d\n", e1[0], e2[1], gate[i], v);
//			 printf("mm %d %d %d\n", cal(0, 1, 0), cal(e1[0], e2[1], 0), 0|1);
			 fori(r1,2)fori(r2,2) if(cal(r1,r2,1-gate[i])==v){
//				 printf("OK %d %d %d %d\n", r1, r2, e1[r1], e2[r2]);
				res=min(res, 1+e1[r1]+e2[r2]);
			 }
		}								 
		return res;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &stest);
	rep(ee,1, stest){
		scanf("%d%d", &n, &V);
		rep(i, 1, (n-1)/2) {
			scanf("%d%d", &gate[i], &change[i]);
		}
		rep(i, ((n-1)/2) + 1, n) {
			scanf("%d", &gate[i]);
		}
		rep(i,1,n)fori(k,2)f[i][k]=inf;
		go(1, V);
		//go(3, 1);
//		printf("%d \n", f[3][1]);
//		printf("%d \n", f[1][1]);
		if(f[1][V]>=inf) printf("Case #%d: IMPOSSIBLE\n", ee);
		else printf("Case #%d: %d\n", ee, f[1][V]);
	}
	
	return 0;
}
