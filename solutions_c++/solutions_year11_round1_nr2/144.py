// ============================================================================
//   [ Filename    ]  pb.cpp
//   [ Description ]  
//   [ Created     ]  西元2011年05月21日 09時39分33秒 CST
//   [ Author      ]  Jiunru Yang, yangjiunru[at]gmail.com, LaDS3, GIEE, NTU
// ============================================================================

#include <vector>
#include <iostream>
#include <cstring>

using namespace std;

class Sol
{
public:
   void read()
   {
      cin >> nd >> nl;
      for (int i = 0; i < nd; ++i) {
         cin >> dict[i];
         dlen[i] = strlen(dict[i]);
      }
      for (int i = 0; i < nl; ++i)
         cin >> lett[i];
      for (int i = 0; i < nd; ++i) {
         for (int j = 0; j < 26; ++j) {
            int x = 0;
            int m = 1;
            for (int k = 0; dict[i][k]; ++k) {
               if (dict[i][k] == j + 'a')
                  x |= m;
               m <<= 1;
            }
            mask[i][j] = x;
         }
      }
   }
   int calc(int pd, int pl) {
      bool poss[100];
      int ans = 0;
      for (int i = 0; i < nd; ++i)
         poss[i] = (dlen[i] == dlen[pd]);
      for (int i = 0; i < 26; ++i) {
         int cur = lett[pl][i] - 'a';

         // check if no need to use this letter
         bool okay = false;
         for (int j = 0; j < nd; ++j) {
            if (poss[j] != true) continue;
            if (mask[j][cur]) {
               okay = true;
               break;
            }
         }
         if (!okay) continue;

         // guess this letter
         if (mask[pd][cur] == 0) ++ans; // wrong guess, +1 point
         for (int j = 0; j < nd; ++j) // eliminate inconsistent words
            if (mask[pd][cur] != mask[j][cur])
               poss[j] = false;
      }
      return ans;
   }
   int solve(int caseNo)
   {
      cout << "Case #" << caseNo << ":";
      for (int i = 0; i < nl; ++i) {
         int ma = -1;
         int wh = -1;
         for (int j = 0; j < nd; ++j) {
            int ans = calc(j, i);
            if (ma < ans) {
               ma = ans;
               wh = j;
            }
         }
         cout << " " << dict[wh];
      }
      cout << endl;
   }
private:
   int nd, nl;
   char dict[100][15];
   int dlen[100];
   char lett[10][27];
   int mask[100][26];
};

int main()
{
   int n;
   cin >> n;
   for (int i = 1; i <= n; ++i) {
      Sol s;
      s.read();
      s.solve(i);
   }
   return 0;
}
