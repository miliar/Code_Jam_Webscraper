#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;

  int N;
  int total;
  int allxor;
  int smallest;
  int next;
  
  for (int t=1; t<=T; t++) {
    total = 0;
    allxor = 0;
    smallest = 1000001;

    cin >> N;
    for (int j=0; j<N; j++) {
      cin >> next;
      allxor = allxor xor next;
      total += next;
      smallest = (smallest > next)? next : smallest;
    }
    cout << "Case #" << t << ": ";
    if(allxor == 0) {
      cout << total-smallest;
    } else {
      cout << "NO";
    }
    cout << endl;
  }
}
