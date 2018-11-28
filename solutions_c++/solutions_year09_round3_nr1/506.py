#include <iostream>
#include <cstdio>
#include <string>
#include <map>
using namespace std;

typedef unsigned long long ULL;

ULL solve(string s)
{
 int diff = 0;
 
 map <char, bool> used;
 for (int i = 0; i < s.size(); i++)
  if (!used[s[i]])
  {
   used[s[i]] = true;
   diff++;
  }
 
 ULL ret = 0; bool flag = true;
 int num = 0; 
 
 for (ULL base = diff; base < 38; base++) 
 {
  ULL cur = 0; 
  map <char, int> ass;
  bool added[100];
  memset(added, 0, sizeof(added));
  
  bool fuck = false;
  for (int i = 0; i < s.size(); i++)
  {
   bool ok = false;
   if (ass.count(s[i]))
   {
    ok = true;
    cur = cur * base + ass[s[i]];
   }
   else
   {
    for (int j = 0; j < base; j++)
    {
     if (j == 0 && i == 0) continue;
     if (!added[j])
     {
      ok = true;
      ass[s[i]] = j;
      added[j] = true;
      cur = cur * base + ass[s[i]];
      break;
     }
    }
   } 
   if (!ok) { fuck = true; break; }
  }
  
  if (fuck) continue;
  
  num++;
  if (num == 3) break;
  
  if (cur < ret || flag)
  {
   ret = cur;
   flag = false;
  }
 }
 
 return ret;
}

int main()
{
 int T;
 cin >> T;
 
 for (int t = 0; t < T; t++)
 {
  string s; cin >> s;
  printf("Case #%d: ", t + 1);
  cout << solve(s) << endl;
 }
 
 return 0;
}
