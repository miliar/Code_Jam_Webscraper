#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


string s;

const int P = 31;

long long hash()
{
   unsigned long long res = s[s.length() - 1] - 'a';

   for (int i = s.length() - 2; i >= 0; i--)
   {
      res = res * P + (s[i] - 'a');
   }

   return res;
}

int main()
{
   freopen("alien.in", "r", stdin);
   freopen("alien.out", "w", stdout);
   int l,d,n;
   scanf("%d%d%d", &l, &d, &n);
   getline(cin, s);
   vector<long long> list[l][100];
   for (int i = 0; i < d; i++)
   {
      getline(cin, s);
      unsigned long long h = hash();
      for (int j = 0; j < l; j++)
      {
         list[j][s[j] - 'a'].push_back(h);
      }
   }
   string str;
   vector<long long> now;
   int k;
   for (int i = 0; i < n; i++)
   {
      now.clear();
      getline(cin, str);
      k = 0;
      int j = 0;
      while (j < str.length())
      {
         if (str[j] == '(')
         {
            j++;
            while (str[j] != ')')
            {
               for (int r = 0; r < list[k][str[j] - 'a'].size(); r++)
               {
                now.push_back(list[k][str[j] - 'a'][r]);
               }
               j++;
            }
         }
         else
         {
            for (int r = 0; r < list[k][str[j] - 'a'].size(); r++)
            {
             now.push_back(list[k][str[j] - 'a'][r]);
            }
         }
         k++;
         j++;
      }
      sort(now.begin(), now.end());
      int cnt = 1, count = 0;
      now.push_back(-1);
      for (int r = 1; r < now.size(); r++)
      {
         if (now[r] == now[r - 1])
         {
            cnt++;
         }
         else
         {
             if (cnt == l)
             {
               count++;
              }
            cnt = 1;
         }
      }
      printf("Case #%d: %d\n", i + 1, count);
   }

   return 0;
}
