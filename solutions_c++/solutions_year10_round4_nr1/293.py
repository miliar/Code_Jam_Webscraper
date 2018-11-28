#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <string>
#include <cmath>
using namespace std;

const int NaN = -298324793;

int main() {
  int casenum;
  cin >> casenum;

  for(int iii=1; iii<=casenum; iii++) {
    int input_size;
    cin >> input_size;

    int table[128][128];
    fill(&table[0][0], &table[127][127]+1, NaN);

    for(int y=0; y<input_size; y++) {
      for(int x=0; x<=y; x++) {
        int offset = input_size-1 - y;
        cin >> table[offset + x*2][y];
      }
    }
    for(int y=input_size-2; y>=0; y--) {
      for(int x=0; x<=y; x++) {
        int offset = input_size-1 - y;
        cin >> table[offset + x*2][input_size*2-y-2];
      }
    }

    /*
    for(int i=0; i<input_size*2; i++) {
      for(int j=0; j<input_size*2; j++) {
        if(table[j][i]==NaN) cout << " ";
        else cout << table[j][i];
      }
      cout << endl;
    }
    //*/

    int cost = INT_MAX;
    int size = input_size * 2 - 1;
    for(int cy=0; cy<size; cy++) {
      for(int cx=0; cx<size; cx++) {

        bool flag = true;
        for(int y1=0; y1<size; y1++) {
          for(int x1=0; x1<=size; x1++) {
            if(table[x1][y1] == NaN) continue;
            int x2 = 2*cx - x1;
            int y2 = 2*cy - y1;

            bool x_nan =
              (x2 < 0 || size <= x2) || 
              table[x2][y1] == NaN;
            bool y_nan =
              (y2 < 0 || size <= y2) || 
              table[x1][y2] == NaN;

            if(x_nan && y_nan) continue;
            if(x_nan && table[x1][y1] == table[x1][y2]) continue;
            if(y_nan && table[x1][y1] == table[x2][y1]) continue;
              
            if(table[x1][y1] != table[x1][y2] || table[x1][y1] != table[x2][y1]) {
              flag = false;
              break;
            }
          }
        }

        if(flag) {
          int diff = abs(cx - (input_size-1)) + abs(cy - (input_size-1));
          int c = (diff+input_size) * (diff+input_size) - input_size*input_size;
          cost = min(cost, c);
          //          cout << "cx,cy=" << cx << "," << cy << "   cost=" << c << "   input_size=" << input_size;
          //          cout << "  diff=" << diff << endl;
        }
      }
    }

    cout << "Case #" << iii << ": " << cost << endl;
  }

  return 0;
}
