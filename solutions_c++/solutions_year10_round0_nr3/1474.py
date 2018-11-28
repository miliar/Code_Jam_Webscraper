#include<cstdio>
#include<queue>

using namespace std;

struct group {
  int ct, idx;
};

int main()
{
  group G[1024];
  int earn[1024], next[1024];
  int T;
  scanf("%d", &T);
  for(int i=1; i<=T; ++i) {
    int R, k, N;
    queue<group> Q;
    scanf("%d%d%d", &R, &k, &N);
    for(int j=0; j<N; ++j) {
      int g;
      scanf("%d", &g);
      G[j].ct = g;
      G[j].idx = j;
      Q.push(G[j]); 
    }
    for(int j=0; j<N; ++j)
      earn[j] = -1;
    long long sol = 0;
    int loop = -1;
    for(int j=0; j<R; ++j) {
      if(earn[Q.front().idx] >= 0 && loop==-1) {
	int loopct = 1;
	long long get = earn[Q.front().idx];
	for(int p=next[Q.front().idx]; p!=Q.front().idx; p=next[p]) {
	  loopct++;
	  get += earn[p];
	}
	sol += (R-j)/loopct*get;
	j += (R-j)/loopct*loopct-1;
	loop=1;
	continue;
      }
      int fst = Q.front().idx;
      queue<group> reque;
      earn[fst] = 0;
      while(!Q.empty()) {
	if(earn[fst]+Q.front().ct > k) break;
	earn[fst] += Q.front().ct;
	reque.push(Q.front());
	Q.pop();
      }
      while(!reque.empty()) {
	Q.push(reque.front());
	reque.pop();
      }
      sol += earn[fst];
      next[fst] = Q.front().idx;
    }
    printf("Case #%d: %lld\n", i, sol);
  }
  return 0;
}
