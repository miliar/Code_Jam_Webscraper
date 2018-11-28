#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define sqr(_a) ((_a) * (_a))
#define syso system("pause")

using namespace std;

/*
	on left or on right side of line, or on line
	0 - line
	< 0 - left
	> 0 - right
	
	(x, y) is check point
	(p1, q1) and (p2, q2) are points on line 
*/
long long lambda(long long x, long long y, long long p1, long long q1, long long p2, long long q2){
  return (q2 - q1) * x - (p2 - p1) * y + q1 * p2 - p1 * q2;
}

bool g[100][100];

int dp[1 << 17], poss[1 << 17], idxes[100], cntIdxes;

int memo(int mask){
  if (!mask)
    return 0;
    
  int &ret = dp[mask];
  if (ret != -1)
    return ret;
    
  ret = 1 << 20;

  bool ok;
  for(int a = mask; ; a = (a - 1) & mask) {
    if (poss[a] == -1){
      cntIdxes = 0;
      FOR (i, 16)
        if (a & (1 << i))
          idxes[cntIdxes++] = i;
      ok = true;
      FOR (i, cntIdxes){
        ffor (j, i + 1, cntIdxes)
          if (!g[idxes[i]][idxes[j]]){
            ok = false;
            break;
          }
        if (!ok)
          break;
      }
      
      if (ok)
        poss[a] = 1;
      else
        poss[a] = 0;
    }
    
    if (poss[a])
      ret <?= 1 + memo(mask ^ a);
    if(!a)
      break;
  }
  
  return ret;
}

int main(){
  freopen("Cs.out","wt", stdout);
  freopen("Cs.in","r", stdin);
  int tests, n, k;
  scanf("%d\n", &tests);
  FOR (test, tests){
    scanf("%d %d", &n, &k);
    int val[n][k];
    FOR (i, n)
      FOR (j, k)
        scanf("%d", &val[i][j]);
        
    FOR (i, n)
      ffor (j, i + 1, n){
        bool ok = true;
        FOR (s, k - 1){
          ok &= (lambda(s, val[j][s], s, val[i][s], s + 1, val[i][s + 1]) *
                lambda(s + 1, val[j][s + 1], s, val[i][s], s + 1, val[i][s + 1]) > 0);
          if (!ok)
            break;
        }
        
        g[i][j] = g[j][i] = ok;
      }
    int ret = 0;
    SET(dp, 255);
    SET(poss, 255);
    
    printf("Case #%d: %d\n", test + 1, memo((1 << n) - 1));
  }
  
  return 0;
}
