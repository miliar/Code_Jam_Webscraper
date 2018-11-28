#include <iostream>
#include <iomanip>
#include <sstream>

#include <cmath>
#include <algorithm>

#include <map>
#include <vector>

using namespace std;


#define PI acos(-1.)
#define EPS 1e-7

#define NMAX 30
#define KMAX 100000000


int main() {
  // Declare members
  uint32_t num_case;
  cin >> num_case;

  uint32_t N;
  uint32_t K;

  vector<uint32_t> vect;
  vect.resize(NMAX, 0);
  vect[1] = 1;
  for (int i = 2; i <= NMAX; i++) {
    vect[i] = vect[i - 1]*2 + 1;
  }

  for (int j = 1; j <= num_case; j++) {
    // Init members
    cin >> N >> K;
    string out;
    if (K%(vect[N]+1) == vect[N]) {
      out = "ON";
    } else {
      out = "OFF";
    }
    
    // Print output for case j
    cout << "Case #" << j << ": " << out << endl;
  }


  return 0;
}
