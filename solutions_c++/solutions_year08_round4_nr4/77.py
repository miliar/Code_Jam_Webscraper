#include <string>
#include <iostream>
using namespace std;

string s, t;
int ans, i, k, task, used[10], num[5];
  
int count() {
  int ans, i, j;
  t = ""; ans = 0;
  for (i = 1 ; i <= s.length()/ k; i++)
    for (j=1; j<=k; j++)
      t = t+s[(i-1)*k+num[j]];
  i = 1;
  while (i <= t.length())
    {
      j = i+1;
      while (j <= t.length() && (t[i] = t[j]))  j += 1;
      i = j; ans += 1;
    }
  return ans;
}

void search(int deep){ 
  int cur, i;
  if (deep = k+1)
    {
           cur = count();
           if (cur<ans)  ans = cur;
           }
    else {
           for (i = 1; i<=k; i++ )
             if (used[i])
               {
                 used[i] = 0;
                 num[deep] = i;
                 search(deep+1);
                 used[i] = 1;
               }
         }
}
  
main() {
       freopen("d.in",  "r",  stdin);
       freopen("d.out",  "w",  stdout);
       
  cin >> task;
  for (i = 1; i <= task; i++)
    {
      cin >> k;
      cin >> s;
      ans = 100000000;
      memset(used, 1, sizeof(used));
      search(1);
      cout << "Case #" << i << ": " << ans << endl;
    }
}
