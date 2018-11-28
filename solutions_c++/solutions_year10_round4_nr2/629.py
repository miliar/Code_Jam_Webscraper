#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <string>
#include <cmath>
using namespace std;

int round_num;
int result;
int m[1025];

void rec(int depth, int from, int to) {
  //  cout << "from,to = " << from << "," << to << endl;

  bool flag = false;
  for(int i=from; i<to; i++) {
    if(m[i] > 0) {
      flag = true;
      break;
    }
  }

  if(flag) {
    result++;
    for(int i=from; i<to; i++) {
      m[i] = max(0, m[i]-1);
    }

    int temp = (from+to)/2;
    rec(depth-1, from, temp);
    rec(depth-1, temp, to);
  } else {
    return;
  }
}

int main() {
  int casenum;
  cin >> casenum;

  for(int iii=1; iii<=casenum; iii++) {
    cin >> round_num;

    int team_num = 1<<round_num;
    for(int i=0; i<team_num; i++) {
      int temp;
      cin >> temp;
      m[i] = round_num - temp;
    }

    // discard
    int costs[1024];
    for(int i=0; i<team_num-1; i++) cin >> costs[i];

    result = 0;
    rec(round_num, 0, team_num);
    
    cout << "Case #" << iii << ": " << result << endl;
  }

  return 0;
}
