#include <iostream>
#include <cstdio>
#include <string>
#include <map>

using namespace std;

map<string,bool> m;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int N,k=1,n,mi;
    string s;
    scanf("%d",&N);
    while (k <= N)
    {
          int hasil = 0;
          scanf("%d %d",&n,&mi);
          m.clear();
          m[""] = true;
          for (int i = 0; i < n; i++)
          {
              cin >> s;
              string temp = "";
              for (int j = 0; j < s.size(); j++)
              {
                  if (s[j] == '/')
                     m[temp] = true;
                  temp += s[j];
              }
              m[temp] = true;
          }
          for (int i = 0; i < mi; i++)
          {
              cin >> s;
              string temp = "";
              for (int j = 0; j < s.size(); j++)
              {
                  if (s[j] == '/' && !m[temp])
                  {
                     m[temp] = true;
                     hasil++;
                  }
                  temp += s[j];
              }
              if (!m[temp])
              {
                 m[temp] = true;
                 hasil++;
              }
          }
          printf("Case #%d: %d\n",k,hasil);
          k++;
    }
    return 0;
}
