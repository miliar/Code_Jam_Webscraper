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
    int small, large, multi;
    cin >> small >> large >> multi;

    int cnt=0;
    long long s=small;
    while(s < large) {
      s *= multi;
      cnt++;
    }

    int result=0;
    double c = cnt;
    while(c > 1) {
      c /= 2;
      result++;
    }

    cout << "Case #" << iii << ": " << result << endl;
  }


  return 0;
}
