#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string>

using namespace std;

#define PI acos(-1.)
#define EPS 1e-7
#define LL long long



int main() {
  // Declare members
  int num_case;
  cin >> num_case;

  for (int j = 1; j <= num_case; j++) {
    // Init members
    int num_b;
    cin >> num_b;

    string bot;
    int num;

    int pb = 1;
    int po = 1;

    int tb = 0;
    int to = 0;
    int res = 0;

    for (int i = 0; i < num_b; i++) {
      cin >> bot;
      cin >> num;

      if (bot == "O") {
	int t = abs(po - num) + 1;
	if (t > to) {
	  res += t - to;
	  tb += t - to;
	} else {
	  tb = 1;
	  res += 1;
	}
	po = num;
	to = 0;
      } else {
	int t = abs(pb - num) + 1;
	if (t > tb) {
	  res += t - tb;
	  to += t - tb;
	} else {
	  to = 1;
	  res += 1;
	}
	pb = num;
	tb = 0;
      }
    }

    // Print output for case j
    cout << "Case #" << j << ": " << res << endl;
  }


  return 0;
}
