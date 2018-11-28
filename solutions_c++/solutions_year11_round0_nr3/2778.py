#include <iostream>

using namespace std;

// ./a.out < XXX.in.txt > XXX.out.txt

int main() {
  // read in the number of test cases
  int T;
  cin >> T;

  // read in data for test cases
  for(int test=1; test<=T; test++) {
    int N;
    cin >> N;
    size_t patrick=0;
    int min=1000000, sum=0;
    for(int i=0; i<N; i++) {
      int c;
      cin >> c;
      patrick^=c;
      min = (min<c) ? min : c;
      sum += c;
    }
    if(patrick!=0)  cout << "Case #" << test << ": NO" << endl;
    else
      cout << "Case #" << test << ": " << (sum-min) << endl;
  }

  return 0;
}

