#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <limits>
#include <algorithm>

using namespace std;
typedef map<string, int> StrMap;
typedef vector<int> IntVect;

StrMap T;
const char nl = '\n';
const int Inf = numeric_limits<int>::max();

int main()
{
   int N, S, Q;
   string str;

   freopen("pa.in", "r", stdin);
   cin >> N;
   for ( int m = 1; m <= N; m++ ) {
      cin >> S; cin.ignore();
      for ( int i = 0; i < S; i++ ) {
         getline(cin, str);
         T[str] = i;
      }
      cin >> Q; cin.ignore();
      IntVect C(S, 0), C1(S, 0);
      for ( int i = 0; i < Q; i++ ) {
         getline(cin, str);
         int id = T[str];
         for ( int j = 0; j < S; j++ ) {
            int minv = Inf;
            for ( int k = 0; k < S; k++ )
               if ( k != id && C[k] < minv )
                  minv = C[k];
            if ( j == id )
               C1[j] = minv + 1;
            else
               C1[j] = min(C[j], minv + 1);
         }
         C.swap(C1);
      }
      cout << "Case #" << m << ": " << *min_element(C.begin(), C.end()) << nl;
   }
   return 0;
}
