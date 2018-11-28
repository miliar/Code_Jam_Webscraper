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

lint cnt[3][3];
lint p[9];

void add(lint X, lint Y)
{
	cnt[X%3][Y%3]++;
	p[(X%3)*3 + (Y%3)]++;
}
main()
{
	int cases = readInt();
	int tc = 0;
	while(cases--){
		++tc;
		int n = readInt();
		lint A = readLL();
		lint B = readLL();
		lint C = readLL();
		lint D = readLL();
		lint X0 = readLL();
		lint Y0 = readLL();
		lint MOD = readLL();
		fo(i,3)fo(j,3) cnt[i][j] = 0;
		fo(i,9) p[i] = 0;
		lint X, Y;
		X = X0, Y = Y0;
		add(X, Y);
		fo(i,(n-1)){
			X = (A*X + B)%MOD;
			Y = (C*Y + D)%MOD;
			add(X,Y);
		}
		lint ret = 0;
		fo(i,9)fo(j,(i+1))fo(k,(j+1)){
			if( (i/3 + j/3 + k/3)%3) continue;
			if( (i%3 + j%3 + k%3)%3) continue;
			if(i==j && j==k)
				ret = ret + p[i]*(p[i]-1)*(p[i]-2)/6;
			else if(j==k)
				ret = ret + p[i] * (p[j])*(p[j]-1)/2;
			else if(i==j)
				ret = ret + p[i]*(p[i]-1)/2 * p[k];
			else ret = ret + p[i] * p[j] * p[k];
		}
		printf("Case #%d: ",tc);
		cout<<ret<<endl;
	}
}

