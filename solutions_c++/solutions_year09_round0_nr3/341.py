#include<iostream>
#include<cstdio>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<functional>
#include<complex>
#include<iomanip>
#include<numeric>
#include<cassert>
#include<cstring>
#include<cmath>
#include<ctime>
#include<cctype>
#include<utility>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#include<set>
#include<list>
#include<bitset>
#include<map>

using namespace std;

template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> T gcd( T a , T b ){ return b==0?a:gcd(b,a%b);}

const double pi=acos(-1.0);
const double eps=(1e-9);
const int Dx[8]={-1,0,0,1,-1,1,1,-1};
const int Dy[8]={0,-1,1,0,1,1,-1,-1};
const int op[4] = {3,2,1,0};
const int MAXN = 105;
const int MAXM = 105 ;
const int MOD = 10000 ;
const double inf = 1e50;

typedef long long LL ; 
//typedef __int64 LL ;

const char patten[] = {"welcome to code jam"};
char word[505];
int dp[20] ;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int cases ; scanf("%d",&cases);getchar();int sz = strlen( patten ) ;
	for( int k = 1 ; k <= cases ; k ++ ){
		gets( word ) ;int len = strlen( word ) ; 
		memset( dp , 0 ,sizeof( dp ) ) ;dp[0] = 1;
		for( int i = 0 ; i < len ; i++ ){
			for( int j = sz ; j > 0 ; j -- )
				if( word[i] == patten[j-1] )
					dp[j] = ( dp[j] + dp[j-1] ) % MOD  ;
		}
	  printf("Case #%d: %04d\n",k,dp[sz] );
	}
}
