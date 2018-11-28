#include<cstdio>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
using namespace std;
int n;
int used[1024];
vector<pair<int, int> > dat;
int main() {
  int e = 0, T;
  scanf("%d",&T);
  int ans;
  while(T--) {
    ans = 0;
    printf("Case #%d: ", ++e);
    scanf("%d",&n);
    dat.clear();
    for(int i = 0; i < n; ++i) {
      int x, y;
      scanf("%d%d",&x,&y);
      dat.push_back(make_pair(y, x));      
      used[i] = 0;
    }
    sort(dat.begin(), dat.end());
    /*
    for(int i = 0; i < n; ++i) 
      printf("[%d %d]\n", dat[i].first, dat[i].second);
    printf("\n");
    */
    int cnt = 0;
    int prog = 0;
    while(1) {
      for(int i = 0; i < n; ++i) {
        if(used[i] == 2) continue;
        if(dat[i].first <= cnt) {
          if(used[i] == 1) cnt++;
          else cnt+= 2;
          used[i] = 2;
          ans++;
          prog = 1;
        }
      }
      for(int i = n-1; i>=0; --i) {
        if(used[i] >= 1) continue;
        if(dat[i].second <= cnt) {
          used[i] = 1;
          cnt++;
          ans++;
          prog = 1;
          break;
        }
      }
      if(prog == 0) break;
      prog = 0;
    }
    if(cnt != n*2) ans = -1;
    if(ans == -1)
      printf("Too Bad\n");
    else
      printf("%d\n", ans);
  }
  return 0;
}
