#include <iostream>
#include <cstdio>
using namespace std;

/*
  Check if buinum bit of number is set
  @bitnum: count 0 as first bit from right to left
  @number: check for the bit in this value
 */
bool nth_bit(unsigned number, int bitnum) {
  return (1<<bitnum) & number;
}

// bool is_on(unsigned number, int bitnum) {
//   unsigned k=0;
//   return ~((~k) << bitnum);
// }

int main() {
  int T=1;
  cin >> T;
  // cerr << "T: " << T;
  for(int i = 1; i<= T; i++) {
    unsigned N=10, K=60;
    cin >> N >> K;

    bool state = false;

    unsigned mask= ~0U;
    mask = ~(mask<<N);

    state = ((mask & K) == mask);
    // cout << "N: " << N << ", K: "<< K << " "
    //   // << endl
    //   ;
    
    cout << "Case #"<<i<<": "<< (state? "ON":"OFF")<<endl;
    
  }
}
