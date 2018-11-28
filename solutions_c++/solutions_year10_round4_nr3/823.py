#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FOR(i,N) for(int i=0;i<N;i++)
#define MP (x,y) make_pair(x,y)
#define SIZE(X) ((int)(X.size()))

using namespace std;

typedef long long LL;
typedef unsigned long long LLU;
typedef pair<int,int> PII;
typedef pair<int,PII> PPII;
template<class T> void checkmin(T& a,T b){if(a>b)a=b;}
template<class T> void checkmax(T& a,T b){if(a<b)a=b;}
template<class T> void gcd(T a,T b){return b?gcd(b,a%b):a;}

const double EPS=(1e-10);

#define in "C-small-attempt0.in"
#define out "out.out"

const int INF = (1<<29);
const LL  LINF = (1LL<<60);
const int MAXN = 1000 ;
int mk[MAXN][MAXN]  ;
int nmk[MAXN][MAXN] ;

int sx , sy , ex , ey ;
void mark( int a , int b , int c , int d ){
	for( int i = a ; i <= c ; i ++ )
		for( int j = b ; j <= d ; j ++ )
			mk[i][j] = 1 ;
}

int over(){
	for( int i = 0 ; i < MAXN ; i ++ )
		for( int j = 0 ; j < MAXN ; j ++ )
			if( mk[i][j] ) return 0 ;
	return 1;
}

void change(){
	//memset( nmk , 0 , sizeof(nmk) ) ;
	for( int i = sx ; i <=ex ; i ++ )
		for( int j = sy ; j <= ey ; j ++ )
			nmk[i][j] = 0 ;
	for( int i = sx ; i <=ex ; i ++ )
		for( int j = sy ; j <= ey ; j ++ ) if( mk[i][j] == 1 ){
			
			if( mk[i-1][j] == 0 && mk[i][j-1] == 0 ){
				//cout << i << " " << j << endl;
				//nmk[i][j] = 0 ;
			}else nmk[i][j] = 1;

	}else{
		if( mk[i-1][j] == 1 && mk[i][j-1] == 1 ){
			//cout << i << " " << j << endl;
			nmk[i][j] = 1 ;
		}
	}
	int nsx = INF , nsy = INF , nex = -INF , ney = -INF ; 
	for( int i = sx ; i <= ex+1; i ++ )
		for( int j = sy ; j <= ey+1 ; j ++ ){
			mk[i][j] = nmk[i][j] ;
			if( mk[i][j] ){
				checkmax( nex , i ) ;
				checkmax( ney , j ) ;
				checkmin( nsx , i ) ;
				checkmin( nsy , j ) ;
			}
		}
	sx = nsx , sy = nsy , ex = nex , ey = ney ;
}
int N ;

void show(){
	for( int i = 0 ;i <= 10 ;cout<<endl, i ++ )
		for( int j = 0 ; j <= 10 ; j ++ ) cout << mk[i][j] ;
}
int main(){
	freopen(in,"r",stdin);
	freopen(out,"w",stdout);

	int cases; scanf("%d",&cases);
	for( int test = 1 ; test <= cases; test ++ ){
		scanf("%d",&N);
		memset( mk , 0 , sizeof(mk) ) ;
		int x1 , y1 , x2 , y2 ;
		sx = INF , sy = INF , ex = -INF , ey = -INF ; 
		for( int i = 0 ; i < N ; i ++ ){
			cin >> y1 >> x1 >> y2 >> x2 ;
			mark(x1,y1,x2,y2) ;
			checkmax( ex , x2 ) ;
			checkmax( ey , y2 ) ;
			checkmin( sx , x1 ) ;
			checkmin( sy , y1 ) ;
		}
		int ret = 0 ;
		//show();
		while( sx<=ex && sy<=ey ){
			//cout << sx << " " << sy << " " << ex << " " << ey << endl;
			ret++;
			change() ;
			//show();
			//cout << sx << " " << sy << " " << ex << " " << ey << endl;
		}
		
		cout << "Case #"<< test <<": "<<ret << endl;
	}
}
