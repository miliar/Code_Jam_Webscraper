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

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=0; t<tn; t++){
    int n, k;
    scanf("%d%d", &n, &k);
    printf("Case #%d: %s\n", t+1, (k % (1<<n) == ((1<<n)-1)) ? "ON" : "OFF");
  }
  return 0;
}
