#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
using namespace std;

char a[30];
const char s[6][100] =
{
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"
};

int main()
{
    int n;

    for (int i = 0;i < 3;++i)
        for (int j = 0;j < strlen(s[i]);++j)
            if (s[i][j] >= 'a' && s[i][j] <= 'z')
            {
                a[s[i][j]-'a'] = s[i+3][j];
            }
    a['q'-'a'] = 'z';
    a[25] = 'q';


   freopen("1.in","r",stdin);
   freopen("1.out","w",stdout);
   scanf("%d%*c",&n);
  // cout << n;
   char c;
   for (int j = 1; j <= n;++j)
   {
       cout << "Case #" << j << ": ";
       scanf("%c",&c);
       while ((c >= 'a' && c <= 'z') || (c ==' ') )
       {
        if (c >= 'a' && c <= 'z') cout << a[c-'a'];
        else cout << c;
        scanf("%c",&c);
       }
               cout << endl;
   }

   return 0;

}
