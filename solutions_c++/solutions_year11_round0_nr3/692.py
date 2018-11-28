#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char **argv) {
  //Get number of cases
  int N;
  cin >> N;
  
  // Loop over each case
  for (int i=0; i<N; i++) {
    int T;
    cin >> T;

    int c[T];
    for (int j=0; j<T; j++) {
      cin >> c[j];
    }

    int sum = 0;
    for (int j=0; j<T; j++) {
      sum ^= c[j];
    }

    if (sum == 0) {
      sum = 0;
      sort(c, c+T);
      for (int j=1; j<T; j++) {
        sum += c[j];
      }
      cout << "Case #" << i+1 << ": " << sum << endl;
    } else {
      cout << "Case #" << i+1 << ": NO" << endl;
    }


    // Print output here
  
  }
    
  return 0;
}
