#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <string>
#include <cmath>
using namespace std;

int main() {
  int casenum;
  cin >> casenum;

  for(int iii=1; iii<=casenum; iii++) {
    bool table[256][256];
    fill(&table[0][0], &table[255][255]+1, false);

    int bacteria_num;
    cin >> bacteria_num;
    
    for(int i=0; i<bacteria_num; i++) {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      for(int x=x1; x<=x2; x++) {
        for(int y=y1; y<=y2; y++) {
          table[x][y] = true;
        }
      }
    }

    int turn = 0;
    int remain = 1;
    while(remain > 0) {
      remain = 0;
      turn++;

      for(int x=255; x>0; x--) {
        for(int y=255; y>0; y--) {
          if(table[x][y]) {
            if(table[x-1][y] || table[x][y-1]) {
              remain++;
            } else {
              table[x][y] = false;
            }
          } else {
            if(table[x-1][y] && table[x][y-1]) {
              table[x][y] = true;
              remain++;
            }
          }
        }
      }

      /*
      for(int y=0; y<10; y++) {
        for(int x=0; x<10; x++) {
          cout << table[x][y];
        }
        cout << endl;
      }
      cout << "remain = " << remain << endl;
      //*/
    }

    cout << "Case #" << iii << ": " << turn << endl;
  }

  return 0;
}
