#include <iostream>
#include <algorithm>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <vector>
using namespace std;

typedef long long LL ;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

template<class T> inline void checkmax( T&a ,T b ){ if(b>a) a=b;}
template<class T> inline void checkmin( T&a ,T b ){ if(b<a) a=b;}
template<class T> inline T gcd( T a , T b ){ return b?gcd(b,a%b):a;}
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}


const int MAXN = 105 ;
const int MAXM = 270 ;

map<char,int> base ;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int cases ; string str ;
	scanf("%d",&cases);
	for( int k = 1 ; k <= cases ; k ++ ){
		cin >> str ;
		int B  = 0 ;
		for( int i = 0 ; i < str.size() ; i ++ ){
			if( base.find( str[i] ) != base.end()  ) continue ;
			base[str[i]] = B++ ;
		}
		LL res = 0 ; if( B <= 1 ) B = 2 ;
		for( int i = 0 ; i < str.size() ; i ++ ){
			int d = base[str[i]] ;
			if( d == 0 ) d = 1 ;
			else if( d == 1 ) d = 0 ;
			res = res * B + d ;
		}
		cout << "Case #"<<k <<": "<< res << endl ; base.clear();
	}
}