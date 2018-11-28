#include <iostream>
using namespace std;

int main(int argc, char** argv)
{
  int tests = 0;
  cin >> tests;
  for (int i=0; i<tests; ++i) {
    int N;
    unsigned long long K;
    cin >> N >> K;
    bool* power = new bool[N];
    bool* state = new bool[N];
    for (int j=0; j<N; ++j) {
      power[j] = false;
      state[j] = false;
    }
    power[0] = true;
    for (unsigned long long j=0; j<K; ++j) {
      state[0] = !state[0];
      for (int k=1; k<N; ++k) {
        if (power[k]) {
          state[k] = !state[k];
        }
        power[k] = state[k-1] & power[k-1];
      }
    }
    cout << "Case #" << i+1 << ": ";
    if (power[N-1] && state[N-1]) {
      cout << "ON" << endl;
    } else {
      cout << "OFF" << endl;
    }
    delete[] power;
    delete[] state;
  }
  return 0;
}
