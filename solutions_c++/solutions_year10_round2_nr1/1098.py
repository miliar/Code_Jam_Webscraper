#include <stdio.h>
#include <string>
#include <iostream>
#include <map>
using namespace std;

int n, m;
map<string, int> mp;

int main()
{
  freopen("A-large.in", "r", stdin);
   freopen("A-large.out", "w", stdout);
   int i, j, cs, cnt, csnum, ans;
   string s, t;
   cs = 1;
   scanf ("%d", &csnum);
   while (csnum--)
   {
      mp.clear();
      scanf ("%d %d", &n, &m);
      cnt = 0;
      for (i = 0; i < n; i++)
      {
         cin >> s;
         t = "";
         for (j = 1; j < s.length(); j++)
         {
            if (s[j] != '/')
               t += s[j];
            else
            {
               //cout << "t " << t << endl;
               mp[t] = 1;
               t += '/';
               //while(1);
            }
         }
         mp[t] = 1;
      }
      ans = 0;
      for (i = 0; i < m; i++)
      {
         cin >> s;
         t = "";
         for (j = 1; j < s.length(); j++)
         {
            if (s[j] != '/')
               t += s[j];
            else
            {
               //cout << "t " << t << endl;
             //  mp[t] = 1;
               if (mp.find(t) == mp.end())
                  cnt++;
               mp[t] = 1;
               t += '/';
               //while(1);
            }
         }
         if (mp.find(t) == mp.end())
                  cnt++;
         mp[t] = 1;
      }
      printf("Case #%d: %d\n", cs++, cnt);
      
      
   }
}
/*
3
2 1
/chicken
/chicken/egg
/chicken
*/
