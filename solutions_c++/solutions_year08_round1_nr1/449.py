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
		int N = GI;
		vector<LL> A,B;
		REP(n,N){
			LL aa;scanf("%lld",&aa);
			A.pb(aa);
		}
		REP(n,N){
			LL bb;scanf("%lld",&bb);
			B.pb(bb);
		}
		
		LL ret = 0;
		sor(A);sor(B);	
		
		int inda = 0,indb = B.sz-1;
		while( (inda < A.sz) && A[inda] < 0 ){
			ret+=A[inda]*B[indb];
			inda++;indb--;
		}
		inda = A.sz -1;indb = 0;
		while( (inda >=0) && A[inda] >=0 ){
			ret+=A[inda]*B[indb];
			inda--;indb++;
		}
		
		printf("Case #%d: %lld\n",t+1,ret);
	}

return 0;
}
