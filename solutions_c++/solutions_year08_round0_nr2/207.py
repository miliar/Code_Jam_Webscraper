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

int get_time(){
	static char buffer[16];
	scanf("%s",buffer);
	int a,b;
	sscanf(buffer,"%02d:%02d",&a,&b);
	return a*60 + b;
}

#define ENTERA(t) (2*t)
#define LEAVEA(t) (2*(t)+1)
#define ENTERB(t) (2*NA+2*(t))
#define LEAVEB(t) (2*NA+2*(t)+1)

int Cap[512][512], Seen[512], Seenid , Source, Sink ,NA , NB;
VI Gr[512];


vector<int> PATH;
void printVERTEX( int a ) ;
vector< PII> A,B;

int go( int v , int flow ) {
	if( Seen[ v ] == Seenid ) return 0;
	Seen[v] = Seenid;
	PATH.pb( v );
	if( v == Sink ){
		//EACH(it,PATH) printVERTEX(*it), cout << " :-> ";
		//puts("");
		return INT_MAX;
	}	
	int ret;
	EACH(it,Gr[v]) 
		if( Cap[v][*it] > 0 ){
		int x = min( flow , Cap[v][*it] );
		if( (ret=go(*it,x)) > 0 ) {
			Cap[v][*it]--;
			Cap[*it][v]++;
			PATH.pop_back();
			return ret;
		}
	}
	PATH.pop_back();
	return 0;
}

void printVERTEX( int a ) {
	if( a == Sink ) cout << "Sink";
	else if( a == Source ) cout << "Source" ;
	else if( a < 2*NA ) cout << A[a/2].first/60 <<":"<<A[a/2].first%60 << ( a%2 ? "(LeaveA) " : "(FromA)");
	else if( a >= 2*NA ) cout << B[(a-2*NA)/2].first/60 <<":"<<B[(a-2*NA)/2].first%60 <<( a%2 ? "(LeaveB) " : "(FromB)");
}

void print( int a , int b ) {
	cout << " Edge from : ";
	printVERTEX( a ); 
	cout <<"  -> ";
	printVERTEX( b );
	puts("");
	
}

int main(){
	int T = GI;
	freopen("train.out","w",stdout);
	FOR(tt,1,T){		
		int turn = GI;
		NA = GI,NB = GI;
		A.clear();B.clear();
		REP(i,NA+NB) {
			int start = get_time(), end = get_time();
			PII p(start,end);
			if( i < NA ) A.pb( p );
			else B.pb( p );					
		}
		Source = 2*(NA + NB);
		Sink = Source + 1;
		REP(i,Sink+1) Gr[i].clear();
		memset( Cap, 0 , sizeof( Cap ) );
		
		#define EDGE(a,b) Gr[a].pb( b ), Gr[b].pb( a ), Cap[a][b]++
		REP(i,NA) {
			EDGE(Source,ENTERA(i));
			EDGE(LEAVEA(i),Sink);
		}
		REP(i,NB){
			EDGE(Source,ENTERB(i));
			EDGE(LEAVEB(i),Sink);
		}	
		REP(i,A.sz) REP(j,B.sz) if( B[j].first >= A[i].second + turn ){
			EDGE(ENTERA(i),LEAVEB(j));
		}
		REP(i,B.sz) REP(j,A.sz) if( A[j].first >= B[i].second + turn ) {
			EDGE(ENTERB(i),LEAVEA(j));
		}
		
		do ++Seenid,PATH.clear(); while( go(Source,INT_MAX) );
		
		int ansA = 0,ansB = 0;
		REP(i,NA) ansA += Cap[Sink][LEAVEA(i)];
		REP(i,NB) ansB += Cap[Sink][LEAVEB(i)];
		printf("Case #%d: %d %d\n",tt,NA-ansA,NB-ansB);		
	}
	return 0;
}