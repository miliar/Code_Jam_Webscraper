#include <iostream>
#include <stdio.h>
#include <map>
#include <vector>

using namespace std;

vector<int> a;
map<pair<int,int>, int> M;

int get_best(int b, int e) {
  if (b >= e) return 0;
  if (M.find(make_pair(b,e)) != M.end()) {
    return M[make_pair(b,e)];  
  }
  int best = -1;
  for (int i=0;i<a.size();++i) {
    if (a[i] < b || a[i] > e) continue;
    int l1 = get_best(b,a[i]-1);
    int l2 = get_best(a[i]+1,e);
    int cur = l1 + l2 + e - b;
    if (best == -1 || cur < best) {
      best = cur;
    }
  }
  if (best == -1) {
    best = 0;e - b + 1;
  }
  //  printf("%d %d %d\n",b,e,best);
  return M[make_pair(b,e)] = best;
}

int main() {
    freopen("c.in","r",stdin);
    freopen("c.solout","w",stdout);
  int T;
  scanf("%d\n",&T);
  for (int i=1;i<=T;++i) {
    int p,q;
    a.clear();
    M.clear();
    scanf("%d %d\n",&p,&q);
    int cur;
    for (int j=0;j<q;++j) {
      scanf("%d",&cur);
      a.push_back(cur);
    }
    sort(a.begin(),a.end());
    int res = get_best(1,p);
    printf("Case #%d: %d\n",i,res);
  }
  return 0;
}
