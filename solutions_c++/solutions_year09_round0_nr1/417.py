#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int l, d, n;
string dic[5010];
string str, tmp;
char ds[30];
int ans;
void dfs(int p, int lev)
{
     if (lev == l)
     {
          ds[lev] = '\0';
          tmp = ds;
          for (int i=0; i<d; i++)
          {
               if (tmp == dic[i])
               {
                    ans++;
                    return;
               }
          }
          return;
     }
     if (str[p] == '(')
     {
          int ai;
          for (ai=p; str[ai]!=')'; ai++);
          for (int i=p+1; i<ai; i++)
          {
               ds[lev] = str[i];
               bool flag = false;
               for (int j=0; j<d; j++)
               {
                    if (dic[j][lev] == ds[lev])
                         flag = true;
               }
               if (flag)
                    dfs(ai+1, lev+1);
          }
     }
     else
     {
          ds[lev] = str[p];
          dfs(p+1, lev+1);
     }
}
bool ok(int k)
{
     int p = 0;
     for (int i=0; i<l; i++)
     {
          if (str[p] == '(')
          {
               bool flag = false;
               p++;
               while (str[p] != ')')
               {
                    if (str[p] == dic[k][i])
                         flag = true;
                    p++;
               }
               if (!flag)
                    return false;
          }
          else
          {
               if (str[p] != dic[k][i])
                    return false;
          }
          p++;
     }
     return true;
}
int main(int argc, char *argv[])
{
     cin >> l >> d >> n;
     for (int i=0; i<d; i++)
          cin >> dic[i];
     for (int i=1; i<=n; i++)
     {
          ans = 0;
          cin >> str;
          for (int j=0; j<d; j++)
          {
               if (ok(j))
               {
                    ans++;
               }
          }
          cout << "Case #" << i << ": " << ans << endl;
     }
     return 0;
}
