#include <cstdio>
#include <vector>

struct node {
  bool leaf;
  bool and_gate;
  bool one;
  bool change;
  int cheapest0;
  int cheapest1;
};

int main()
{
  int N;
  scanf("%d", &N);
  for(int nc = 1; nc <= N; ++nc) {
    int M, V;
    scanf("%d%d", &M, &V);
    std::vector<struct node> v(M);
    for(int i=0; i<(M-1)/2; ++i) {
      int G, C;
      scanf("%d%d", &G, &C);
      v[i].leaf = false;
      v[i].and_gate = (G==1);
      v[i].change = (C==1);
    }
    for(int i=(M-1)/2; i<M; ++i) {
      int I;
      scanf("%d", &I);
      v[i].leaf = true;
      v[i].one = (I==1);
    }
    for(int i=M-1; i>=0; --i) {
      if(v[i].leaf) {
	v[i].cheapest0 = v[i].cheapest1 = 1000000;
	if(v[i].one)
	  v[i].cheapest1 = 0;
	else
	  v[i].cheapest0 = 0;
      } else {
	if(v[i].and_gate) {
	  v[i].cheapest0 = v[2*i+1].cheapest0 <? v[2*i+2].cheapest0;
	  v[i].cheapest1 = v[2*i+1].cheapest1 + v[2*i+2].cheapest1;
	  if(v[i].change)
	    v[i].cheapest1 <?= (v[2*i+1].cheapest1<?v[2*i+2].cheapest1)+1;
	} else {
	  v[i].cheapest0 = v[2*i+1].cheapest0 + v[2*i+2].cheapest0;
	  v[i].cheapest1 = v[2*i+1].cheapest1 <? v[2*i+2].cheapest1;
	  if(v[i].change)
	    v[i].cheapest0 <?= (v[2*i+1].cheapest0<?v[2*i+2].cheapest0)+1;
	}
      }
    }
    int cost;
    if(V)
      cost = v[0].cheapest1;
    else
      cost = v[0].cheapest0;
    if(cost >= 1000000)
      printf("Case #%d: IMPOSSIBLE\n", nc);
    else
      printf("Case #%d: %d\n", nc, cost);
  }
  return 0;
}
