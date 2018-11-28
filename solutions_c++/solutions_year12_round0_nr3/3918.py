#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<ctime>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<cassert>
#include<cstdlib>
using namespace std;

#define taskname "a"


int main()
{
  freopen(taskname".in", "r", stdin);
  freopen(taskname".out", "w", stdout);
  int l, r, t;
  set<int> s;
  cin >> t;
  for(int k = 0; k < t; k++)
  {
    long long ans = 0;
    cin >> l >> r;
    int q = 0;
    int w = l;
    while(w > 0)
    {
      w/=10;
      q++;
    }
    long long y = 1;
    for(int i = 0; i < q-1; i++)
      y *= 10;
    for(int i = l; i <= r; i++)
    {
      s.clear();
      int w = i;
      for(int j = 0; j < q; j++)
      {
        if(w >= l && w <= r && w > i )
          s.insert(w);
        int z = w / y;
        w = (w%y)*10+z; 
      }
      ans += s.size();
    }
    cout << "Case #" << k+1 << ": " << ans << endl;
  }
  return 0;
}
