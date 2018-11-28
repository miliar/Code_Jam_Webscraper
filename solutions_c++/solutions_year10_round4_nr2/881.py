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

#define in "in.in"
#define out "out.out"

const int INF = (1<<29);
const LL  LINF = (1LL<<60);
const int MAXN = 50+10 ;

int N , A[MAXN][MAXN] ;

int main(){
	//freopen(in,"r",stdin);
	//freopen(out,"w",stdout);

	int cases; scanf("%d",&cases);
	for( int test = 1 ; test <= cases; test ++ ){
		scanf("%d",&N);
		for( int i = 1 ; i <= N*2-1 ; i ++ ){
			int limit =  i>N ? N-(i-N) : i ;
			for( int j = 0 ; j < limit ; j ++ ){
				scanf("%d",&A[i][j] );
			}
			
		}
		for( int i = 1 ; i <= N*2-1 ; i ++ ){
			int limit =  i>N ? N-(i-N) : i ;
			
			for( int j = 0 ; j < limit ; j ++ )
				cout << A[i][j] << " " ;
			cout << endl;
		}
	}
}
