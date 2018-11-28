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

void tcInit(){
}

/////////// INIT BLOCKS END ///////

void solve(){
	int n = readInt();
	VI v;
	fo(i,n){
		char buf[100];
		scanf(" %s",buf);
		string s = buf;
		int cnt = 0;
		fo(j,n) if(s[j] == '1') cnt = j;
		v.pb(cnt);
	}
	int ret = 0;
	fo(i,v.size()){
		for(int j=i;j<v.size();++j) if(v[j] <= i){
			for(int k=j;k>=i+1;--k) v[k] = v[k-1]; 
			ret += (j-i);
			break;
		}
	}
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


