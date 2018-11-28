#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv) {
  ifstream ifs(argv[1]);
  ofstream ofs(argv[2]);

  unsigned T = 0;
  ifs >> T;

  for (unsigned t = 0; t < T; ++t) {
    unsigned N = 0;
    ifs >> N;
    unsigned min = unsigned(-1);
    unsigned sum = 0;
    unsigned patSum = 0;
    for (unsigned n = 0; n < N; ++n) {
      unsigned c;
      ifs >> c;
      if (c < min) min = c;
      sum += c;
      patSum ^= c; 
    }

    // Output.
    ofs << "Case #" << t + 1 << ": ";
    if (patSum) {
      ofs << "NO" << endl;
      continue;
    }
    ofs << sum - min << endl;
  }

  return 0;
}
