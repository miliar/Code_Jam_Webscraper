#include <cstdlib>
#include <iostream>

using namespace std;

#define le 100

char str1[][100] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                "de kr kd eoya kw aej tysr re ujdr lkgc jv"};

char str2[][100] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};

int tran[30];
char str[100000];

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int len;
    int i, j;
    for (i = 0; i < 3; i++)
    {
        len = strlen(str1[i]);
        for (j = 0; j < len; j++)
        {
            if (str1[i][j] == ' ')
               continue;
            tran[str1[i][j] - 'a'] = str2[i][j] - 'a';
        }
    }
    tran['z'-'a'] = 'q' - 'a';
    tran['q'-'a'] = 'z' - 'a';
    int n;
    scanf ("%d\n", &n);
    int cas = 1;
    while (n--)
    {
          gets(str);
          printf ("Case #%d: ", cas++);
          len = strlen(str);
          for (i = 0; i < len; i++)
          {
              if (str[i] == ' ')
                 printf (" ");
              else
                  printf ("%c", tran[str[i]-'a'] + 'a');
          }
          printf ("\n");
    }
    return 0;
}
