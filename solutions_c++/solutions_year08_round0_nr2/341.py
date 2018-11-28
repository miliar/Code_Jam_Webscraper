#include <cstdio>
#include <map>
#include <string>
#include <vector>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,v) FOR(i,(int)v.size())
#define BEND(v) v.begin(),v.end()

int T,NA,NB;
int cas = 0;
int gett() {
  int h,m;
  scanf("%d:%d",&h,&m);
  return h*60+m;
}
int doit2(vector<int> starts, vector<int> ends) {
  int ne = 0;

  int req = 0;

  FORI(i,starts) {
    if (ne < (int)ends.size() && ends[ne]+T <= starts[i]) {
      ne++;
    } else {
      req++;
    }
  }
  return req;
}
void doit() {
  scanf("%d%d%d",&T,&NA,&NB);

  vector<int> as,ae,bs,be;
  FOR(i,NA) {
    int s = gett();
    int e = gett();
    as.push_back(s);
    be.push_back(e);
  }
  FOR(i,NB) {
    int s = gett();
    int e = gett();
    bs.push_back(s);
    ae.push_back(e);
  }
  sort(BEND(as));
  sort(BEND(ae));
  sort(BEND(bs));
  sort(BEND(be));

  printf("Case #%d: %d %d\n",++cas,doit2(as,ae),doit2(bs,be));
}

int main() {
  int N;
  scanf("%d",&N);
  FOR(i,N) doit();
}
