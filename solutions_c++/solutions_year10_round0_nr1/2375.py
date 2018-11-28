#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>
using namespace std;

int main(int argc, char **argv)
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int N, K;

    cin >> N >> K;
    int light = 1;
    light = (light << N);
    if (K > light) {
      K = K % light;
    }

    bool ans = true;
    for (int j = 0; j < N; j++) {
      int a = (1<<j) & K;
      if (a > 0) {
        continue;
      } else {
        ans = false;
        break;
      }
    }
    string s = (ans == true) ? "ON" : "OFF";
    cout << "Case #" << i+1 << ": " << s << endl;
  }
  return 0;
}
