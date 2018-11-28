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


int P[MAXN][MAXN] ;
int N , K ;

int inter( int i , int j ){
	for( int k = 0 ; k < K ; k ++  ){
		if( P[i][k] >= P[j][k] ) return 0 ;
	}
	return 1 ;
}


int a[MAXN][MAXN],ans,mk[MAXN] ,ymate[MAXN];

bool dfs( int p ){
	for( int i = 0 ; i < N ; i ++ ){
		if( a[p][i] && !mk[i] ){
			mk[i] = 1 ;
			int t = ymate[i] ; ymate[i] = p ;
			if( t == -1 || dfs( t ) ) return true ;
			ymate[i] = t ;
		}
	}
	return false ;
}


int match(){
	memset( ymate , -1 , sizeof(ymate) ) ;
	int res = 0 ;
	for( int i = 0 ; i < N ; i ++ ){
		memset(mk, 0 , sizeof(mk) ) ;
		if( dfs(i) ) res ++ ;
	}
	return res ;
}

int main(){

	freopen("C-large.in","r",stdin);
	freopen("out.out","w",stdout);

	int cases ; scanf("%d",&cases);

	for( int tc = 1 ; tc <= cases ; tc ++ ){
		cin >> N >> K ;
		for( int i = 0 ; i < N ; i ++ )
			for( int j = 0 ; j < K ; j ++ )
				scanf("%d",&P[i][j] ) ;
	
		memset(a,0,sizeof(a));

		for( int i = 0 ; i < N ; i ++ )
			for( int j = 0 ; j < N ; j ++ )
				a[i][j] = inter( i , j ) ;
		ans = match();
		//for( int i = 0 ; i < N ; i ++ ) cout<<i<<" " <<ymate[i] << endl;
		printf("Case #%d: %d\n",tc , N - ans);
	}
}
