#include <iostream>
#include <cstring>

#include <string>

using namespace std;

#define SZ(a) int((a).size())

char T[26][26];
int opp[26];
int freq[26];

int main(int argc, char* argv[]) {
   int TC;
   cin >> TC;
   for (int tc = 1; tc <= TC; ++tc) {
      memset(T, 0, sizeof(T));
      int C;
      cin >> C;
      while (C-- > 0) {
         string S;
         cin >> S;
         int c0 = S[0]-'A', c1 = S[1]-'A';
         T[c0][c1] = T[c1][c0] = S[2];
      }

      memset(opp, 0, sizeof(opp));
      int D;
      cin >> D;
      while (D-- > 0) {
         string S;
         cin >> S;
         int c0 = S[0]-'A', c1 = S[1]-'A';
         opp[c0] |= 1 << c1;
         opp[c1] |= 1 << c0;
      }

      string res;
      memset(freq, 0, sizeof(freq));
      int in_list = 0;

      int N;
      cin >> N;
      string S;
      cin >> S;
      for (int i = 0; i < N; ++i) {
         int ci = S[i]-'A';
         if (!res.empty()) {
            int last = res[SZ(res)-1]-'A';
            if (T[last][ci]) {
               if (--freq[last] == 0)
                  in_list &= ~( 1 << last );
               res[ SZ(res)-1 ] = T[last][ci];
               last = res[SZ(res)-1]-'A';
               freq[last]++;
               in_list |= 1 << last;
               continue;
            }
            if (opp[ci] & in_list) {
               res.clear();
               memset(freq, 0, sizeof(freq));
               in_list = 0;
               continue;
            }
         }
         res += S[i];
         freq[ci]++;
         in_list |= 1 << ci;
      }

      cout << "Case #" << tc << ": [";
      for (int i = 0; i < SZ(res); ++i) {
         if (i > 0) cout << ", ";
         cout << res[i];
      }
      cout << "]" << endl;
   }
   return 0;
}
