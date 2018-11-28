#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int read_time(){
  int h, m;
  scanf("%d:%d", &h, &m);
  return h * 60 + m;
}

void solve(){
  int t, na, nb;
  scanf("%d%d%d", &t, &na, &nb);
  int n = na + nb;
  vector<pair<int, int> > v;
  for(int i = 0; i < n; ++i){
    int id = (i < na ? 1 : 2);
    int other = (i < na ? 2 : 1);
    int d = read_time();
    int r = read_time() + t;
    v.push_back(make_pair(d, id));
    v.push_back(make_pair(r, -other));
  }
  sort(v.begin(), v.end());
  int ct[] = {0,0,0};
  int res[] = {0,0,0};
  for(int i = 0; i < n * 2; ++i){
    int id = v[i].second;
    if(id < 0){
      ++ct[-id];
    }else{
      if(ct[id] <= 0){
        ++res[id];
      }else{
        --ct[id];
      }
    }
  }
  printf("%d %d\n", res[1], res[2]);
}

int main(){
  int t;
  scanf("%d", &t);
  for(int c = 0; c < t; ++c){
    printf("Case #%d: ", c+1);
    solve();
  }
}
