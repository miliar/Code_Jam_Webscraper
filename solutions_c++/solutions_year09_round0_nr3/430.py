#include <iostream>
#include <string>
#include <cstring>
using namespace std;
const int maxl = 510;
char str[maxl];
char s[] = " welcome to code jam";
bool v[maxl][20];
int f[maxl][20];
int l;
void init()
{
     memset(v, false, sizeof(v));
     memset(f, 0, sizeof(f));
     gets(str+1);
     l = strlen(str+1);
     v[0][0] = true;
     f[0][0] = 1;
}
void calc()
{
     for (int i=1; i<=l; i++)
     {
          int id[20], tot = 0;
          for (int j=1; j<=19; j++)
          {
               if (s[j] == str[i])
                    id[tot++] = j;
          }
          if (tot == 0) continue;
          for (int j=0; j<i; j++)
          {
               for (int k=0; k<tot; k++)
               {
                    if (v[j][id[k]-1])
                    {
                         v[i][id[k]] = true;
                         f[i][id[k]] += f[j][id[k]-1];
                         if (f[i][id[k]] >= 10000)
                              f[i][id[k]] -= 10000;
                    }
               }
          }
     }
}
int main(int argc, char *argv[])
{
     int t;
     cin >> t;
     getchar();
     for (int i=1; i<=t; i++)
     {
          init();
          calc();
          int ans = 0;
          for (int j=1; j<=l; j++)
          {
               ans += f[j][19];
               if (ans >= 10000)
                    ans -= 10000;
          }
          printf("Case #%d: %04d\n", i, ans);
     }
     return 0;
}
