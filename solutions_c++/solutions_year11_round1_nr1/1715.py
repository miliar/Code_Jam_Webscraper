#include <iostream>

using namespace std;

// ./a.out < XXX.in.txt > XXX.out.txt

int main() {
  // read in the number of test cases
  int T;
  cin >> T;

  // read in data for test cases
  for(int test=1; test<=T; test++) {
    int N, Pd, Pg;
    cin >> N >> Pd >> Pg;
    if (Pd>0 && Pg==0)  cout << "Case #" << test << ": Broken" << endl;
    else if (Pd<100 && Pg==100) cout << "Case #" << test << ": Broken" << endl;
    else {
    int i=1;
    for (; i<=N; i++) {
      if (i*Pd % 100 == 0) { cout << "Case #" << test << ": Possible" << endl; break; }
    }
    if (i>N) cout << "Case #" << test << ": Broken" << endl;
    }
  }

  return 0;
}

