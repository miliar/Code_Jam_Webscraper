#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int casenum = 1; casenum <= t; ++casenum) {
    int n;
    cin >> n;

    vector< pair<int,int> > ab;
    for (int i = 0; i < n; ++i) {
      int a,b;
      cin >> a;
      cin >> b;
      ab.push_back(make_pair(a,b));
    }

    sort(ab.begin(), ab.end());

    int crosses = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j) {
	crosses += (ab[i].second > ab[j].second) ? 1 : 0;
      }
    }

    cout << "Case #" << casenum << ": ";
    cout << crosses;
    cout << endl;
  }
}
