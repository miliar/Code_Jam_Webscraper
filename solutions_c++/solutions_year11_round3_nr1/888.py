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
	 
	 int R,C,T,i,j,kas=0;
	 cin>>T;
	 while(T--)
	 {
		 char mat[200][200];
		 cin>>R>>C;
		 for(i=0;i<R;i++)
		 {
			 
			 cin>>mat[i];
		 
		 }
		 for(i=0;i<R;i++)
		 {
			 
			 for(j=0;j<C;j++)
			 {
				 if(mat[i][j]=='#')
				 {
					int f1=1,f2=0,f3=0,f4=0;
					if(j+1<C && mat[i][j+1]=='#') f2=1;
					if(i+1<R && j+1<C && mat[i+1][j+1]=='#') f3=1;
					if(i+1<R && mat[i+1][j]=='#') f4=1;
					if(f1 && f2 && f3 && f4)
					{
						mat[i][j]='/';	mat[i][j+1]='\\';
						mat[i+1][j+1]='/';			mat[i+1][j]='\\';
						
					}
				 }
				 
				 
			 }
			 
			 
		 }
		 
		 int IMP=0;
		 printf("Case #%d:\n",++kas);
		 
		 for(i=0;i<R;i++)
		    for(j=0;j<C;j++)
		    if(mat[i][j]=='#') IMP=1;
		    
		   if(IMP) puts("Impossible");
		   else
		   { 
				for(i=0;i<R;i++)
		 
			 cout<<mat[i]<<endl;
			 
		 }
		 
		 
		 
		 
		 
	 }
	 

	
	
	  

         return 0;
 }

