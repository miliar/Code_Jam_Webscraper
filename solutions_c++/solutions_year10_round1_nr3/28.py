#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

const int MAX = 1<<20;
int val[MAX];

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  val[1] = 2;
  val[2] = 4;
  val[3] = 5;
  for (int i=4; i<MAX; i++){
    val[i] = val[i-1] + 2 - (val[val[i-1] + 1 - i] > i);
  }
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    int a1, a2, b1, b2;
    long long ans = 0;
    scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
    for (int i=a1; i<=a2; i++){
      ans += max(0, b2 - max(b1, val[i]) + 1);
    }
    for (int i=b1; i<=b2; i++){
      ans += max(0, a2 - max(a1, val[i]) + 1);
    }
    printf("Case #%d: %I64d\n", t, ans);
  }
  return 0;
}
