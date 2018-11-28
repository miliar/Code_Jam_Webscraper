#include <iostream>

using namespace std;

struct light {
  bool power;
  bool on;
};

int main() {
  int T, N, K;
  cin >> T;
  for ( int i = 0; i < T; i++ ) {
    cin >> N >> K;
    light lights[N];
    for ( int j = 0; j < N; j++ ) {
      lights[j].power = 0;
      lights[j].on = 0;
    }
    lights[0].power = 1;
    int farthestWithPower = 0;
    for ( int j = 0; j < K; j++ ) {
      for ( int kk = 0; kk <= farthestWithPower; kk++ ) {
        lights[kk].on = !lights[kk].on;
      }
      int l = 0;
      while ( lights[l].on ) l++;
      int m;
      for ( m = 0; m <= l; m++ ) {
        lights[m].power = 1;
      }
      for ( ; m <= farthestWithPower; m++ ) {
        lights[m].power = 0;
      }
      farthestWithPower = l;
    }
    if ( lights[N - 1].power && lights[N - 1].on ) {
      cout << "Case #" << i + 1 << ": ON" << endl;
    }
    else {
      cout << "Case #" << i + 1 << ": OFF" << endl;
    }
  }
  return 0;
}
