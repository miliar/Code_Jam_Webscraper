#include <cstdio>
#include <algorithm>
#include <map>
#include <queue>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

const int N=1024;
int _;
int n,a[N],ans;
char c[N];
map<int,int> d;

inline int code(int a, int b, int c) { return a + b*N + c*N*N; }
inline void decode(int d, int& a, int& b, int& c) { a=d%N, d/=N; b=d%N, d/=N; c=d%N; }

int main() {
   scanf("%d",&_);
   REP(test,_) {
      scanf("%d",&n);
      REP(i,n) scanf(" %c%d",&c[i],&a[i]), --a[i];
      queue<int> q;
      d.clear(); ans=-1;
      q.push(code(0,0,0)); d[code(0,0,0)] = 0;
      while (!q.empty()) {
	 int i,x,y; decode(q.front(),i,x,y);
	 if (i==n) { ans = d[q.front()]; break; }
	 REP(dx,4) REP(dy,4) {
	    int nx = dx==3 ? x : x+dx-1;
	    int ny = dy==3 ? y : y+dy-1;
	    if (nx < 0 || ny < 0 || nx >= 100 || ny >= 100) continue;
	    if (dx==3 && !(c[i]=='O' && a[i]==x)) continue;
	    if (dy==3 && !(c[i]=='B' && a[i]==y)) continue;
	    int v = code(i + (dx==3 || dy==3), nx, ny);
	    if (d.find(v)==d.end()) d[v] = d[q.front()] + 1, q.push(v);
	 }
	 q.pop();
      }
      printf("Case #%d: %d\n",test+1,ans);
      fflush(stdout);
   }
}
