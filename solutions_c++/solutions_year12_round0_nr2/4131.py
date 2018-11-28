#include <array>
#include <iostream>

using namespace std;

int main (int argc, char* argv[])
{
  /**
   * Any number can be
   * 0 mod 3 => x, x+1, x+2 (*) or 3x
   * 1 mod 3 => x, x, x+1 or x, x+2, x+2 (*)
   * 2 mod 3 => x, x, x+2 (*) or x, x+1, x+1
   *
   * Always, try to maximize the max score possible
   * as that will imply a max value directly.
   *
   * If even the (*) version < p, just use the smaller version.
   * If even the smaller version > p, just use the smaller version.
   * If only the (*) version > p, then keep a count of the possibles used.
   */
    
  int T /* test cases */, N /* Googlers */, S /* Surprising */, p /* limit */, t /* score */;

  int i = 0, j, x, n;
  
  cin >> T;
  while (i++ < T) {
    cin >> N; cin >> S; cin >> p; j = 0; n = 0;
    while (j++ < N) {
      cin >> t;

      switch (t%3) {
        case 0:
          if (t/3 >= p) n++; // Unsurprising, still got the prize
          else if (t/3 + 1 >= p && t >= 3 && S > 0) {n++; S--;} // Surprising, got the prize
          break;
        case 1:
          if ((t-1)/3 + 1 >= p && t >= 1) n++; // Unsurprising, still got the prize
          else if ((t-1)/3 + 1 >= p && S > 0 && t >= 4) {n++; S--;} // Surprising, got the prize
          break;
        case 2:
          if ((t-2)/3 + 1 >= p && t >= 2) n++; // Unsurprising, still got the prize
          else if ((t-2)/3 + 2 >= p && S > 0 && t >= 2) {n++; S--;} // Surprising, got the prize
          break;
        default:
          cerr << "Math is broken.";
      }
    }

    cout << "Case #" << i << ": " << n << endl;
  }

  return 0;
}
