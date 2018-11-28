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
template<class T> void checkmin(T& a,T b){if(a>b)a=b;}
template<class T> void checkmax(T& a,T b){if(a<b)a=b;}
template<class T> T gcd(T a,T b){return b?gcd(b,a%b):a;}

const double EPS=(1e-10);
const int INF = (1<<29);
const LL  LINF = (1LL<<60);
const int MAXN = 30+10 ;


set<char> opp[ MAXN ] ;
char com[MAXN][MAXN];
string word;
int C , D , N;
void input(){
	cin >> C ;
	memset( com , 0 , sizeof(com) ) ;
	FOR( i , C ){
		cin >> word;
		assert( SIZE(word) == 3 ) ;
		assert( com[ word[0] - 'A' ][ word[1] - 'A' ] == 0 && com[ word[1] - 'A' ][ word[0] - 'A' ] == 0 );
		com[ word[0] - 'A' ][ word[1] - 'A' ] = word[ 2 ] ;
		com[ word[1] - 'A' ][ word[0] - 'A' ] = word[ 2 ] ;
	}
	cin >> D ;
	FOR( i , MAXN ) opp[i].clear();
	FOR( i , D ){
		cin >> word;
		assert( SIZE(word) == 2 );
		opp[ word[0] - 'A' ].insert( word[1] ) ;
		opp[ word[1] - 'A' ].insert( word[0] ) ;
	}

	cin >> N >> word ;
	
}
vector<char> List;
void output();
void solve(){
	List.clear();
	//cout << opp[ 'Q' - 'A' ].size() << endl;
	FOR( i , SIZE(word) ) {
		char c;
		if( SIZE(List) && ( c = com[ List.back() - 'A' ][ word[i] - 'A' ] ) ){
			List.pop_back();
			List.push_back( c );
		}else{
			List.push_back( word[i] ) ; 
			FOR( j , SIZE(List) - 1 ){
				//cout << word[i] << " " << List[i] << " " << ( opp[ word[i] - 'A' ].find( List[i] )  != opp[ word[i] - 'A' ] .end() ? "true" : "false")<< endl;
				if( opp[ word[i] - 'A' ].find( List[j] ) != opp[ word[i] - 'A'].end() ){
					//cout << "find" << endl;
					List.clear();
					break;
				}
			}
		}
		//output();
	}
}
void output(){
	cout << "[";
	FOR( i , SIZE(List) ){
		if( i ) cout << ", ";
		cout << List[i] ;
	}
	cout << "]" << endl;
}
void output();
int main(int argc, char *argv[]){
	int cases; cin >> cases; 
	FOR( tc , cases ){
		input();
		solve();
		cout << "Case #" << tc+1 << ": " ;
		output();
	}
	return 0;
}
