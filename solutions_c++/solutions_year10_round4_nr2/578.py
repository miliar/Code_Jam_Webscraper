#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>
#include <string>
#include <sstream>
#include <vector>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")
#define mp make_pair

using namespace std;

int prices[2000][20];
int M[10000];
int dp[1 << 12][11][20];
int p, n;

const int INF = (1 << 29) - 10;

int memo(int idx, int stage, int taken){
  if (stage < 0){
    if (taken >= p - M[idx])
      return 0;
    return INF;
  }
  
  int &ret = dp[idx][stage][taken];
  if (ret != -1)
    return ret;
    
  ret = INF;
  ret <?= memo(idx * 2, stage - 1, taken) + memo(idx * 2 + 1, stage - 1, taken);
  if (ret > INF)
    ret = INF;
  ret <?= memo(idx * 2, stage - 1, taken + 1) + memo(idx * 2 + 1, stage - 1, taken + 1) + prices[idx][stage];
  if (ret > INF)
    ret = INF;
  
  return ret;
}

int main(){
  freopen("Bl.out","wt", stdout);
  freopen("Bl.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    SET(dp, 255);
    cin >> p;
    n = 1 << p;
    FOR (i, n)
      cin >> M[i];

    int pp = n >> 1, idx = 0;
    while (pp){
      FOR (i, pp)
        cin >> prices[i][idx];
      idx++;
      pp >>= 1;
    }
    
    cout << "Case #" << (test + 1) << ": ";
    cout << memo(0, p - 1, 0) << "\n";
  }
  return 0;
}
