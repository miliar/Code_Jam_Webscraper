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

const int MAX = 100;

int n;
int b;
int ans;
int digs[MAX][MAX];
int lens[MAX];

void go(int pos, int need, int cnum){
  if (need == 0){
    ans++;
    return;
  }
  for (int c=cnum; c<=need; c++){
    int cc = c, ok = 1, clen = 0;
    while (cc > 0 && ok){
      digs[pos][clen] = cc % b;
      cc /= b;
      for (int j=0; j<pos; j++){
        ok &= ((digs[j][clen] != digs[pos][clen]) || (clen >= lens[j]));
      }
      clen++;
    }
    lens[pos] = clen;
    if (ok){
      go(pos + 1, need - c, c + 1);
    }
  }
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn;
  scanf("%d\n", &tn);
  for(int t=1; t<=tn; t++){
    printf("Case #%d: ", t);
    scanf("%d%d", &n, &b);
    ans = 0;
    go(0, n, 1);
    printf("%d\n", ans);
  }
  return 0;
}
