#include <stdio.h>

void readch(int n) {
     char ch;
     for (int i = 0; i < n; ++i)
          scanf("%c", &ch);
}

int n;
char num[30];

void init() {
   n = 0;
   char ch;
   do {
       scanf("%c", &ch);
       if (ch < '0' || ch > '9') break;
//       num[n++] = ((int) ch) - 48;
       num[n++] = ch;
   }  while (true);
// m
   readch(0);
/*   printf("hello: %d  ", n);
   for (int i = 0; i < n; ++i)
     printf("%c", num[i]);
   printf("\n");
*/
}

void solve() {
  if (n == 1) {
     printf("%c0", num[0]);
     return;
  }
  int i = n - 2;
  while (i >= 0 && num[i] >= num[i+1]) --i;
  if (i < 0) {
     for (i = n - 1; i >= 0; --i)
       if (num[i] != '0') break;
     printf("%c0", num[i]);
     for (int k = n - 1; k >= 0; --k)
       if (k != i)
              printf("%c", num[k]);
     return;
  }
  int j;
  for (j = n - 1; j > i; --j)
    if (num[j] > num[i]) break;
  for (int k = 0; k < i; ++k)
    printf("%c", num[k]);
  printf("%c", num[j]);
  for (int k = n - 1; k > j; --k)
    printf("%c", num[k]);
  printf("%c", num[i]);
  for (int k = j - 1; k > i; --k)
    printf("%c", num[k]);
}

int main() {
    int nt;
    scanf("%d", &nt);
// m
    readch(1);
    for (int i = 0; i < nt; ++i) {
        init();
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }
}
