#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;
typedef vector<int> VecInt;

const char nl = '\n';

int main()
{
   int N, P, K, L;
   cin >> N;
   for ( int m = 1; m <= N; m++ ) {
      cin >> P >> K >> L;
      VecInt F(L);
      for ( int i = 0; i < L; i++ )
         cin >> F[i];
      cout << "Case #" << m << ": ";
      if ( P*K < L )
         cout << "Impossible";
      else {
         sort(F.begin(), F.end(), greater<int>());
         int T = 0;
         for ( int i = 0; i < L; i++ )
            T += (i/K+1) * F[i];
         cout << T;
      }
      cout << nl;
   }
   return 0;
}
