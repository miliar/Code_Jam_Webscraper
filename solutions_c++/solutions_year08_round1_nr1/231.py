#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void)
{
   int n;
   cin >> n;
   vector<int> vec_a;
   vector<int> vec_b;
   for(int i = 1; i <= n; ++i)
   {
      cout << "Case #" << i << ": ";
      int len;
      cin >> len;
      if(len == 0)
      {
         cout << "0\n";
         continue;
      }

      vec_a.clear();
      vec_b.clear();
      for(int j = 0; j < len; ++j)
      {
         int x;
         cin >> x;
         vec_a.push_back(x);
      }
      for(int j = 0; j < len; ++j)
      {
         int x;
         cin >> x;
         vec_b.push_back(x);
      }

      sort(vec_a.begin(), vec_a.end());
      sort(vec_b.begin(), vec_b.end(), std::greater<int>());
      int ans = 0;
      for(int j = 0; j < len; ++j)
         ans += (vec_a[j] * vec_b[j]);
      cout << ans << endl;
   }
   return 0;
}
