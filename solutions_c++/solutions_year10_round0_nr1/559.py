#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
using namespace std;


int main() {
  int T, N, K;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cin >> N >> K;
    cout << "Case #" << i << ": " << (((K+1) % (1 << N))?"OFF":"ON") << endl;
  }
}
