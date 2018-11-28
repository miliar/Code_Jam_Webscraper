#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
//#include <ios>
using namespace std;

int main(int argc, char** argv) {
  ifstream ifs(argv[1]);
  ofstream ofs(argv[2]);

  unsigned T = 0;
  ifs >> T;

  vector<unsigned> list;
  list.reserve(1000);
  for (unsigned t = 0; t < T; ++t) {
    unsigned N = 0;
    ifs >> N;

    list.clear();
    for (unsigned n = 0; n < N; ++n) {
      unsigned i;
      ifs >> i;
      list.push_back(i);
    }

    vector<unsigned> sorted(list);
    sort(sorted.begin(), sorted.end());

    unsigned numHold = 0;
    unsigned numInt = sorted.size();
    for (unsigned i = 0; i < numInt; ++i) {
      if (list[i] == sorted[i]) ++numHold;
    }

    float exp = (numInt - numHold);

    // Output.
    ofs << "Case #" << t + 1 << ": " << fixed << exp << endl;
  }

  return 0;
}
