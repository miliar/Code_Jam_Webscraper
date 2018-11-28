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

int n;
int AND = 1, OR = 0;
int change[20000], val[20000], type[20000];
int inf = 10000000;

void init(){
}

int memo[20000][2];
int doit(int root, int required){
	if(val[root] == required) return 0;
	if(root >= (n-1)/2) return inf;
	int& ret = memo[root][required];
	if(ret != -1) return ret;
	ret = inf;
	fo(i,2)fo(j,2){
		if(type[root] == AND && ((i&j)==required) ) ret <?= doit(2*root+1, i) + doit(2*root+2, j);
		if(type[root] == OR && ((i|j)==required) ) ret <?= doit(2*root+1, i) + doit(2*root+2, j);
	}
	if(change[root]){
		fo(i,2)fo(j,2){
			if(type[root] != AND && ((i&j)==required) ) ret <?= 1 + doit(2*root+1, i) + doit(2*root+2, j);
			if(type[root] != OR && ((i|j)==required) ) ret <?= 1 + doit(2*root+1, i) + doit(2*root+2, j);
		}
	}
	return ret;
}

void solve(){
	n = readInt();
	memset(memo,-1,sizeof(memo));
	int req = readInt();
	fo(i,(n-1)/2){
		type[i] = readInt();
		change[i] = readInt();
	}
	for(int i=(n-1)/2;i<n;i++){
		val[i] = readInt();
	}
	for(int i=(n-1)/2-1;i>=0;i--){
		if(type[i] == AND){
			val[i] = (val[2*i+1] & val[2*i+2]);
		}
		else val[i] = (val[2*i+1] | val[2*i+2]);
	}
	int ret = doit(0, req);
	if(ret < inf){
		cout<<ret<<endl;
	}
	else cout<<"IMPOSSIBLE"<<endl;
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

