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


const int MAXN = 1000000;
const int MAXM = 100 ;

struct node{
	int L , R ;
	string feature;
	double wei;
};

node mem[MAXN] ;

string str ; int p , tp ;

int NewNode( ){
	mem[tp].L = mem[tp].R = -1 ;
	mem[tp].feature = "" ;
	mem[tp].wei = 0 ;
	return tp ++ ;
}
int build( ){
	int root = NewNode() ;
	p ++ ; double t = 0 ;
	while( isdigit( str[p] ) ) t = t*10 + str[p] - '0' , p ++ ;
	if( str[p] == '.' ){
		int base = 10 ; p ++ ;
		while( isdigit( str[p] ) ){
			if( base <= 1000000000 ){
				t += ( ( double )( str[p] - '0' ) ) / base  ;
				base *= 10 ;
			}
			p ++ ;
		}
	} mem[root].wei = t ;
	if( islower( str[p] ) ){
		while( islower( str[p] ) ){
			mem[root].feature += str[p] ; p ++ ;
		}
		mem[root].L = build() ;
		mem[root].R = build();
	} p++ ; 
	return root ;
}

void print( int root ){
	cout << mem[root].wei << endl ; 
	if( mem[root].L != -1 ){
		print( mem[root].L);
		print( mem[root].R);
	}
}

void Add( string tmp ){
	for( int i = 0 ; i < tmp.size() ; i ++ ){
		if( !isspace( tmp[i] ) )
			str += tmp[i] ;
	}
}

vector<string> feature(200) ;
int n ;
double ans ;

bool Have( string feat ){
	for( int i = 0 ; i < n ; i ++ ){
		if( feature[i] == feat )
			return true ;
	}
	return false ;
}
void solve( int root ){
	ans *= mem[root].wei ;
	if( mem[root].feature != "" ){
		if( Have( mem[root].feature ) ){
			solve( mem[root].L ) ;
		}else{
			solve( mem[root].R ) ;
		}
	}
	return ;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("outAl.out","w",stdout);
	int cases; scanf("%d",&cases);getchar();
	for( int k = 1 ; k <= cases ; k ++ ){
		int line , A  ; string name ;
		cin >> line ; getchar() ; str = "" ;
		for( int i = 0 ; i < line ; i ++ ){
			getline( cin , name ) ;
			Add( name ) ;
		}
		//cout << str << endl ;
		tp = 0 ; p = 0 ; int root = build( ) ;// print( root );
		cin >> A ;  cout << "Case #" << k <<":" << endl;
		for( int i = 0 ; i < A ; i ++ ){
			cin >> name >> n ;
			for( int i = 0 ; i < n ; i ++ ){
				cin >> feature[i] ;
			}
			ans = 1.0 ; solve( root ) ;
			printf("%.8lf\n",ans);
		}
	}
}



