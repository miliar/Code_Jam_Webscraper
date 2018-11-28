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
char a[103][103];
int f[10][1<<10];
int m, n;
int co(int e, int j){
	return (e>>j)&1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &stest);
	rep(ee, 1, stest){
		scanf("%d%d", &m, &n);
		fori(i,m) scanf("%s", a[i]);

		fill(f);
		
		int res=0;
		fori(e, (1<<n)) {
			int pre=-3;
			int ok = 1;
			int d=0;
			fori(j, n) if((co(e, j)) && a[m-1][j]=='.') {
				if(pre==j-1) ok =0;
				d++;
				pre=j;
			}
			if(ok) {
				f[m-1][e]=d;
				res>?=d;
			}
		}

						  
		for(int k=m-2;k>=0;k--){
			fori(e, (1<<n)){
				int pre=-3;
				int ok = 1;
				int d=0;
				
				fori(j, n) if(co(e,j) && a[k][j]=='.') {
					if(pre==j-1) ok =0;
					d++;
					pre=j;
				}	

				if(ok){							
					fori(e1, (1<<n)){
						int ok1 = 1;
						fori(j, n) if(co(e1, j) && ((j && co(e, j-1))||((j<n-1) && co(e,j+1)))) ok1=0;
						if(ok1){
							f[k][e]>?=f[k+1][e1]+d;
							res>?=f[k][e];
						}
					}
				} 	
			}
		}					
		printf("Case #%d: %d\n", ee, res);
	}
		
	return 0;
}
