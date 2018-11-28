// ============================================================================
//   [ Filename    ]  pd.cpp
//   [ Description ]  
//   [ Created     ]  西元2011年05月07日 13時51分40秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <iostream>
#include <vector>

using namespace std;

void solve(int caseNo) {
   vector<int> seq;
   int n;
   int ans = 0;
   cin >> n;
   for (int i = 0; i < n; ++i) {
      int x;
      cin >> x;
      if (x != i + 1) ++ans;
   }
   /*seq.resize(n);
   for (int i = 0; i < n; ++i)
      cin >> seq[i];
   for (int i = 0; i < n; ++i) {
      if (seq[i] != i + 1) {
         ans += 2;
         for (int j = i + 1; j < n; ++j)
            if (seq[j] == i + 1) {
               seq[j] = seq[i];
               break;
            }
      }
   }*/
   cout << "Case #" << caseNo << ": " << ans << ".000000" << endl;
}

int main() {
   int N;
   cin >> N;
   for (int i = 1; i <= N; ++i)
      solve(i);
   return 0;
}
