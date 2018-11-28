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

void print(int a,int b,int c,int d,int e,int f){
	printf("%d %d %d %d %d %d\n",a,b,c,d,e,f);
}

void solve(){
	int m = readInt();
	int n = readInt();
	int A = readInt();
	for(int y1=0;y1<=n;y1++)
		for(int y3=0;y3<=n;y3++)
			for(int x2=0;x2<=m;x2++){
				int rem = A - x2*(y3-y1);
				if(rem != 0){
					if(y1 == 0) continue;
					if(rem %y1) continue;
					if(rem/y1 < 0 || rem/y1 > m) continue;
					print(0,y1,x2,0,rem/y1,y3);
					return;
				}
				else{
					print(0,y1,x2,0,0,y3);
					return;
				}
				rem = -A - x2*(y3-y1);
				if(rem != 0){
					if(y1 == 0) continue;
					if(rem %y1) continue;
					if(rem/y1 < 0 || rem/y1 > m) continue;
					print(0,y1,x2,0,rem/y1,y3);
					return;
				}
				else{
					print(0,y1,x2,0,0,y3);
					return;
				}
			}
	cout<<"IMPOSSIBLE"<<endl;
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

