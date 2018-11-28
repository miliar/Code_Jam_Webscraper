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

#define p3 pair<int, pair<int,int> >
#define X first
#define Y second
#define mp3(x,y,z) mp(x,mp(y,z))

void init(){
}

void solve(){
	int n = readInt();
	vector<p3> v;
	fo(i,n){
		int x = readInt(), y = readInt(), z = readInt();
		v.pb(mp3(x,y,z));
	}
	sort(v.begin(),v.end());
	vector<pii> A;
	int ret  = 0;
	fo(i,v.size()){
		int x = v[i].X;
		int rem = 10000-x;
		A.pb(mp(v[i].Y.X,v[i].Y.Y));
		sort(A.begin(),A.end());
		int cur = 0;
		multiset<int> S;
		S.insert(-1000000);
		for(int j=0;j<A.size();j++){
			int y  = A[j].X;
			int z = rem - y;
			if(z < 0) break;
			S.insert(A[j].Y);
			multiset<int>::iterator it = S.end();
			--it;
			while(*it > z) S.erase(it--);
			cur = max(cur, (int)S.size()-1);
		}
		ret = max(ret, cur);
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

