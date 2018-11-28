#include <iostream>
using namespace std;

int main() {
  int problem;
  cin >> problem;

  for(int iii=0; iii<problem; iii++) {
    int n, k;
    cin >> n >> k;

    int num = 1 << n;
    bool result = k%num == num-1;
    cout << "Case #" << iii+1 << ": " << ((result) ? "ON" : "OFF") << endl;
  }

  return 0;
}
