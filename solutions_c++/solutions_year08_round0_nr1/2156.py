#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define REP(i,N) for( int i = 0;i < N;i++ )
#define FOR(i,a,b) for( int i = (a);i <= (b);i++ )
#define VI vector<int>
#define sz size()
#define pb push_back
#define GI ({int t;scanf("%d",&t);t;})
#define REPV(i,V) REP(i,V.sz)
#define EACH(it,mp) for( __typeof(mp.begin)it = mp.begin();it!=mp.end();it++ )
#define sor(a) sort(a.begin(),a.end())
#define rev(a) reverse(a.begin(),a.end())
#define INF (int)(1<<30)
#define VS vector<string>

typedef long long LL;


int main(){

	int T = GI;
	REP(t,T){
		int S = GI;

		char s[128],ch = getchar();
		REP(k,S) {  cin.getline(s,125); }

		int Q = GI,ret = 0;
		ch = getchar();
		set<string>Server;

		REP(q,Q){
			cin.getline(s,125);
			string ss = (string)s;
			Server.insert(ss);
			if(Server.sz == S ) { ret++; Server.clear(); Server.insert(ss);}
			
		}
		printf("Case #%d: %d\n",(t+1),ret);


	}


return 0;
}
