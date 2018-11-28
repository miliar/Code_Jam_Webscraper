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
using namespace std;

#define pb push_back
#define mp make_pair
#define pii pair<int,int>

#define fo(i,n) for(int i=0; i < (n) ; ++i)
#define FO(i,a,b) for(int i=a;i<=(b);++i)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define REV(v) reverse(ALL(v))
#define UNIQ(v) (v).erase(unique(ALL(v)),(v).end())

#define VDebug(x)  {fo(i,(x).size()) cout<<(x)[i]<<" ";cout<<endl;}
#define VVDebug(x) {fo(j,(x).size()) VDebug(x[j])}
				     
typedef istringstream iss;
typedef ostringstream oss;
typedef long long int lint;
typedef complex<double> point;
				     
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef vector<VS> VVS;
				     
const char eof = -123;

void printBits(unsigned int x,int end = 32,int start = 0){for(int i = end-1;i>=start;i--) if(x & (1<<i)) cout<<1<<" "; else cout<<0<<" ";}
int readInt(){	int x;if(scanf("%d",&x) != 1) return eof;return x;}
char readChar() { char c; if(scanf("%c",&c) != 1) return eof; return c;}
lint readLL(){lint x; if(cin>>x) return x; return eof;}
double readDouble(){double f;if(scanf("%lf",&f) == 1)return f;return eof;}

void globalInit();
void tcInit();
void tcEnd();

//////////// START HERE ///////////
const int MAXL = 500;
int memo[MAXL][19];
string s = "welcome to code jam";

void globalInit(){
}

void tcInit(){
	memset(memo,-1,sizeof(memo));
}

/////////// INIT BLOCKS END ///////

string t;
int doit(int x,int index){
	if(index == s.size()) return 1;
	if(x == t.size()) return 0;
	int& ret = memo[x][index];
	if(ret != -1) return ret;
	ret = 0;
	ret += doit(x + 1, index);
	if(s[index] == t[x])
		ret += doit(x + 1, index+1);
	ret %= 10000;
	return ret;
}
void solve(){
	char buf[MAXL+2];
	scanf(" %[^\n]",buf);
	t = string(buf);
	printf("%.4d\n",doit(0,0));
}


main()
{
	globalInit();
	int cases = readInt();
	int tc = 0;
	while(cases--){
		tc++;
		printf("Case #%d: ",tc);
		tcInit();
		solve();
		tcEnd();
	}
}

void tcEnd(){
}


