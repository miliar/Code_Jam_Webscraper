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
    int wn;
    cin >> wn;

    vector<pair<int, int> > wire;
    for(int i=0; i<wn; i++) {
      int a, b;
      cin >> a >> b;
      wire.push_back(make_pair(a, b));
    }
    sort(wire.begin(), wire.end());

    int result = 0;
    for(int i=0; i<wn; i++) {
      int h = wire[i].second;
      for(int j=i+1; j<wn; j++) {
        if(wire[j].second < h) result++;
      }
    }

    cout << "Case #" << iii << ": " << result << endl;
  }

  return 0;
}
