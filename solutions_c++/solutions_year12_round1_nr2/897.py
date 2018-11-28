
#include <cstdio>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cmath>
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
template<class T> T GCD(T a,T b) {return ((!b)?(a):GCD(b,a%b));}
template<class T> T fastPow(T Base,T Power) {T Result=1; while(Power>0){if(Power&((T)1))Result*=Base; Power>>=1; Base*=Base;} return Result;}
template<class T> T fastModPow(T Base,T Power,T Mod) {T Result=1; while(Power>0){if(Power&((T)1))Result=(Result*Base)%Mod; Power>>=1; Base=(Base*Base)%Mod;} return (Result%Mod);}
inline int compDouble(double x,double y) {double d=x-y; if(d-ERR>0.0) return 1; else if(d+ERR<0.0) return -1; else return 0;}

#define all(X)       (X).begin(),(X).end()
#define Size(X)      ((int)(X).size())
#define DUMP(x)      cout << #x << " = " << x << endl;
#define rep(x,n)     for(x=0;x<(int)(n);x++)
#define fori(x,a,b)  for(x=(a);x<=(b);x++)
#define ford(x,a,b)  for(x=(a);x>=(b);x--)
#define Mem(X,with)  memset((X),(with),sizeof(X))
#define Each(X,itr)  for( __typeof((X).begin()) itr=(X).begin(); itr!=(X).end(); itr++)
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

#define sz 1003
int a[sz], b[sz];
bool aa[sz], bb[sz];

int main()
{
//	freopen("in.txt","r",stdin);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	int i,j,k,n;
	int have,cnt;
	
	int _kase,kase=0;
	scanf("%d",&_kase);
	while(kase++<_kase)
	{
		scanf("%d",&n);
		rep(i,n)
		{
			scanf(" %d %d",&a[i],&b[i]);
			aa[i]=bb[i]=false;
		}
		
		have=0;
		cnt=0;
		while(have<2*n)
		{
			rep(i,n)if(!bb[i])if(b[i]<=have) break;
			
			if(i<n)
			{
				//printf("B %d\n",i);
				if(!aa[i])
				{
					have++; aa[i]=true;
				}
				have++; cnt++; bb[i]=true;
				continue;
			}
			
			k=-1;
			rep(i,n)if(!aa[i])if(a[i]<=have)if(k==-1 || b[i]>b[k]) k=i;
			
			if(k!=-1)
			{
				//printf("A %d\n",k);
				have++; cnt++; aa[k]=true;
				continue;
			}
			
			break;
		}
		
		printf("Case #%d: ",kase);
		if(have<2*n) printf("Too Bad");
		else printf("%d",cnt);
		printf("\n");
	}
	
	return 0;
}
