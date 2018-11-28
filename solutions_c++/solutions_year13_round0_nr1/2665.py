
#include <cstdio>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <limits>
#include <utility>
#include <numeric>
#include <iterator>
#include <algorithm>
using namespace std;

const int INF=(1<<30)-1;
const long long LINF=(1ll<<62)-1;
const int DIRX[]={-1,0,0,1,-1,-1,1,1}, DIRY[]={0,-1,1,0,-1,1,-1,1};
const double ERR=1e-11, PI=(2*acos(0.0));

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)<(b)?(b):(a))
template<class T> inline T MIN(T a,T b) {return ((a<b)?(a):(b));}
template<class T> inline T MAX(T a,T b) {return ((b<a)?(a):(b));}
template<class T> inline T ABS(T a) {return ((a<0)?(-a):(a));}
template<class T> inline void checkMIN(T& a,T b) {if(b<a) a=b;}
template<class T> inline void checkMAX(T& a,T b) {if(a<b) a=b;}
template<class T> inline T SQR(T x) {return (x*x);}
template<class T> inline T GCD(T a,T b) {T c; while((c=a%b)!=0)a=b,b=c; return b;}
template<class T> inline T fastPow(T Base,T Power) {T Result=1; while(Power>0){if(Power&1)Result*=Base; Power>>=1; Base*=Base;} return Result;}
template<class T> inline T fastModPow(T Base,T Power,T Mod) {T Result=1;while(Power>0){if(Power&1)Result=(Result*Base)%Mod; Power>>=1; Base=(Base*Base)%Mod;} return (Result%Mod);}
inline int compDouble(double x,double y) {double d=x-y; if(d-ERR>0.0) return 1; else if(d+ERR<0.0) return -1; else return 0;}

#define ALL(X)       (X).begin(),(X).end()
#define Size(X)      ((int)(X).size())
#define REP(i,n)     for(i=0;i<(n);i++)
#define FORI(x,a,b)  for(x=(a);x<=(b);x++)
#define FORD(x,a,b)  for(x=(a);x>=(b);x--)
#define MEM(X,with)  memset((X),(with),sizeof(X))
#define EACH(X,itr)  for( __typeof((X).begin()) itr=(X).begin(); itr!=(X).end(); itr++)
#define Contains(X,item)    ((X).find(item)!=(X).end())
#define Contains_n(X,item)	(find((X).begin(),(X).end(),(item))!=(X).end())
#define PB  push_back
#define MP  make_pair
#define fs  first
#define sc  second

typedef unsigned long long ULL;
typedef long long      LL;
typedef stringstream   SS;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<LL>     VL;
typedef vector<int>    VI;
typedef pair<int,int>  Pii;

string b[4];
string ans;

inline bool win(char ch)
{
	int c,t;
	
	// horizontal
	for(int i=0;i<4;i++)
	{
		c=t=0;
		for(int j=0;j<4;j++)
		{
			if(b[i][j]==ch) c++;
			else if(b[i][j]=='T') t++;
		}
		if(t<=1 && c+t==4) return true;
	}
	
	// vertical
	for(int j=0;j<4;j++)
	{
		c=t=0;
		for(int i=0;i<4;i++)
		{
			if(b[i][j]==ch) c++;
			else if(b[i][j]=='T') t++;
		}
		if(t<=1 && c+t==4) return true;
	}
	
	// diagonal
	{
		c=t=0;
		for(int i=0;i<4;i++)
		{
			if(b[i][i]==ch) c++;
			else if(b[i][i]=='T') t++;
		}
		if(t<=1 && c+t==4) return true;
	}
	{
		c=t=0;
		for(int i=0,j=3;i<4;i++,j--)
		{
			if(b[i][j]==ch) c++;
			else if(b[i][j]=='T') t++;
		}
		if(t<=1 && c+t==4) return true;
	}
	
	return false;
}

inline bool draw()
{
	for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(b[i][j]=='.') return false;
	return true;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int kases;cin>>kases;
	for(int kaseno=1;kaseno<=kases;kaseno++)
	{
		for(int i=0;i<4;i++)cin>>b[i];
		
		if(win('X')) ans="X won";
		else if(win('O')) ans="O won";
		else if(draw()) ans="Draw";
		else ans="Game has not completed";
		
		cout<<"Case #"<<kaseno<<": "<<ans<<endl;
	}
	
	
	return 0;
}
