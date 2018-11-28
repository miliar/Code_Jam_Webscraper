#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

const int MID = 2500000;
const int MAX = 5000000;

int iter;
int hmuch[2][MAX];
int turn[MAX];
int q[MAX];
vector<int> v;

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn;
  scanf("%d\n", &tn);
  for(int t=1; t<=tn; t++){
    printf("Case #%d: ", t);
    int n;
    scanf("%d\n", &n);
    iter++;
    v.clear();
    for (int i=0; i<n; i++){
      int x, p;
      scanf("%d%d", &x, &p);
      x += MID;
      hmuch[0][x] = p;
      v.push_back(x);
      turn[x] = iter;
    }
    long long ans = 0;
    int lay = 0;
    bool ok = true;
    while (v.size() > 0 && ok){
      vector<int> w;
      iter++;
      lay = 1-lay;
      ok = false;
      for (int i=0; i<(int)v.size(); i++){
        int cx = v[i];
        int hm = hmuch[1-lay][cx];
        int nm = hm / 2;
        if (nm > 0){
          ok = true;
          ans += nm;
          if (turn[cx + 1] != iter){
            turn[cx + 1] = iter;
            hmuch[lay][cx+1] = 0;
          }
          hmuch[lay][cx + 1] += nm;
          if (q[cx + 1] != iter){
            w.push_back(cx + 1);
            q[cx + 1] = iter;
          }
          if (turn[cx - 1] != iter){
            turn[cx - 1] = iter;
            hmuch[lay][cx-1] = 0;
          }
          hmuch[lay][cx-1] += nm;
          if (q[cx - 1] != iter){
            w.push_back(cx - 1);
            q[cx - 1] = iter;
          }
        }
        if (hm & 1){
          if (turn[cx] != iter){
            turn[cx] = iter;
            hmuch[lay][cx] = 0;
          }
          hmuch[lay][cx] += 1;
          if (q[cx] != iter){
            w.push_back(cx);
            q[cx] = iter;
          }
        }
      }
      v = w;
    }
    printf("%I64d\n", ans);
  }
  return 0;
}
