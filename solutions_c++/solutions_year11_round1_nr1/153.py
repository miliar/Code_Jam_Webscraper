// ============================================================================
//   [ Filename    ]  pa.cpp
//   [ Description ]  
//   [ Created     ]  西元2011年05月21日 09時08分05秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <iostream>

using namespace std;

bool run()
{
   long long n, pd, pg;
   cin >> n >> pd >> pg;
   if (pg == 100 && pd < 100)
      return false;
   if (pg == 0 && pd > 0)
      return false;
   long long thre = 100;
   if (pd % 25 == 0)
      thre /= 25;
   else if (pd % 5 == 0)
      thre /= 5;
   if (pd % 4 == 0)
      thre /= 4;
   else if (pd % 2 == 0)
      thre /= 2;
   return n >= thre;
}

int main()
{
   int n;
   cin >> n;
   for (int i = 1 ; i <= n; ++i) {
      cout << "Case #" << i << ": " << (run() ? "Possible" : "Broken") << endl;
   }
   return 0;
}
