#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

string str = "welcome to code jam";
vector<int> c[1000];
int cnt = 0;

void put(int e, int p)
{
   if (e == str.length())
   {
      cnt++;
      cnt %= 10000;
      return;
   }
   for (int j = 0; j < c[str[e]].size(); j++)
     {
        if (c[str[e]][j] > p)
        {
           put(e + 1, c[str[e]][j]);
        }
      }
}

int main()
{
   freopen("welcome.in", "r", stdin);
   freopen("welcome.out", "w", stdout);
   int n;
   scanf("%d\n", &n);
   string s;
   for (int z = 0; z < n; z++)
   {
   cnt = 0;
   getline(cin, s);
   if (s.length() < str.length())
   {
      cnt = 0;
   }
   else
   {
   for (int i = 0; i < s.length(); i++)
   {
      c[s[i]].clear();
   }
   for (int i = 0; i < s.length(); i++)
   {
      c[s[i]].push_back(i);
   }
   put(0, -1);
   }
   
   printf("Case #%d: ", z + 1);
   printf("%04d\n", cnt);
   }

   return 0;
}
