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

void globalInit(){
}

const int MAXN = 100;
int n,k;
int edge[MAXN][MAXN];
int price[MAXN][25];
int done[MAXN];
int match[MAXN];

void tcInit(){
	memset(edge,0,sizeof(edge));
}

/////////// INIT BLOCKS END ///////

int getDir(int i,int j){
	int l1 = price[i][0], l2 = price[j][0];
	if(l1 == l2) return 0;

	bool lessThan = (l1 < l2);
	fo(a,k) if(a > 0){
		int r1 = price[i][a];
		int r2 = price[j][a];
		if(r1 == r2) return 0;
		if(lessThan){
			if(r1 > r2) return 0;
		}
		else{
			if(r1 < r2) return 0;
		}
		l1 = r1;
		l2 = r2;
	}
	return lessThan ? -1 : 1 ;
}

bool augment(int u){
	if(done[u]) return false;
	done[u] = true;
	fo(i,n) if(edge[u][i]){
		if(match[i] == -1 || augment(match[i])){
			match[i] = u;
			return true;
		}
	}
	return false;
}
int maxFlow(){
	int ret = 0;
	memset(done,0,sizeof(done));
	memset(match,-1,sizeof(match));
	fo(i,n){
		if(augment(i)) ret++;
		memset(done,0,sizeof(done));
	}
	return ret;
}
void solve(){
	n = readInt();
	k = readInt();
	fo(i,n){
		fo(j,k) price[i][j] = readInt();
	}
	int ret = 0;
	fo(i,n){
		fo(j,i) {
			int dir = getDir(i,j);
			if(dir == -1) {
				edge[i][j] = 1;
			}
			else if(dir == 1){
				edge[j][i] = 1;
			}
		}
	}

	int flow = maxFlow();
	ret = n - flow;
	cout<<ret<<endl;
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


