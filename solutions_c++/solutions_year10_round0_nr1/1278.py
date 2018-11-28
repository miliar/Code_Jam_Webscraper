#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <cmath>
#include <queue>
#include <list>

using namespace std;
int main() {
  long long T, K, N;
  int c = 1;
  cin>>T;
  while(c <= T) {
    cin >> N >> K;
    cout << "Case #" << c <<": ";
    bool t = true;
    long long a = 1;
    while(a <= (1LL << (N-1))) {
      if (!(a & K)) {
        t = false;
      }
      a <<= 1;
    }
    if (t) {
      cout << "ON";
    } else {
      cout << "OFF";
    }
    cout << endl;
    c++;
  }
}
