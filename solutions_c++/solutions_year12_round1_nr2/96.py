#include <set>
#include <cstdio>
#include <algorithm>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

int main(){
  int t = getInt();
  REP(cc, t){
    int n = getInt();
    vector<pair<int, int> > v(n);
    vector<int> use(n);
    int ans = 0;

    REP(i,n){
      v[i].first  = getInt();
      v[i].second = getInt();
    }

    REP(i,n) swap(v[i].first, v[i].second);
    sort(v.begin(), v.end());
    REP(i,n) swap(v[i].first, v[i].second);

    int cnt = 0;

    while(cnt != n + n){
      REP(i,n) if(use[i] != 2 && v[i].second <= cnt){
	cnt += 2 - use[i];
	use[i] = 2;
	goto next;
      }

      for(int i = n - 1; i >= 0; i--){
	if(use[i] == 0 && v[i].first <= cnt){
	  cnt += 1;
	  use[i] = 1;
	  goto next;
	}
      }

      break;
    next:;
      ans++;
    }

    printf("Case #%d: ", cc + 1);
    if(cnt == n + n)
      printf("%d\n", ans);
    else
      puts("Too Bad");
  }
  return 0;
}
