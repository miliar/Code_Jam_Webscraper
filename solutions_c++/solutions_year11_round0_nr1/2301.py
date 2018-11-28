#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define CLEAR(a) memset(a, 0, sizeof(a))

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int C = 1; C <= T; C++) {
	  int t = 0;
	  int pa = 1;
	  int pb = 1;
	  int ta = 0;
	  int tb = 0;
	  int n, p, s;
	  char c;
	  for (cin >> n; n; n--) {
		  cin >> ws >> c >> p;
		  switch (c) {
			  case 'O' : s = abs(pa-p)+1; 
						 if (ta+s > t)
							 t = ta+s;
						 else
							 t = t+1;
						 ta = t;
						 pa = p;
						 break;
			  case 'B' : s = abs(pb-p)+1; 
						 if (tb+s > t)
							 t = tb+s;
						 else
							 t = t+1;
						 tb = t;
						 pb = p; 
						 break;
			  default : cerr << "zle je" << endl;
		  }
	  }

    cout << "Case #" << C << ": " << t << endl;
  }
}
