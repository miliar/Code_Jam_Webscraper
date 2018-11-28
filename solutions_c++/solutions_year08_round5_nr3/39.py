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

int m , n;
VS g;
int broken[100][100];

int match[4000];
int done[4000];

int dfs(int i,int j)
{
	int hash = (j/2)*m + i;
	if(done[hash]) return 0;
	done[hash] = 1;
	for(int x = i-1;x<=i+1;x++)for(int y=j-1;y<=j+1;y++){
		if(y != j && x >= 0 && x < m && y >= 0 && y < n && !broken[x][y]){
			int F = (y/2)*m + x;
			if(match[F] == -1 || dfs(match[F]%m,2*(match[F]/m))){
				match[F] = hash;
				return 1;
			}	
		}
	}
	return 0;
}

void solve(){
	m = readInt();
	n = readInt();
	g.clear();
	char buf[100];
	fo(i,m){
		scanf(" %s",buf);
		g.pb(string(buf));
	}
	fo(i,m)fo(j,n) broken[i][j] = (g[i][j]=='x');
	int ret = m*n;
	fo(i,m)fo(j,n) if(broken[i][j]) ret--;
	memset(match,-1,sizeof(match));
	fo(j,n)if(j%2==0) fo(i,m) if(!broken[i][j]) {
		memset(done,0,sizeof(done));
		if(dfs(i,j)) ret--;
	}
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
		solve();
	}
}

