// ============================================================================
//   [ Filename    ]  snapper.cpp
//   [ Description ]  
//   [ Created     ]  �褸2010�~05��08�� 11��59��26�� CST
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
