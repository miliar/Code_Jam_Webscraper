// ============================================================================
//   [ Filename    ]  pc.cpp
//   [ Description ]  
//   [ Created     ]  西元2011年05月07日 13時43分42秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <iostream>

using namespace std;

int main()
{
   int N;
   cin >> N;
   for (int i = 1; i <= N; ++i) {
      int sum = 0;
      int xsum = 0;
      int small = INT_MAX;
      int n;
      cin >> n;
      for (int j = 0; j < n; ++j) {
         int x;
         cin >> x;
         if (small > x)
            small = x;
         sum += x;
         xsum ^= x;
      }
      cout << "Case #" << i << ": ";
      if (xsum != 0) {
         cout << "NO" << endl;
      }
      else {
         cout << (sum - small) << endl;
      }
   }
   return 0;
}
