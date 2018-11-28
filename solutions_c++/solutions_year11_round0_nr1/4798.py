#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int testcase = 0; testcase < T; testcase++) {
    int N;
    cin >> N;
    int t = 0;
    int o = 1;
    int b = 1;
    int blank = 0;
    string prev = "";
    for (int i = 0; i < N; i++) {
      string r;
      int p;
      cin >> r >> p;

      if (r == "O") {
	int d = abs(p-o);
	if (r == prev) {
	  t += d + 1; // move and push
	  blank += d + 1;
	} else {
	  if (d <= blank) {
	    t += 1;
	    blank = 1;
	  } else {
	    t += d - blank + 1;
	    blank = d - blank + 1;
	  }
	}
	o = p;
      } else {
	int d = abs(p-b);
	if (r == prev) {
	  t += d + 1; // move and push
	  blank += d + 1;
	} else {
	  if (d <= blank) {
	    t += 1;
	    blank = 1;
	  } else {
	    t += d - blank + 1;
	    blank = d - blank + 1;
	  }
	}
	b = p;
      }
      prev = r;
    }
    cout << "Case #" <<  testcase + 1 << ": " << t << endl;
  }
}
