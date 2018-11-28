#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    int N, L, H;
    cin >> N >> L >> H;
    int freqs[10000];
    for(int i = 0; i < N; i++) {
      cin >> freqs[i];
    }
    int frequency = -1;
    for(int freq = L; freq <= H; freq++) {
      bool yes = true;
      for(int i = 0; i < N; i++) {
	if(freqs[i] % freq != 0 && freq % freqs[i] != 0) {
	  yes = false;
	  break;
	}
      }
      if(yes) {
	frequency = freq;
	break;
      }
    }
    cout << "Case #" << t << ": ";
    if(frequency > 0) {
      cout << frequency << endl;
    } else {
      cout << "NO" << endl;
    }
  }
}
