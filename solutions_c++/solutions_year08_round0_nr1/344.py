#include <cstdio>
#include <map>
#include <string>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,v) FOR(i,(int)v.size())
#define BEND(v) v.begin(),v.end()

int S,Q;
int cas = 0;
string getit() {
  char buf[128];
  fgets(buf,sizeof(buf),stdin);
  assert(buf[strlen(buf)-1] == '\n');
  return string(buf);
}
int qs[1024];
void doit() {
  scanf("%d",&S);
  getit();
  map<string,int> ss;
  FOR(i,S) {
    ss[getit()] = i;
  }
  scanf("%d",&Q);
  getit();
  FOR(i,Q) {
    qs[i] = ss[getit()];
  }

  int dp[128][1024]={};

  const int inf = 123456789;
  int ans = inf;
  for (int q = Q-1; q >= 0; q--) {
    FOR(s,S) {
      dp[s][q] = inf;
      if (s != qs[q]) {
	FOR(s2,S) {
	  dp[s][q] <?= (s!=s2) + dp[s2][q+1];
	}
      }
    }
  }
  FOR(s,S) ans <?= dp[s][0];

  printf("Case #%d: %d\n",++cas,ans);
}

int main() {
  int N;
  scanf("%d",&N);
  FOR(i,N) doit();
}
