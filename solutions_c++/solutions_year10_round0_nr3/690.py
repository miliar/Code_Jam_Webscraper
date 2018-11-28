// ============================================================================
//   [ Filename    ]  theme.cpp
//   [ Description ]  
//   [ Created     ]  西元2010年05月08日 12時36分02秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <iostream>
#include <vector>

using namespace std;

int caseNo = 1;

void solve()
{
   unsigned long long ans = 0;
   int R;
   unsigned K, N;
   cin >> R >> K >> N;
   vector<unsigned> gi(N);
   for (unsigned i = 0; i < N; ++i)
      cin >> gi[i];
   if (N == 1) {
      if (gi[0] > K)
         ans = 0;
      else
         ans = R * gi[0];
      cout << "Case #" << (caseNo++) << ": " << ans << endl;
      return;
   }

   vector<int> hiscur(N, -1);
   vector<unsigned long long> hisans;

   unsigned cur = 0;
   unsigned many = 0;
   hiscur[0] = 0;
   hisans.push_back(0ull);
   while (R--) {
      unsigned ck = K;
      while (ck && many != N) {
         if (gi[cur] > ck)
            break;
         ck -= gi[cur];
         ans += gi[cur];
         cur = (cur+1)%N;
         many++;
      }
      many = 0;
      if (hiscur[cur] != -1)
         break;
      hiscur[cur] = hisans.size();
      hisans.push_back(ans);
   }
   if (R <= 0) {
      cout << "Case #" << (caseNo++) << ": " << ans << endl;
      return;
   }
   unsigned len = hisans.size() - hiscur[cur];
   unsigned long long cans = ans - hisans[hiscur[cur]];
   unsigned long long cycle = R / len;
   R %= len;
   ans += cycle * cans;
   if (R >= 0) {
      while (R--) {
         unsigned ck = K;
         while (ck && many != N) {
            if (gi[cur] > ck)
               break;
            ck -= gi[cur];
            ans += gi[cur];
            cur = (cur+1)%N;
            many++;
         }
         many = 0;
      }
   }

   cout << "Case #" << (caseNo++) << ": " << ans << endl;
}

int main()
{
   int T;
   cin >> T;
   while (T--)
      solve();
   return 0;
}
