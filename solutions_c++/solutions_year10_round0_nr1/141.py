// snapper
// srh
#include <iostream>

/*
I keep doing this for hours. Will the light be on or off after I have snapped my fingers K times? The light is on if and only if it's receiving power from the Snapper it's plugged into.
*/

int main() {

  /*
    Input

    The first line of the input gives the number of test cases, T.
  */
  // 1 <= T <= 10000
  long T;
  std::cin >> T;

  /*
    T lines follow.
  */
  for (long i = 1; i <= T; ++i) {
    /*  Each one contains two integers, N and K. */
    // 1 <= N <= 30
    long N;
    std::cin >> N;
    // 0 <= K <= 10^8
    long K;
    std::cin >> K;
    /*
      Output

      For each test case, output one line containing "Case #x: y", where
      x is the case number (starting from 1) and y is either "ON" or
      "OFF", indicating the state of the light bulb.
    */

    // N devices, K snaps

    // Power is at the end of the Nth device if the first N devices
    // are on.  That is, if K = -1 (mod 2^N).

    long minusOne = ((1 << N) - 1);
    long bulbOn = ((K & minusOne) == minusOne);

    std::cout << "Case #" << i << ": " << (bulbOn ? "ON" : "OFF") << "\n";
  }
}
