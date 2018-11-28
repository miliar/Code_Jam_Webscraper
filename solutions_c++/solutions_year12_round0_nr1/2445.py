#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;
//           "abcdefghijklmnopqrstuvwxyz"
char res[] = "yhesocvxduiglbkrztnwjpfmaq";
              
int main (void)
{
  int test, tests, i, n;
  char s[111];
  freopen ("a.in", "rt", stdin);
  freopen ("a.out", "wt", stdout);
  scanf ("%d", &tests);
  gets (s);
  for (test = 0; test < tests; test++)
  {
    gets (s);
    n = strlen(s);
    printf ("Case #%d: ", test + 1);
    for (i = 0; i < n; i++)
    {
      if (s[i] >= 'a' && s[i] <= 'z')
        s[i] = res[s[i] - 'a'];
      putchar (s[i]);
    }
    putchar ('\n');
    
  }
  return 0;
}
