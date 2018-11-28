#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <fstream>
#include <sstream>

using namespace std;

int main() {
  ifstream cin("file.in");
  ofstream cout("out.txt");
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int N;
    cin >> N;
    vector<int> O;
    vector<int> B;
    vector<bool> who;  // 0 - O, 1 - B
    for(int i = 0; i < N; i++) {
      char c;
      cin >> c;
      int button;
      cin >> button;
      who.push_back(c == 'B');
      if(who.back())
        B.push_back(button);
      else
        O.push_back(button);
    }
    int res = 0;
    int curB = 0;
    int curO = 0;
    int posB = 1;
    int posO = 1;
    for(int cur = 0; cur < N; cur++) {
      int time = 0;
      if(who[cur]) {
        time += abs(B[curB] - posB) + 1;
        posB = B[curB];
        if(!O.empty())
        if(posO < O[curO])
          posO = min(posO + time, O[curO]);
        else
          posO = max(posO - time, O[curO]);
        curB++;
      } else {
        time += abs(O[curO] - posO) + 1;
        posO = O[curO];
        if(!B.empty())
        if(posB < B[curB])
          posB = min(posB + time, B[curB]);
        else if(posB > B[curB])
          posB = max(posB - time, B[curB]);
        curO++;
      }
      res += time;
    }
    cout << "Case #" << t << ": ";
    cout << res;
    cout << endl;
  }
}
