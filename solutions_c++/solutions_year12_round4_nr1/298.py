#include <set>
#include <cstdio>
#include <queue>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

inline int getInt(){ int s; scanf("%d", &s); return s; }

using namespace std;

int main(){
  int t = getInt();

  REP(cc, t){
    int n = getInt();

    vector<int> d(n);
    vector<int> l(n);

    REP(i,n){
      d[i] = getInt();
      l[i] = getInt();
    }

    int D = getInt();

    vector<int> dp(n);

    dp[0] = d[0];

    bool ans = false;

    REP(i,n){
      int len = dp[i];

      if(d[i] + len >= D) ans = true;

      for(int j = i + 1; j < n; j++){
	int ln = d[j] - d[i];
	if(len >= ln){
	  dp[j] = max(dp[j], min(ln, l[j]));
	}else{
	  break;
	}
      }
    }

    printf("Case #%d: %s\n", cc + 1, ans ? "YES" : "NO");
  }

  return 0;
}
