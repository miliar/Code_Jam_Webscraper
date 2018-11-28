#include <vector>
#include <List>
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
#include <cassert>
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
typedef vector<int> VI;
template<class T> void checkmin(T& a,T b){if(a>b)a=b;}
template<class T> void checkmax(T& a,T b){if(a<b)a=b;}
template<class T> T gcd(T a,T b){return b?gcd(b,a%b):a;}

const double EPS=(1e-10);
const int INF = (1<<29);
const LL  LINF = (1LL<<60);
const int MAXN = 1000+10 ;

int A[ MAXN ] ;
int bitct[ 20 + 5 ];
int N ;
void input(){
	cin >> N ;
	FOR( i , N ) cin >> A[i] ;
}
int Add( VI& S , int& s ){
	int ret = 0 ;
	FOR( i , SIZE(S) ){
		ret ^= S[i] ;
		s += S[i] ;
	}
	return ret;
}
void solve(){
	fill( bitct , bitct + 20 , 0 ) ;
	FOR( i , N ){
		FOR( k , 20 )if( A[i] & ( 1 << k ) )
			bitct[ k ] ++ ;
	}
	FOR( k , 20 ) if( bitct[k]&1 ){
		cout << "NO" << endl;
		return;
	}
	sort( A , A+N ) ;
	cout << accumulate(A+1 , A+N , 0 ) <<endl;
}
void output(){
	
}
void output();
int main(int argc, char *argv[]){
	int cases; cin >> cases; 
	FOR( tc , cases ){
		cout << "Case #" << tc+1 << ": " ;
		input();
		solve();
		
		output();
	}
	return 0;
}
