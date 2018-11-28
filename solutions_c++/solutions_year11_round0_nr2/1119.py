#include <cstdio>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <sstream>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int n, tn, nt;
char s[1000];

int a[256][256];
int was[256];
int op[256];

int main(void)
{
   freopen("B-small-attempt1.in", "r", stdin);
   freopen("B-small-attempt1.out", "w", stdout);
//   freopen("B-large.in", "r", stdin);
//   freopen("B-large.out", "w", stdout);

   scanf("%d", &nt);
   for (tn=0; tn<nt; tn++)
   {
      fprintf(stderr, "Case #%d: \n", tn+1);
      memset(a, 0, sizeof(a));
      memset(op, 0, sizeof(op));
      memset(was, 0, sizeof(was));

      printf("Case #%d: ", tn+1);

      scanf("%d", &n);
      for (int i=0; i<n; i++) {
        scanf("%s", s);
        a[s[0]][s[1]] = s[2];
        a[s[1]][s[0]] = s[2];
      }

      scanf("%d", &n);
      for (int i=0; i<n; i++) {
        scanf("%s", s);
        op[s[0]] = s[1];
        op[s[1]] = s[0];
      }

      scanf("%d", &n);
      scanf("%s", s);
      int j = 0;
      for (int i=0; i<n; i++) {
        s[j++] = s[i];
        was[s[i]]++;
        if (j >= 2 && a[s[j-1]][s[j-2]]) {
          was[s[j-1]]--;
          was[s[j-2]]--;
          
          s[j-2] = a[s[j-1]][s[j-2]];
          j--;
          was[s[j-1]]++;
        }
        if (j >= 1 && was[op[s[j-1]]]) {
          memset (was, 0, sizeof (was));
          j = 0;
        }
      }
      
      putchar ('[');
      for (int i=0; i<j; i++)
        printf("%c%s", s[i], i==j-1 ? "]" : ", ");
      if (j == 0) {
        printf ("]");
      }
      puts("");
   }
   return 0;
}
