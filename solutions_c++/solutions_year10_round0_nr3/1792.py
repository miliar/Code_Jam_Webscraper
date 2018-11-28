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

const int MAXN = 1000+1000;
const int MAXM = 50010 ;

LL G[MAXN] ;
int Next[MAXN] ;
LL R, K ;
int N ;
int mk[MAXN] ;
LL Td[MAXN] ;
int Begin , Len , bid ;

void FindCycle(){
	memset( mk , 0 , sizeof(mk) ) ;
	bid = 0  ;int cnt = 1   ;
	while( !mk[bid] ){
		mk[bid] = cnt ++ ;
		bid = Next[bid] ;
	}
	//cout << id << " " << cnt << endl;
	Begin = mk[bid] ; Len = cnt - mk[bid]  ;
}

LL Go( int begin , int Len ){
	if( !Len ) return 0 ;
	return Td[begin] + Go( Next[begin] , Len-1) ;
}
int main(int argc, char *argv[]){

	freopen("C-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int cases ; scanf("%d",&cases);
	for( int k = 1 ; k <= cases ; k ++ ){
		scanf("%d%lld%lld",&R,&K,&N);
		for( int i = 0 ; i < N ; i ++ ) scanf("%d",&G[i]);
		for( int i = 0 ; i < N ; i ++ ){
			Td[i] = 0 ; int j ;
			for( j = i ; j < N+i ; j ++ ){
				if( Td[i] + G[j%N] <= K ) Td[i] += G[j%N] ;
				else break;
			}
			//cout << sum << " " << j << endl;
			Next[i] = j % N  ;
			//cout << Td[i] << " " ;
		}
		//cout << endl;
		
		FindCycle() ;

		//cout << Begin << " " << Len << " "  << endl;
		LL ret = 0 ;
		if( R <= Begin ){
			ret += Go( 0 , R ) ;
		}else{
			ret += Go( 0 , Begin-1 ) ; 
			//cout << ret << endl; 
			R -= Begin-1 ;
			//cout << Go( 0 , Len ) << endl;
			ret += (R/Len) * Go(bid,Len) ;
			//cout << ret << endl;
			ret += Go(bid,R%Len) ;
			//cout << ret << endl;
		}		
		printf("Case #%d: %lld\n",k,ret);
	}
	return 0;
}
