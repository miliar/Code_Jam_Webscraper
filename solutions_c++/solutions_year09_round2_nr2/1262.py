// =====================================================================================
//   [ Filename    ]  naive.cpp
//   [ Description ]  
//   [ Created     ]  09/13/2009 12:10:19 AM CST
//   [ Author      ]  Jiunru Yang , yangjiunru [at] gmail.com, NTUEE
// =====================================================================================

#include <iostream>
#include <vector>

using namespace std;

static inline vector<unsigned> count(unsigned n)
{
   vector<unsigned> ret(9);
   while (n) {
      unsigned i = n % 10;
      n /= 10;
      if (i)
         ++ret[i-1];
   }
   return ret;
}

void solve(int caseNo)
{
   unsigned N;
   cin >> N;
   vector<unsigned> vu = count(N);
   unsigned i = N+1;
   while (true) {
      if (count(i) == vu)
         break;
      ++i;
   }
   cout << "Case #" << caseNo << ": " << i << endl;
}

int main()
{
   int T;
   cin >> T;
   for (int t = 0; t < T; ++t)
      solve(t+1);
   return 0;
}
