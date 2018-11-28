#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <string>
#include <ctime>
#include <climits>
#include <cassert>
#include <queue>

#define FOR(i,n) for(int i=0;i<n;i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define MP make_pair

using namespace std;

typedef long long LL;
typedef vector<int> VI;

template<class T> void checkmin(T& a,T b){if(a>b)a=b;}
template<class T> void checkmax(T& a,T b){if(a<b)a=b;}
LL gcd(LL a,LL b){return b?gcd(b,a%b):a;}



const int MAXN = 100000 + 10 ;
const int LIMIT = 1 << 10 ;
const int MOD = 1000000007;

typedef vector<pair<LL,int> > VP; 
typedef pair<int,int> PII;


#define LARGE_INPUT_FILE "A-large.in"
#define SMALL_INPUT_FILE "A-small-attempt0.in"
#define OUTPUT_FILE "out.out"




#define FILE_IN_OUT
#define LARGE
//#define DEBUG

int L[MAXN] , D[MAXN] ;
int N , DD ;
bool reach[MAXN] ;
int main(){

#ifdef FILE_IN_OUT
	#ifdef LARGE
		freopen( LARGE_INPUT_FILE,"r",stdin);
	#else
		freopen( SMALL_INPUT_FILE,"r",stdin);
	#endif
		
	freopen( OUTPUT_FILE,"w",stdout);
#endif
	
	int cases; cin >> cases;
	
	FORE( tc , 1  , cases ){
		cin >> N ;
		FOR( i , N ) cin >> D[i] >> L[i] ;
		cin >> DD;
		fill ( reach , reach + N+ 1 , false );
		
		queue<PII> Q ;
		Q.push(MP(0,D[0])) ;
		
		bool ok = false;
		if( D[0] + D[0] >= DD ) ok = true;
		for( int i = 1 ; i < N ; i ++ ){
			while( !Q.empty() &&  D[Q.front().first]+Q.front().second < D[i] ){
				Q.pop();
			}
			if(Q.empty()){
				break;
			}
			Q.push( MP(i , min( L[i] , D[i] - D[Q.front().first]) ) );
			if( D[i] + min( L[i] , D[i] - D[Q.front().first]) >= DD )
				ok = true;
		}
		printf("Case #%d: %s\n" , tc, ok ? "YES" : "NO" );

	}
	
}