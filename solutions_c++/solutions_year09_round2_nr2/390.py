#include <iostream>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <vector>
using namespace std;

#ifdef __GNUC__
typedef long long LL;
typedef unsigned long long LLU;
#else
typedef __int64 LL;
typedef unsigned __int64 LLU;
#endif

#define FOR(x,a,b) for(int x=(a);x<(int)(b);x++) 
#define All(a) (a).begin(),(a).end()
#define SIZE(a) (a).size()
#define LENGTH(a) (a).length()
#define TWO(a) (1<<a)
#define CONTAIN(a,b) ((a)&TWO(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))


template<class T> inline void checkmax( T&a ,T b ){ if(b>a) a=b;}
template<class T> inline void checkmin( T&a ,T b ){ if(b<a) a=b;}
template<class T> inline T gcd( T a , T b ){ return b?gcd(b,a%b):a;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}


const int MAXN = 15;
const int MAXM = 100 ;

char num[200] ;
int len ;

bool find( int& f , int& t ){
	for( int i = len - 1 ; i >= 0 ; i -- ){
		for( int j = len-1 ; j > i ; j -- )
			if( num[j] > num[i] ){
				f = i , t = j ;
				return true ;
			}
	}
	return false ;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("out1.out","w",stdout);
	int cases; scanf("%d",&cases);getchar();
	for( int k = 1 ; k <= cases ; k ++ ){
		cout << "Case #" << k << ": " ; 
		scanf("%s",num);
		len = strlen(num); int f , t ;
		if( find( f , t ) ){
			swap( num[f] , num[t] ) ;
			sort( num+f+1 , num+len ) ;
			puts( num );
		}else{
			sort( num , num+len ) ;
			for( int i = 0 ; i < len ; i ++ ) 
				if( num[i] != '0' ){
					cout << num[i] << "0" ; num[i] = -1 ; break;
				}
				for( int i = 0 ; i < len ; i ++ ){
					if( num[i] == -1 ) continue ;
					cout << num[i] ;

				}
			cout << endl ;
		}
	}
}



