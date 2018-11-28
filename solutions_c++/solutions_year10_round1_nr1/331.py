#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <functional>
#include <algorithm>
#include <numeric>
#include <bitset>
#include <cmath>
#include <sstream>
#include <complex>
#include <deque>
#include <cassert>
using namespace std;

#define fo(a,b) for(int a=0;a<b;++a)
#define pb push_back
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin();it != (c).end();++it)
#define mp make_pair
typedef long long int lint ;
typedef pair<int,int> pii;
typedef vector<string> VS;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef stringstream SS;

template<typename T> void print( T a, string name="" ) {if(name != "") cerr<<name<<":";cerr << a;}
static void print( long long a, string name="" ) {if(name != "") cerr<<name<<":";cerr << a << "LL";}
static void print( string a, string name="" ) {if(name != "") cerr<<name<<":";cerr << '"' << a << '"';}
template<typename T, typename W> void print(pair<T,W> P,string name="") {if(name != "") cerr<<name<<":"; cerr<<"("; print(P.first); cerr<<","; print(P.second); cerr<<")";}
template<typename T> void print( vector<T> a, string name="" ) {if(name!="")cerr<<name<<":";cerr << "{";for ( int i = 0 ; i != a.size() ; i++ ) 
{if ( i != 0 ) cerr << ", ";print( a[i] );}cerr << "}" << endl;}
void printBits(unsigned int x,int end = 32,int start = 0){for(int i = end-1;i>=start;i--) if(x & (1<<i)) cout<<1<<" "; else cout<<0<<" ";}
template<typename T> void printEndl( T x,string name="") { print(x,name); cerr<<endl;}

template<typename T> vector<T> tokenize(string s, string delim){int i=0,j=0; vector<T> ret;for(;i<s.size();++i)
{j = s.find_first_of(delim,i);if(j==-1)j=s.size();if(j>i){ stringstream in(s.substr(i,j-i)); T temp; in>>temp; ret.pb(temp);}i=j;}return ret;}
int bitCount(int x) { return __builtin_popcount(x);}
template<typename T> bool checkMax(T & ret, T & cur){ if(ret < cur) { ret = cur; return true; } return false;}
template<typename T> bool checkMin(T & ret, T & cur){ if(ret > cur) { ret = cur; return true; } return false;}

const char eof = -123;

int readInt(){	int x;if(scanf("%d",&x) != 1) return eof;return x;}
char readChar() { char c; if(scanf("%c",&c) != 1) return eof; return c;}
lint readLL(){lint x; if(cin>>x) return x; return eof;}
double readDouble(){double f;if(scanf("%lf",&f) == 1)return f;return eof;}

void init(){
}

string g[55], s[55];
bool checkHorizontal(int i,int j, int K){
	int n = g[0].size();
	char c = g[i][j];
	for(int k=0;j<n&&k<K;++k,++j) if(g[i][j] != c) return false;
	return true;
}
bool checkVertical(int i,int j,int K){
	int n = g[0].size();
	char c = g[i][j];
	for(int k=0;i<n&&k<K;++i,++k) if(g[i][j] != c) return false;
	return true;
}
bool checkDiagonal(int i,int j,int K){
	int n = g[0].size();
	char c = g[i][j];
	if(i+K <= n && j+K<=n){
		bool good = true;
		for(int k=0;k<K;++k) if(g[i+k][j+k] != c) good = false;
		if(good) return true;
	}
	if(i+K <= n && j >= K-1){
		for(int k=0;k<K;++k) if(g[i+k][j-k] != c) return false;
		return true;
	}
	return false;
}
void solve(int testCase){
	int n = readInt();
	int k = readInt();
	fo(i,n){ cin>>s[i];}
	fo(i,n){
		g[i] = "";
		fo(j,n) if(s[i][j] != '.') g[i] += s[i][j];
		if(g[i].size() < n) g[i] = string(n-g[i].size(),'.') + g[i];
	}
	int blue = 0, red = 0;
	fo(i,n)fo(j,n) if(g[i][j] != '.'){
		if(j + k <= n && checkHorizontal(i,j,k)) ((g[i][j]=='B')?blue:red)=1;
		if(i + k <= n && checkVertical(i,j,k)) ((g[i][j]=='B')?blue:red)=1;
		if(checkDiagonal(i,j,k)) ((g[i][j]=='B')?blue:red)=1;		
	}
	if(blue && red) cout<<"Both"<<endl;
	if(blue &&!red) cout<<"Blue"<<endl;
	if(!blue&& red) cout<<"Red"<<endl;
	if(!blue&&!red) cout<<"Neither"<<endl;
}

main()
{
	init();
	int cases = readInt();
	int tc = 0;
	while(cases--){
		tc++;
		printf("Case #%d: ",tc);
		solve(tc);
	}
}

