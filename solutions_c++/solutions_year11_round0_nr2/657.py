#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

const char basic[] = "QWERASDF";

char combine[100][100];
char destroy[100][100];

int main(void)
{
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    vector <int> freqs(100);
    memset(combine, 0, sizeof(combine));
    memset(destroy, 0, sizeof(destroy));
    int C; cin >> C;
    for (int c = 0; c < C; c++) {
      string s; cin >> s;
      combine[s[0]][s[1]] = s[2];
      combine[s[1]][s[0]] = s[2];
    }
    int D; cin >> D;
    for (int d = 0; d < D; d++) {
      string s; cin >> s;
      destroy[s[0]][s[1]] = 1;
      destroy[s[1]][s[0]] = 1;
    }
    string input;
    int L; cin >> L;
    cin >> input;
    string output = input;
    int len = 0;
    for (int i = 0; i < L; i++) {
      if (len) {
	if (combine[output[len-1]][input[i]]) {
	  char out = combine[output[len-1]][input[i]];
	  freqs[output[len-1]]--;
	  freqs[out]++;
	  output[len-1] = out;
	  goto done;
	}
	else {
	  for (int k = 0; k < 8; k++)
	    if (freqs[basic[k]] && destroy[basic[k]][input[i]]) {
	      for (int k2 = 0; k2 < 8; k2++)
		freqs[basic[k2]] = 0;
	      len = 0;
	      goto done;
	    }
	}
      }
      freqs[input[i]]++;
      output[len++] = input[i];
    done:;
    }
    printf("Case #%d: [", t);
    for (int i = 0; i < len; i++) {
      if (i > 0) printf(", ");
      printf("%c", output[i]);
    }
    printf("]\n");
  }
}
