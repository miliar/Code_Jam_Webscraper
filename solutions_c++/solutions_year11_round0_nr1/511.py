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

int n;

const int MAXN = 103;

char seq[MAXN];
int pos[MAXN];

int dp[MAXN][MAXN][MAXN];

const int INF = 1 << 20;

int memo(int p1, int p2, int idx){
  if (idx == n)
    return 0;
  if (p1 < 1 || p2 < 1)
    return INF;
  
  if (p1 > 100 || p2 > 100)
    return INF;
    
  int &ret = dp[p1][p2][idx];
  if (ret != -1)
    return ret;
    
  ret = 1 << 20;
  
  int p = pos[idx];
  bool id = seq[idx] == 'B'; // B is the 2nd value
  int os[3] = {p1, p2, idx};
  int ns[3];
  for (int i = -1; i < 2; i++){
    ns[0] = os[0];
    ns[1] = os[1];
    ns[2] = os[2];
    ns[1 - id] += i;
    if (os[id] == p)
      ns[2]++;
    else if (os[id] < p)
      ns[id]++;
    else
      ns[id]--;
      
    ret <?= 1 + memo(ns[0], ns[1], ns[2]);
  }
  
  return ret;
}

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests;
  cin >> tests;
  scanf("\n");
  
  FOR (test, tests){
    cin >> n;
    FOR (i, n)
      cin >> seq[i] >> pos[i];
    SET(dp, 255);
    cout << "Case #" << (test + 1) << ": ";
    cout << memo(1, 1, 0) << "\n";
  }
  return 0;
}
