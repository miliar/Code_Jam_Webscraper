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
#include <cstring>
#include <climits>
#include <ctime>

#define FOR(i,N) for(int i=0;i<(N);i++)
#define REP(i,a,b) for(int i=(a);i<=(b);i++)
#define Out(v) cerr << #v << ": " << (v) << endl;
#define MP make_pair
#define SIZE(X) ((int)(X.size()))

using namespace std;

typedef long long LL;
typedef unsigned long long LLU;
typedef pair<int,int> PII;
template<class T> void checkmin(T& a,T b){if(a>b)a=b;}
template<class T> void checkmax(T& a,T b){if(a<b)a=b;}
template<class T> T gcd(T a,T b){return b?gcd(b,a%b):a;}

const double EPS=(1e-10);
const int INF = (1<<29);
const LL  LINF = (1LL<<60);
const int MAXN = 100+10 ;

int dp[ MAXN ][ MAXN ][ MAXN ] ;
vector<pair<char,int> > A;
int update( int& a , int b ){ if(a==-1||a>b){a=b;return 1;}return 0;}
int go( int nowo , int nowb , int nextto ){
	if( nextto >= SIZE(A) )return 0;
	if( dp[nowo][nowb][nextto] != -1 )
		return dp[nowo][nowb][nextto];
	int ret = -1 ;
	if( A[nextto].first == 'O' && A[ nextto ].second == nowo )
		REP( i ,-1, -1 ){
			int nb = nowb + i ;
			if( nb < 1 || nb > 100 ) continue;
			update( ret , go( nowo , nb , nextto+1 ) + 1 );
		}
		
	if( A[nextto].first == 'B' && A[ nextto ].second == nowb )
		REP( i ,-1, -1 ){
			int no = nowo + i ;
			if( no < 1 || no > 100 ) continue;
			update( ret , go( no , nowb , nextto+1 ) + 1 );
		}
	REP( i , -1 , 1 ){
		int no = nowo + i ;
		if( no < 1 || no > 100 ) continue;
		REP( j , -1 , 1 ){
			if( i == 0 && j == 0 ) continue;
			int nb = nowb + j ;
			if( nb < 1 || nb > 100 ) continue;	
			update( ret , go( no , nb , nextto ) + 1 ) ;
		}
	}
	return dp[nowo][nowb][nextto] = ret;
}
int N ;
int solve(){
	dp[0][1][1] = 0 ;
	REP( i , 0 , N ){
		queue<PII> Q;
		REP( nowo , 1, 100 )REP( nowb , 1 , 100 ) if( dp[i][nowo][nowb] != -1 )Q.push( MP(nowo,nowb ) ) ;
		while( !Q.empty() ){
			int nowo = Q.front().first;
			int nowb = Q.front().second; Q.pop();
			REP( dx , -1 , 1 ){
				int no = nowo + dx ;
				if( no < 1 || no > 100 ) continue;
				REP( dy , -1 , 1 ){
					if( dx == 0 && dy == 0 ) continue;
					int nb = nowb + dy;
					if( nb < 1 || nb > 100 ) continue;
					if( update( dp[i][no][nb] , dp[i][nowo][nowb]+1) )
						Q.push( MP(no,nb) );
				}
			}
		}
		REP( nowo , 1, 100 )REP( nowb , 1 , 100 ) if( dp[i][nowo][nowb] != -1 )
			if( A[i].first == 'O' && A[i].second == nowo ){
				REP( dy , -1 , 1 ){
					int nb = nowb + dy ;
					if( nb < 1 || nb > 100 ) continue;
					update( dp[i+1][nowo][nb] , dp[i][nowo][nowb]+1 );
				}
			}else if( A[i].first == 'B' && A[i].second == nowb){
				REP( dx , -1 , 1 ){
					int no = nowo + dx ;
					if( no < 1 || no > 100 ) continue;
					update( dp[i+1][no][nowb] , dp[i][nowo][nowb]+1 );
				}
			}
	}

	int ret = -1 ;
	REP( i ,1 , 100 )REP( j , 1 ,100)if( dp[N][i][j] != -1 ) update( ret , dp[N][i][j] ) ;
	return ret;
}
int main(int argc, char *argv[]){
	//printf("Hello, world\n");

	int cases; cin >> cases; 
	FOR( tc , cases ){
		cin >> N ;
		A.clear();
		FOR( i , N ){
			string OorB; int button;
			cin >> OorB >> button;;
			A.push_back( MP(OorB[0] , button) ) ;
		}
		memset( dp , -1 , sizeof(dp));


		cout << "Case #" << tc+1 << ": " <<solve() << endl;
	}
	return 0;
}
