#include <iostream>
#include <vector>

using namespace std;

#define REP(i,N) for( int i = 0;i < N;i++ )
#define FOR(i,a,b) for( int i = (a);i <= (b);i++ )
#define REPV(i,V) REP(i,V.sz)
#define sor(a) sort(a.begin(),a.end())
#define VI vector<int>
#define VS vector<string>
#define pb push_back
#define MEM(a) memset(a,0,sizeof(a))
#define sz size()
#define PII pair<int,int>
#define MAX (int)(1<<30)
#define rev(a) reverse(a.begin(),a.end())
#define LL long long
#define GI ({int t;scanf("%d",&t);t;})

int main(){

	int T = GI;
	REP(t,T){
		int N = GI,C = GI,seen[2200];
		vector<PII>V[C];
		bool isposs = true;
		REP(i,C)V[i].clear();
		
		REP(i,C){
			int n = GI;
			MEM(seen);
			REP(j,n){
				int a,b;
				scanf("%d %d",&a,&b);
				a--;
				if( seen[a] ){ 
					REPV(k,V[i])if( V[i][k].first == a ){V[i][k].second=min(V[i][k].second,b);}
				}
				
				else {
					V[i].pb(PII(a,b));
					seen[a] = 1;
				}
			}
		}
		
		
		
		int marked[N];
		MEM(marked);
		REP(i,C) if( V[i].sz == 1 && V[i][0].second == 1 )marked[V[i][0].first] = 1; 
		
		REP(kk,10)
			REP(i,C){
				bool flag = false;
				REPV(j,V[i])
					if( V[i][j].second == marked[V[i][j].first] ){flag = true; break;}
				
				if( !flag ){
					
					REPV(j,V[i])
						if( V[i][j].second == 1 ) { marked[V[i][j].first] = 1; flag = true; break; }
				
				}	
				
				if( !flag ) {isposs = false; goto a; }
			}	
			a:
			if( !isposs ) printf("Case #%d: IMPOSSIBLE\n",t+1);
			else {
			printf("Case #%d: ",(t+1)); 	
			REP(i,N)
				if( i== (N-1) )printf("%d\n",marked[i]); 	
				else printf("%d ",marked[i]); 	
			}
	}
	

return 0;
}
