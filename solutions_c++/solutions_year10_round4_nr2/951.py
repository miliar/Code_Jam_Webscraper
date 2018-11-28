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
template<typename T> T gcd(T a, T b){return a?gcd(b%a,a):b;}
int bitCount(int x) { return __builtin_popcount(x);}
lint two(int x) { return (1LL<<x);}
template<typename T> bool checkMax(T & ret, T & cur){ if(ret < cur) { ret = cur; return true; } return false;}
template<typename T> bool checkMin(T & ret, T & cur){ if(ret > cur) { ret = cur; return true; } return false;}
				     
const char eof = -123;
int readInt(){	int x;if(scanf("%d",&x) != 1) return eof;return x;}
char readChar() { char c; if(scanf("%c",&c) != 1) return eof; return c;}
lint readLL(){lint x; if(cin>>x) return x; return eof;}
double readDouble(){double f;if(scanf("%lf",&f) == 1)return f;return eof;}

void init(){
}



lint canMiss[1<<12];
lint cost[1<<12][1<<12];

int n;
lint inf = (1LL<<60);

lint cache[1<<12][12][12];
lint get(int root, int missed, int height){
	if(height == n) return (missed > canMiss[root])?inf:0;
	lint& ret = cache[root][missed][height];
	if(ret != -1) return ret;
	ret = inf;

	{
		lint A = get(2*root, missed, height+1);
		lint B = get(2*root+1, missed, height+1);
		ret = min(ret, A + B + cost[height][root]);
	}

	{
		lint A = get(2*root, missed+1, height+1) + get(2*root+1, 1, height+1);
		lint B = get(2*root, 1, height+1) + get(2*root+1, missed+1, height+1);
		ret = min(ret, max(A,B));
	}
	return ret;
}
void solve(int testCase){
	n = readInt();
	fo(i,(1<<n)) canMiss[i] = readInt();
	for(int i=n-1;i>=0;--i){
		fo(j,(1<<i)) cost[i][j] = readInt();
	}
	memset(cache,-1,sizeof(cache));
	lint ret = get(0, 0, 0);
	cout<<ret<<endl;
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

