#include <iostream>
#include <fstream>
#include <set>
#include <cassert>

using namespace std;

int num_digit(long n) {
  int c = 0;
  while (n > 0) {
    c++;
    n = n / 10;
  }
  return c;
}

long recycle(long n, int digit) {
  int d = num_digit(n);
  int d1 = d - digit, d0 = digit;
  assert(d1 > 0);
  assert(d0 > 0);
  long ten1 = 1, ten0 = 1;
  for (int i = 0; i < d1; ++i) ten1 *= 10;
  for (int i = 0; i < d0; ++i) ten0 *= 10;

  return (n % ten0) * ten1 + n / ten0;
}

void run(istream& in, ostream& ou, int c) {
  long min, max;
  int total = 0;
  int digits;
  in >> min >> max;
  digits = num_digit(min);
  for (long i = min; i <= max; ++i) {
    set<long> s;
    for (int d = 1; d < digits; ++d) {
      int r = recycle(i, d);
      if ((r > i) && (r <= max) && (s.find(r) == s.end())) {
        s.insert(r);
        //cout << i << " " << r << endl;
        total++;
      }
    }
  }
  ou<<"Case #"<<c<<": "<<total<<endl;
}

int main(int argc, char** argv) {
  ifstream in(argv[1]);
  int cases;
  in >> cases;
  for (int i = 0; i < cases; ++i) {
    run(in, cout, i+1);
  }
}
