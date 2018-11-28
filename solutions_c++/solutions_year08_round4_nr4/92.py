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
void init(){
}


int n;
char buf[100000];
int f[32][32];

int memo[1<<16][1<<4][1<<4];
int inf = 100000000;
int doit(int mask,int last,int final)
{
	if(mask == (1<<n)-1) return f[last][final];
	int& ret = memo[mask][last][final];
	if(ret != -1) return ret;
	ret = inf;
	fo(i,n) if(~mask & (1<<i))
		ret <?= f[last][i] + doit(mask | (1<<i) , i , final);
	return ret;
}

void solve(){
	n = readInt();
	scanf(" %s",buf);
	string s = buf;
	fo(first,n)fo(second,n) if(first != second){
		f[first][second] = 0;
		for(int i=0;i<s.size();i+=n){
			if(s[i+first] != s[i+second]) f[first][second]++;
		}
	}
	int ret = inf;
	memset(memo,-1,sizeof(memo));
	fo(x,n)fo(y,n) if(x != y){
		int cur = 0;
		for(int i=n;i<s.size();i+=n){
			if(s[i + x] != s[i-n+y]) cur++;
		}
		cur += doit((1<<x)|(1<<y),x,y);
		ret <?= cur;
	}
	cout<<ret+1<<endl;
}

main()
{
	init();
	int cases = readInt();
	int tc = 0;
	while(cases--){
		tc++;
		printf("Case #%d: ",tc);
		solve();
	}
}

