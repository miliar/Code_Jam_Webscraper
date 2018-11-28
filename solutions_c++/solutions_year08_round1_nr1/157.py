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

LL a[1000];
LL b[1000];
int n, stest;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &stest);
	rep(ee, 1, stest){
		scanf("%d", &n);
		fori(i,n)cin>>a[i];
		fori(i,n)cin>>b[i];
		sort(a, a+n);
		sort(b, b+n);
		LL res=0;
		fori(i,n)res+=a[i]*b[n-i-1];
		cout<<"Case #"<<ee<<": "<<res<<endl;
	}
	return 0;
}
