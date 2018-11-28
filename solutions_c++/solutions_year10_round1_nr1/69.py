#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int N, K;

bool find(const vector<string> &bord, char ch) {
   static const int dr[] = { -1, -1, 0, 1 };
   static const int dc[] = { 0, 1, 1, 1 };
   for (int r=0; r<N; ++r) {
      for (int c=0; c<N; ++c) {
         for (int dir=0; dir<4; ++dir) {
            int k, nr = r, nc = c;
            for (k=0; k<K; ++k, nr += dr[dir], nc += dc[dir]) {
               if (nr < 0 || nr >= N) break;
               if (nc < 0 || nc >= N) break;
               if (bord[nr][nc] != ch) break;
            }
            if (k == K) {
               return 1;
            }
         }
      }
   }
   return 0;
}

int main(void) { 
   cin.sync_with_stdio(0);

   int CASES; cin >> CASES;
   for (int tt=1; tt<=CASES; ++tt) { // caret here
      cin >> N >> K;

      vector<string> bord(N);
      for (int i=0; i<N; ++i) {
         cin >> bord[i];
         for (int j=N-2; j>=0; --j) {
            int k;
            for (k=j+1; k<N && bord[i][k] == '.'; ++k) ;
            swap(bord[i][j], bord[i][k-1]);
         }
      }

      bool red = find(bord, 'R');
      bool blue = find(bord, 'B');

      string ans = "Neither";
      if (red && blue) ans = "Both";
      else if (red) ans = "Red";
      else if (blue) ans = "Blue";
      cout << "Case #" << tt << ": " << ans << endl;
   }

   return 0;
} 
