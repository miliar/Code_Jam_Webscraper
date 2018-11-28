// ============================================================================
//   [ Filename    ]  snapper.cpp
//   [ Description ]  
//   [ Created     ]  西元2010年05月08日 11時59分26秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <iostream>

using namespace std;

int main() {
   int T;
   cin >> T;
   for (int t = 1; t <= T; ++t) {
      unsigned n, k;
      cin >> n >> k;
      cout << "Case #" << t << ": ";
      if (((k) & ((1u << (n))-1)) == ((1u << (n))-1))
         cout << "ON" << endl;
      else
         cout << "OFF" << endl;
   }
   return 0;
}
