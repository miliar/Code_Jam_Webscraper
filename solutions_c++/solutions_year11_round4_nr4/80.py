#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

const int N=1000;
int _,n,m,a,b,ans,d[N],thr[N];
vector<int> adj[N];

void rek(int v, int ile) {
   if (v==1) ans = max(ans,ile);
   else {
      FORE(i,adj[v])
	 if (++thr[*i]==1) ++ile;
      FORE(i,adj[v]) if (d[*i]==d[v]+1) {
	 rek(*i, ile);
      }
      FORE(i,adj[v])
	 if (thr[*i]--==1) --ile;
   }
}

int main() {
   scanf("%d",&_);
   REP(test,_) {
      scanf("%d%d",&n,&m);
      REP(i,m) {
	 scanf("%d,%d",&a,&b);
	 adj[a].push_back(b);
	 adj[b].push_back(a);
      }
      REP(i,n) d[i]=1000000; d[0]=0;
      queue<int> q; q.push(0);
      while (!q.empty()) {
	 int v = q.front(); q.pop();
	 FORE(i,adj[v]) if (d[*i]==1000000)
	    d[*i]=d[v]+1, q.push(*i);
      }
//      REP(i,n) printf("%d:%d ",i,d[i]); puts("");
      thr[0]=100;
      ans=0;
      rek(0,0);

      printf("Case #%d: %d %d\n",test+1,d[1]-1,ans  - (d[1]-1) );
      REP(i,n) adj[i].clear();
   }
}
