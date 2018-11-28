#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <cstdlib>
using namespace std;

int n, k;
char str[50100], nstr[50100];
int perm[20];

int main(){
  freopen("d.in", "r", stdin);
  freopen("d.out", "w", stdout);
  int tn, tst;
  scanf("%d", &tn);
  for (tst=1; tst<=tn; tst++){
    printf("Case #%d: ", tst);
    scanf("%d\n", &k);
    gets(str);
    n = strlen(str);
    int i, j, ans = 50100;
    for (i=0; i<k; i++) perm[i] = i;
    memset(nstr, 0, sizeof(nstr));
    do{
      for (i=0; i<n; i+=k){
        for (j=0; j<k; j++){
          nstr[i + j] = str[i + perm[j]];
        }
      }
      //printf("%s\n", nstr);
      int cans = 0;
      for (i=1; i<=n; i++){
        if (nstr[i] != nstr[i-1]) cans++;
      }
      if (cans < ans) ans = cans;
    }while (next_permutation(perm, perm+k));
    printf("%d\n", ans);
  }
  return 0;
}