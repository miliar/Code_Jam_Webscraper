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

int delCost, insertCost, M, N;
int v[111];
/*
int memo[111][256];
int doit(int x, int last){
	if(x == N) return 0;
	int& ret = memo[x][last];
	if(ret != -1) return ret;
	ret = (N-x)*delCost;
	for(int i=0;i<256;++i) if(abs(last-i) <= M) ret = min(ret, doit(x,i) + insertCost); //insert
	for(int i=0;i<256;++i) if(abs(last-i) <= M) ret = min(ret, doit(x+1,i) + abs(i-v[x])); //modify
	ret = min(ret, doit(x+1,last) + delCost); //delete
	return ret;
}
*/

int best[111][256];
void solve(int testCase){
	cerr<<testCase<<": ";
	delCost = readInt(); insertCost = readInt(); M = readInt(); N = readInt();
	fo(i,N) v[i] = readInt();
	int ret = delCost * N;

	queue<int> q;
	int inf = (1<<29);
	fo(i,N+1) fo(j,256) best[i][j] = inf;
	fo(i,256){
		q.push(N); q.push(i); best[N+1][i] = 0;
	}

	while(!q.empty()){
		int y = q.front(); q.pop();
		int i = q.front(); q.pop();
		int cost = best[y+1][i];
//		if(i==125) cout<<i<<" "<<y<<" "<<cost<<endl;
//		cout<<y<<" "<<i<<" "<<cost<<endl;
//		ret = min(ret, cost + delCost*(y+1) + ((y>=0)?abs(i-v[y]):0) );
		if(y==-1) continue;

		for(int last=0;last<256;++last) if(abs(last-i)<=M){
			int x = y;
			int newCost = cost + insertCost;
			if(best[x+1][last] <= newCost) continue;
			best[x+1][last] = newCost; q.push(x); q.push(last);
		}

		for(int last=0;last<256;++last) if(abs(last-i)<=M){
			if(y==0) continue;
			int x = y-1;
			int newCost = cost + abs(i-v[x]);
			ret = min(ret, newCost + delCost*x);
			if(best[x+1][last] <= newCost) continue;
			best[x+1][last] = newCost; q.push(x); q.push(last);
		}

		{
			int x = y-1;
			int last = i;
			int newCost = cost + delCost;
			if(best[x+1][last] <= newCost) continue;
			best[x+1][last] = newCost; q.push(x); q.push(last);
		}
	}
	assert(ret <= delCost*(N-1));
	cout<<ret<<endl;
	cerr<<ret<<endl;
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

