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


int g, m, n, stest;
int a[2003][2003];
int sl[2003];
int res[2003];
int ok[2003];
V(int) w[2003];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &stest);
	rep(ee, 1, stest){
		scanf("%d", &n);
		scanf("%d", &m);
		rep(i,1,m)rep(j,1,n)a[i][j]=-1;
		fill(sl);
//		rep(i,1,m)w[i].clear();
		rep(i,1,m){
			scanf("%d", &g);sl[i]=g;
			while(g--){
				int kind, type;
				scanf("%d%d", &type, &kind);
				a[i][type]=kind;
//				w[i].PB(type);
			}
		}
		fill(res);	fill(ok);
		int yes=1;
		while(1){
			int ra=1;
			rep(i, 1, m) if(ok[i]==0 && sl[i]==1){
				ra=0;
				rep(j,1,n)if(a[i][j]>=0) {
					ok[i]=1;
					res[j]=a[i][j];
					sl[i]--;
					rep(k, 1, m)if(ok[k]==0 && a[k][j]>=0){
						if(a[k][j]==a[i][j]) ok[k]=1,sl[k]--; else {
							sl[k]--;
							if(sl[k]==0) yes=0;
							a[k][j]=-1;
						}
					}
					break;
				}				
			}
			if(yes==0)break;
			if(ra)break;
		}

		cout<<"Case #"<<ee<<":";
		if(yes) {
			rep(i,1,n)printf(" %d", res[i]);
			printf("\n");
		} else printf(" IMPOSSIBLE\n");
	}
	return 0;
}
