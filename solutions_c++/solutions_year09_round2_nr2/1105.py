#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <algorithm>
#include <string>

#define rep(i,x,y) for (int i = x; i < y; i++)

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int dig = 0 + '0';
   string s;

int cnt()
{
   int e = 1;
   int ma = -1;
   int dig2;
   while (e < s.length())
   {
   dig2 = s[s.length() - e] - '0';
   for (int i = s.length() - e - 1; i >= 0; i--)
   {
      if (s[i] - '0' < dig2 && i > ma)
      {
         ma = i;
         dig = dig2;
      }
   }
   e++;
   }
   return ma;
}

void count()
{
   getline(cin, s);
   int m[10];
   rep(i,0,10) m[i] = 0;
   for (int i = 0; i < s.length(); i++)
   {
      m[s[i] - '0']++;
   }
   int r = cnt();
   int k = 0;
   if (r == -1)
   {
      m[0]++;
      rep(j,1,10)
      {
         if (m[j])
         {
            printf("%c", j + '0');
            m[j]--;
            break;
         }
      }
      k = 1;
      rep(j,0,10)
         if (m[j])
         {
            while (m[j] > 0)
            {
               printf("%c", j + '0');
               m[j]--;
               k++;
               if (k == s.length() + 1)
               {
                  return;
               }
            }
         }
   }
   for (int i = 0; i < r; i++)
   {
      printf("%c", s[i]);
      m[s[i] - '0']--;
   }
   printf("%c", dig + '0');
   m[dig]--;
   while (true)
   {
      rep(j,0,10)
         if (m[j])
         {
            while (m[j] > 0)
            {
               printf("%c", j + '0');
               m[j]--;
               k++;
               if (k == s.length() - r - 1)
               {
                  return;
               }
            }
         }
   }
}

int main()
{
   freopen("in", "r", stdin);
   freopen("out", "w", stdout);
   int test;
   scanf("%d\n", &test);
   for (int z = 0; z < test; z++)
   {
   printf("Case #%d: ", z + 1);
   count();
   printf("\n");
   }

   return 0;
}
