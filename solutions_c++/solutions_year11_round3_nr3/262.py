#include <iostream>
#include <cstdlib>

int n, a[101];

bool ok(int f) {
  bool flag = true;

  for (int i = 0; i < n; i++)
    if (f % a[i] == 0 || a[i] % f == 0)
      continue;
    else {
      flag = false;
      break;
    }
  
  return flag;
}

int main() {
  int case_no, l, h, t, ans;
  
  scanf("%d", &t);
  for (case_no = 1; case_no <= t; case_no++) {
    scanf("%d%d%d", &n, &l, &h);
    for (int i = 0; i < n; i++)
      scanf("%d", &a[i]);
    
    for (ans = l; ans <= h; ans++)
      if (ok(ans))
        break;
      
    printf("Case #%d: ", case_no);
    if (ans == h + 1)
      puts("NO");
    else
      printf("%d\n", ans);
  }
  
  return 0;
}
