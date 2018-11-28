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
using namespace std;

#define REP(i,n) for(__typeof(n) i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define INF (1<<30)
#define eps 1e-9
#define PB(x) push_back(x)
#define CLEAR(x) memset(x,0,sizeof(x));
#define ALL(x) x.begin(),x.end()
#define SZ size()

#define VI vector<int>
#define VS vector<string>
#define LL long long
#define MII map<int,int>
#define MSI map<string,int>
#define MIS map<int,string>


#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)



template<class T> inline T gcd(T a,T b) {if(a<0)return 
gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b) {if(a<0)return 
lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}

int SetBit(int N,int pos){	return N=(N | (1<<pos));}
int ResetBit(int N,int pos){	return N=(N & ~(1<<pos));}

typedef long long i64;
typedef unsigned long long ui64;

string itoa(long long a){string ret;for(long long i=a; i>0; i=i/10) 
ret.push_back((i%10)+48);reverse(ret.begin(),ret.end());return ret;}
vector< string > token( string a, string b ) {const char *q = 
a.c_str();while( count( b.begin(), b.end(), *q ) ) q++;vector< string > 
oot;while( *q ) {const char *e = q;while( *e && !count( b.begin(), b.end(), 
*e ) ) e++;oot.push_back( string( q, e ) );q = e;while( count( b.begin(), 
b.end(), *q ) ) q++;}return oot;}
double dist(double x1,double y1,double x2,double y2){return 
sqr(x1-x2)+sqr(y1-y2);}


i64 dist(i64 x1,i64 y1,i64 x2,i64 y2){return (sqr(x1-x2)+sqr(y1-y2));}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return 
r;}//NOTES:toInt(
i64 toInt64(string s){i64 r=0;istringstream sin(s);sin>>r;return 
r;}//NOTES:toInt64(
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return 
r;}//NOTES:toDouble(



int main() 
{
	 freopen("in","r",stdin);
	 freopen("out","w",stdout);
	 
	 int kas=0,i,T,j;
	 cin>>T;
	 while(T--)
	 {
		 int N,H,L;
		 
		 int A[1002];
		 
		 cin>>N>>L>>H;
		 
		 for(i=1;i<=N;i++)
		 cin>>A[i];
		 
		 int imp=1,ans;
		 for(i=L;i<=H;i++)
		 {
			 int fl=1;
			 for(j=1;j<=N;j++)
			 {
				 if(A[j]%i==0 || i%A[j]==0) {}
				 else
				 {fl=0;break;}
				 
				 
				
			 }
			 if(fl) 
			 {
				 ans=i;
				 imp=0;
				 break;
				
			}
			 
			 
			 
			 
		 }
		 
		 
		 
		 
		 
		 
		 
		 
		 printf("Case #%d: ",++kas);
		 if(!imp) cout<<ans<<endl;
		 else puts("NO");
	
		    
		 
		 
		 
		 
		 
		 
	 }
	 

	
	
	  

         return 0;
 }

