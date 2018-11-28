#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

#define  DEBUG

map<int, long> two_power_map;

void Initialize() {
  for (int i = 0; i <= 30; ++i) {
    two_power_map[i] = pow(static_cast<double>(2), i);
  }
}

int main() {
  Initialize();

  ifstream inf("A-large.in");
  // save input buffer of the stream
  streambuf* cin_buffer = cin.rdbuf();
  cin.rdbuf(inf.rdbuf());

  ofstream outf("A-large.out");
  // save output buffer of the stream
  streambuf* cout_buffer = cout.rdbuf();
  cout.rdbuf(outf.rdbuf());

  int t = 0;
  int n = 0;
  long k = 0;
  cin >> t;
  int i = 1;
  while (i <= t) {
    cin >> n >> k;
    long p = two_power_map[n];//pow(static_cast<double>(2), n);
    int d = (k + 1) % p;
    //    cout << "n=" << n << "\tk=" << k << "\td=" << d << endl;
    if (k == 0 || d > 0)
      cout << "Case #" << i << ": OFF" << endl;
    else
      cout << "Case #" << i << ": ON" << endl;
    ++i;
  }
  
  cin.rdbuf(cin_buffer);
  cout.rdbuf(cout_buffer);
  return 0;
}
