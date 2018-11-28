#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstring>
#include <map>
#include <cmath>
#include <queue>
#include <string>
#include <vector>
using namespace std;

typedef long long LL ;
typedef vector<int> VI ;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define sqr( x ) ((x)*(x))
template<class T> inline void checkmax( T&a ,T b ){ if(b>a) a=b;}
template<class T> inline void checkmin( T&a ,T b ){ if(b<a) a=b;}
template<class T> inline T gcd( T a , T b ){ return b?gcd(b,a%b):a;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}

const double eps = 1e-15 ;
const int MAXN = 105 ;
const int MAXM = 17 ;
const int INF = 1 << 20 ;


string str[MAXN] ;
int N ;

bool check( int k , int j ){
	for( int i = N-1 ; i > k ; i -- )
		if( str[j][i] == '1' ) return false;
	return true ;
}

int main(){

	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);

	int cases ; scanf("%d",&cases);

	for( int tc = 1 ; tc <= cases ; tc ++ ){
		cin >> N  ;
		for( int i = 0 ; i < N ; i ++ ){
			cin >> str[i] ; 
		}
		int res = 0 ;
		for( int j = 0 ; j < N ; j ++ ){
			for( int i = j ; i < N ; i ++ )
				if( check( j , i ) ){
					for( ; i > j ; i -- )
						swap(str[i],str[i-1] ) , res ++  ;
					break;
				}
		}
		cout << "Case #" << tc << ": " << res << endl ;
	}
}
