#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <iomanip>
#define stream istringstream
#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define repl(i,n) for(__typeof(n) i=1; i<=(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define INF (1<<28)
#define PI 3.14159265358979323846264338327950
#define pb(x) push_back(x)
#define ppb pop_back
#define all(x) x.begin(),x.end()
#define cclear(x,y) memset(x,y,sizeof(x));
#define mem(x,y) memset(x,y,sizeof(x));
#define eps 1e-9
#define pii pair<int,int>
#define pll pair<long long,long long>
#define pmp make_pair



using namespace std;

template<class T> inline T gcd(T a,T b) {if(a<0)return 
gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b) {if(a<0)return 
lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline T sqr(T x){return x*x;}
template<class T> T power(T N,T P){ return (P==0)?  1: N*power(N,P-1); }
template<class T> bool inside(T a,T b,T c){ return (b>=a && b<=c);}
typedef long long i64;
typedef unsigned long long ui64;

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
const i64 INF64 = (i64)1E16;


int distsq2d(int x1,int y1,int x2,int y2){return sqr(x1-x2)+sqr(y1-y2);}
double dist2d(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}
double dist3d(double x1,double y1,double z1,double x2,double y2,double z2){	return sqrt(sqr(x1-x2)+sqr(y1-y2)+sqr(z1-z2));}

i64 toInt64(string s){i64 r=0;istringstream sin(s);sin>>r;return r;}
double LOG(i64 N,i64 B){	return (log10l(N))/(log10l(B));	}
string itoa(long long a){if(a==0) return "0";string ret;for(long long i=a; i>0; i=i/10) ret.push_back((i%10)+48);reverse(ret.begin(),ret.end());return ret;}

vector< string > token( string a, string b ) 
{
	const char *q = a.c_str();while( count( b.begin(), b.end(), *q ) ) q++;vector< string > 
	oot;while( *q ) {const char *e = q;while( *e && !count( b.begin(), b.end(), 
	*e ) ) e++;oot.push_back( string( q, e ) );q = e;while( count( b.begin(), 
	b.end(), *q ) ) q++;}return oot;
}
//bool operator < ( const node& p ) const {      return w < p.w;   }
int isvowel(char s){s=tolower(s); if(s=='a' || s=='e' || s=='i' || s=='o' || s=='u')return 1; return 0;}
int isupper(char s) {if(s>='A' and s<='Z') return 1; return 0;}
int Set(int N,int pos){return N=N | (1<<pos);}
int reset(int N,int pos){return N= N & ~(1<<pos);}
int check(int N,int pos){return (N & (1<<pos));}
int toggle(int N,int pos){if(check(N,pos))return N=reset(N,pos);return N=Set(N,pos);}
void pbit(int N){	printf("("); for(int i=10;i>=0;i--)	{bool x=check(N,i);cout<<x;}	puts(")");}



#define mx 203
i64 Di[mx],Li[mx];

int n;
i64 TL;

bool dp[mx][mx];
bool vis[mx][mx];
int call(int i,int j)
{
	if(j==n)return 1;
	i64 cov=min(Di[j]-Di[i],Li[j]);
	
	if(vis[i][j]) return dp[i][j];
	vis[i][j]=1;
	int ret=0;
	for(int k=j+1;k<=n;k++)
	{		
		
		if(Di[j]+cov>=Di[k])
		{
			
			int get=call(j,k);
			if(get==1) ret=1;
		}
	}
	return dp[i][j]=ret;
	
	
}
int main()
{	
	READ("in");
	WRITE("outAS.txt");
	int t,kas=0;
	cin>>t;
	while(t--)
	{
		mem(vis,0);
		cin>>n;
		for(int i=1;i<=n;i++)
		{
			cin>>Di[i]>>Li[i];
		}
		cin>>TL;
		Di[n+1]=TL;
		n++;
	
	
	
		int ret=call(0,1);
		printf("Case #%d: ",++kas);
		if(ret) puts("YES");
		else puts("NO");
		
	}


	
	
}
