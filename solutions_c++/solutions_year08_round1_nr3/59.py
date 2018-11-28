#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <cmath>

char res[35][10] = {
"000",
"000", "027", "143", "751", "935", "607", "903", "991", "335", "047",
"943", "471", "055", "447", "463", "991", "095", "607", "263", "151",
"855", "527", "743", "351", "135", "407", "903", "791", "135", "647"};

int main(){
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    int n;
    scanf("%d", &n);
    printf("Case #%d: %s\n", t, res[n]);
  }
  return 0;
}