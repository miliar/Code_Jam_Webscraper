// =====================================================================================
//   [ Filename    ]  pa.cpp
//   [ Description ]  
//   [ Created     ]  09/27/2009 12:05:44 AM CST
//   [ Author      ]  Jiunru Yang , yangjiunru [at] gmail.com, NTUEE
// =====================================================================================

#include <iostream>
#include <vector>
#include <string>

using namespace std;

void mySwap(int& a, int& b, int& cnt)
{
   ++cnt;
   int tmp = a;
   a = b;
   b = tmp;
}

void solve(int caseNo)
{
   int n;
   cin >> n;
   vector<int> s;
   int ans = 0;
   s.resize(n);
   for (int i = 0; i < n; ++i) {
      string a;
      cin >> a;
      int j;
      for (j = n-1; j >= 1; --j)
         if (a[j] == '1')
            break;
      s[i] = j+1;
   }

   for (int i = 0; i < n; ++i) {
      int j;
      if (s[i] <= i+1)
         continue;
      for (j = i + 1; j < n; ++j)
         if (s[j] <= i+1)
            break;
      for (--j; j >= i; --j)
         mySwap(s[j], s[j+1], ans);
   }

   cout << "Case #" << caseNo << ": " << ans << endl;
}

int main()
{
   int T;
   cin >> T;
   for (int t = 0; t < T; ++t)
      solve(t+1);
   return 0;
}
