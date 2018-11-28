#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <sstream>
#include <cassert>
#include <queue>
#include <map>
#include <queue>
#include <set>
#include <algorithm>
#include <math.h>

#define GI ({int y;scanf("%d",&y);y;})
#define REP(i,N) for(int i = 0;i<(N);i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i )
#define LET(x,a) __typeof(a) x(a)
#define sz size()
#define cs c_str()
#define REPV(i,ar) for(int i = 0;i<int((ar).size());i++)
#define EACH(it,mp) for(__typeof(mp.begin()) it(mp.begin());it!=mp.end();it++)
#define pb push_back
#define sor(ar) sort(ar.begin(),ar.end())
#define LINF (1e18)
#define INF (1<<30)
#define rev(ar) reverse(ar.begin(),ar.end())
using namespace std;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long int LL;

int N;
char Buffer[128];
int Seen[1024][1024], Seenid ;

int main(){
	int T = GI;	
	freopen("some.out","w",stdout);
	FOR(tt,1,T) {
		map<string,int> Id;
		vector<int> V;	
		int N = GI;getchar();
		REP(i,N){
			gets(Buffer),Id[ Buffer ] = i;
		}
		int R = GI;
		if( R ) getchar();		
		REP(i,R) gets(Buffer),V.pb( Id[Buffer] );
				
		vector<int> Pos[N];
		REP(i,V.sz) Pos[V[i]].pb( i );
		REP(i,N) Pos[i].pb(INT_MAX);
		
		queue< pair<PII,int> > Q;
		Q.push( make_pair(PII(-1,0),-1) );
		if( R == 0 ) printf("Case #%d: %d\n",tt,0); 
		else { 
			++Seenid;
			while( Q.sz ){
				int start = Q.front().first.first, p = Q.front().first.second;
				int cost = Q.front().second;
				Q.pop();			
				if( start > -1 ) {
					if( Seen[start][p] == Seenid ) continue; 
					Seen[ start ][ p ] = Seenid;
				}				
				if( p == INT_MAX ) { printf("Case #%d: %d\n",tt,cost); break; }			
				REP(i,N) if( i != start ) REPV(j,Pos[i]) {
					int prev = ( j == 0 ? -1 : Pos[i][j-1] );					
					if( p > prev && p < Pos[i][j] ) Q.push( make_pair( PII(i,Pos[i][j]) , cost+1 ) );				
				}		
			}
		}
	}
	return 0;
}