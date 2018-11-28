#include <cstdio>
#include <cstring>
#include <cctype>

using namespace std;

char trans[30], buf[200];
int n, j;

void learn(const char *b, const char *a)
{
  for (int i = strlen(a) - 1; i >= 0; i--)
    if (isalpha(a[i]))
      trans[a[i] - 'a'] = b[i];
}

int main()
{
  trans['z' - 'a'] = 'q';
  trans['q' - 'a'] = 'z';
  learn("our language is impossible to understand",
        "ejp mysljylc kd kxveddknmc re jsicpdrysi");
  learn("there are twenty six factorial possibilities",
        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
  learn("so it is okay if you want to just give up",
        "de kr kd eoya kw aej tysr re ujdr lkgc jv");

  scanf("%d\n", &n);
  for (int i = 0; i < n; i++)
  {
    fgets(buf, sizeof(buf), stdin);
    printf("Case #%d: ", i + 1);
    j = 0;
    while (buf[j]) 
    {
      if (isalpha(buf[j]))
        printf("%c", trans[buf[j] - 'a']);
      else 
        printf("%c", buf[j]);
      j++;
    }
  }

  return 0;
}
