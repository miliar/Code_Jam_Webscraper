#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

typedef vector<int> VI;

void run(istream& in, ostream& ou, int c) {
  int T, S, p;
  VI v;
  in >> T >> S >> p;
  for (int i = 0; i < T; ++i) {
    int pt;
    in >> pt;
    v.push_back(pt);
  }

  // sort
  sort(v.rbegin(), v.rend());

  int count = 0;
  for (VI::iterator i = v.begin(); i != v.end(); ++i) {
    int r = *i % 3;
    int avg = *i / 3;
    if (avg >= p) {
      count++;
    } else if ((avg == p - 1) && (r > 0) && (p - 1 >= 0)) {
      count++;
    } else if ((avg == p - 1) && (r == 0)) {
      if ((S > 0) && (p - 2 >= 0) ) {
        count++;
        S--;
      }
    } else if ((avg == p - 2) && (r > 1)) {
      if (S > 0 && (p - 2 >= 0)) {
        count++;
        S--;
      }
    }
  }
  ou << "Case #" << c << ": " << count << endl;
}

int main(int argc, char** argv) {
  ifstream in(argv[1]);
  int cases;
  in >> cases;
  for (int i = 0; i < cases; ++i) {
    run(in, cout, i+1);
  }
}
