#include<iostream>
#include<cmath>

using namespace std;

int main() {
  int T;
  long long N,K, power[32];
  bool on =false;
  cin >> T;
  for (int i=0; i<32; i++)
    power[i] = (long long) pow(2.0,i);
  for (int t=1; t<=T; t++) {
    cin >> N >> K;
    on = (((K+1) % power[N]) == 0);
    if (K==0) on = false;
    if (on) {
      cout << "Case #" << t << ": " << "ON" << endl;
    } else {
      cout << "Case #" << t << ": " << "OFF" << endl;
    }
  }
}
