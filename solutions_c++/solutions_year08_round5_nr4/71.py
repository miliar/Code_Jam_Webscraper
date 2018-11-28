#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>

using namespace std;

int mv[2][2] = {{2,1}, {1,2}};

int H, W, R;
bool inside (int x, int y) {
  return x <= H && y <= W;
}


int main() {
  int num_cases ;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    cout << "Case #" << case_num << ": ";
    cin >> H >> W >> R;
    set<pair<int,int> > evils;
    for (int i = 0; i < R; ++i) {
      int r,c;
      cin >> r >> c;
      evils.insert (make_pair (r,c));
    }
    vector<vector<int> > comb (H+1, vector<int> (W+1,0));
    comb[1][1] = 1;
    for (int i = 1; i <= H; ++i) {
      for (int j = 1; j <= W; ++j) {
        for (int k = 0; k < 2; ++k) {
          int nx = i + mv[k][0];
          int ny = j + mv[k][1];
          if (inside (nx,ny) && evils.find (make_pair (nx,ny)) == evils.end() ) {
            comb[nx][ny] += comb[i][j];
            comb[nx][ny] %= 10007;
          }
        }
      }
    }
    cout << comb[H][W] << "\n";
  }
}

    
