#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <cstdio>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t < T+1; ++t) {
    cout << "Case #" << t << ":" << endl;

    int R, C;
    cin >> R >> C;

    vector<string> pic(R);
    for (int i = 0; i < R; ++i)
      cin >> pic[i];

    for (unsigned int i = 0; i < pic.size(); ++i) {
      for (unsigned int j = 0; j < pic[i].size(); ++j) {
	if (pic[i][j] == '#') {
	  if ((j+1 < pic[i].size() && pic[i][j+1] == '#') &&
	      (i+1 < pic.size() && pic[i+1][j] == '#') &&
	      (pic[i+1][j+1] == '#')) {
	    pic[i][j] = pic[i+1][j+1] = '/';
	    pic[i][j+1] = pic[i+1][j] = '\\';
	  }
	}
      }
    }

      bool possible = true;
      for (unsigned int i = 0; i < pic.size(); ++i) {
	if (pic[i].find("#", 0) != string::npos) {
	  possible = false;
	  break;
	}
      }

      if (possible) {
	for (unsigned int i = 0; i < pic.size(); ++i)
	  cout << pic[i] << endl;
      } else {
	cout << "Impossible" << endl;
      }

  }
  return 0;
}
