// ============================================================================
//   [ Filename    ]  fair.cpp
//   [ Description ]  
//   [ Created     ]  西元2010年05月08日 22時24分01秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <iostream>
#include <gmpxx.h>

using namespace std;

int caseNo = 1;

inline mpz_class diff(mpz_class& a, mpz_class& b) { return (a>b?(a-b):(b-a)); }

mpz_class mgcd(mpz_class& a, mpz_class& b)
{
   mpz_t r;
   mpz_init(r);
   mpz_gcd(r, a.get_mpz_t(), b.get_mpz_t());
   return mpz_class(r);
}

void solve()
{
   int n;
   cin >> n;
   mpz_class a0, T, a1;
   cin >> a0 >> a1;
   T = diff(a0, a1);
   for (int i = 2; i < n; ++i) {
      cin >> a1;
      mpz_class d = diff(a1, a0);
      T = mgcd(T, d);
   }
   a1 = a0 % T;
   if (a1 != mpz_class(0))
      a1 = T - a1;
   cout << "Case #" << (caseNo++) << ": " << a1 << endl;
}

int main()
{
   int T;
   cin >> T;
   while (T--)
      solve();
   return 0;
}
