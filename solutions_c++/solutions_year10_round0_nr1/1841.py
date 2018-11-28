#include<set>
#include<map>
#include<list>
#include<cmath>
#include<ctime>
#include<queue>
#include<stack>
#include<cstdio>
#include<cctype>
#include<vector>
#include<string>
#include<fstream>
#include<sstream>
#include<iomanip>
#include<numeric>
#include<cassert>
#include<cstring>
#include<utility>
#include<algorithm>
#include<iostream>
#include<functional>

#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
#define MP(X,Y) make_pair(X,Y)
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<pair<string,int> > VSI;
typedef vector<pair<int,string> > VIS;
typedef vector<pair<int,int> > VII;
typedef map<int,int> MII;
typedef map<string,string> MSS;
typedef map<string ,int > MSI;
typedef map<int , string > MIS;
typedef priority_queue<char,vector<char>,greater<char> > PCG;


#if defined WIN32
typedef __int64 LL ;
typedef unsigned __int64 LLU;
#else
typedef long long LL;
typedef unsigned long long LLU;
#endif

template<class T> inline void Checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void Checkmax(T &a,T b){if(b>a) a=b;}
template<class T> T Sqr(T x){return x*x;}
template<class T> void Clear(const T* A,int n,T v){for(int i=0;i<n;i++)A[i]=v;}
template<class T> void Clear(const T** A,int n,int m,T v){for(int i=0;i<n;i++)Clear(A[i],m,v);}
template<class T> void Output(const T* A,int n){for(int i=0;i<n;i++)cout<<A[i]<<" ";cout<<endl;}
template<class T> void Output(const T** A,int n,int m){for(int i=0;i<n;i++)outPut(A[i],m);}
template<class T> inline T Gcd(T a,T b)
{if(a<0)return Gcd(-a,b);if(b<0)return Gcd(a,-b);return (b==0)?a:Gcd(b,a%b);}

 
const double PI=acos(-1.0);
const double EI=2.718281828459;
const double EPS=(1e-5);
const int INF = (1<<29);
const LL  LINF = (1LL<<60);
const int Dx[8]={-1,0,1,0,-1,1,1,-1};
const int Dy[8]={0,1,0,-1,1,1,-1,-1};

const int MAXN = 10000;
const int MAXM = 50010 ;

int main(int argc, char *argv[]){

	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int cases ; scanf("%d",&cases);
	for( int k = 1 ; k <= cases ; k ++ ){
		int N , K ;
		cin >> N >> K ;
		printf("Case #%d: %s\n",k,(K%(1<<N))==((1<<N)-1)?"ON":"OFF");
	}
	return 0;
}
