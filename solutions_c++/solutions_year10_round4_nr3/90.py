#include <iostream>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;




int main() {
  int t;
  cin >> t;
  for (int casenum = 1; casenum <= t; ++casenum) {
    int r;
    cin >> r;

    set< pair<int, int> > bacts;  // false means dead last round
    set< pair<int, int> > fresh;  // true means kill

    typedef set< pair<int, int> >::iterator iter;
    
    for (int i = 0; i < r; ++i) {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;

      for (int j = x1; j <= x2; ++j) {
	for (int k = y1; k <= y2; ++k) {
	  bacts.insert(make_pair(j, k));
	}
      }

      for (int j = x1; j <= x2+1; ++j) {
	fresh.insert(make_pair(j, y1));
	fresh.insert(make_pair(j, y2+1));
      }
      for (int j = y1; j <= y2+1; ++j) {
	fresh.insert(make_pair(x1, j));
	fresh.insert(make_pair(x2+1, j));
      }
    }


    // now we simulate.

    int seconds = 0;

    while (!bacts.empty()) {
      set< pair<int, int> > newfresh;
      set< pair<int, int> > kills;
      set< pair<int, int> > inss;

      iter bend = bacts.end();
      for (iter p = fresh.begin(), e = fresh.end(); p != e; ++p) {
	pair<int, int> pair = *p;
	
	iter left = bacts.find(make_pair(pair.first-1, pair.second));
	iter right = bacts.find(make_pair(pair.first, pair.second-1));
	if (left == bend && right == bend) {
	  // kill...
	  kills.insert(pair);
	  newfresh.insert(make_pair(pair.first+1, pair.second));
	  newfresh.insert(make_pair(pair.first, pair.second+1));
	}
	if (left != bend && right != bend) {
	  inss.insert(pair);
	  newfresh.insert(make_pair(pair.first+1, pair.second));
	  newfresh.insert(make_pair(pair.first, pair.second+1));
	}
      }

      for (iter p = kills.begin(), e = kills.end(); p != e; ++p) {
	bacts.erase(*p);
      }
      for (iter p = inss.begin(), e = inss.end(); p != e; ++p) {
	bacts.insert(*p);
      }

      fresh.swap(newfresh);

      seconds++;
    }



    cout << "Case #" << casenum << ": ";
    cout << seconds;
    cout << endl;
  }
}
