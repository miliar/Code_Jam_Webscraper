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

int stest;
int a[103][103];
int m, n, sl;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &stest);
	rep(ee,1,stest){
		scanf("%d%d%d", &m, &n, &sl);		
		fill1(a);
		while(sl--){
			int i,j; 
			scanf("%d%d", &i, &j);
			a[i][j]=-2;
		}
		a[1][1]=1;		
		rep(i,1,m)rep(j,1,n)if(a[i][j]>=0) {
			if(i+2<=m && j+1<=n && a[i+2][j+1]!=-2) {
				if(a[i+2][j+1]==-1)a[i+2][j+1]=a[i][j];
				else a[i+2][j+1]=(a[i][j]+a[i+2][j+1])%10007;
			} 
			if(i+1<=m && j+2<=n && a[i+1][j+2]!=-2) {
				if(a[i+1][j+2]==-1)a[i+1][j+2]=a[i][j];
				else a[i+1][j+2]=(a[i][j]+a[i+1][j+2])%10007;
			} 
		}
		if(a[m][n]>=0)
		printf("Case #%d: %d\n", ee, a[m][n]);
		else printf("Case #%d: %d\n", ee, 0);
	}
	
	return 0;
}
