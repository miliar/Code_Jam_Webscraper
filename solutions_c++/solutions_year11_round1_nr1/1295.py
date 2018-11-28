#include <iostream>
#include <set>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <fstream>
using namespace std;

int main() {
  ifstream cin("A-small-attempt1.in");
  ofstream cout("out.txt");
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int PD, PG, N;
    cin >> N >> PD >> PG;
    cout << "Case #" << t << ": ";
    if(PG == 0 && PD != 0) {
      cout << "Broken";
    } else if(PG == 100 && PD != 100) {
      cout << "Broken";
    } else {
      int b = min(100, N);
      bool bb = false;
      for(int i = 1; i <= b; i++) {
        if(PD*i%100 == 0) {
          cout << "Possible";
          bb = true;
          break;
        }
      }
      if(!bb)
        cout << "Broken";
    }
    cout << endl;
  }
}
