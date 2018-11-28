#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>

#define MAX_n 800
using namespace std;

template <class DST, class SRC>
static DST lexical_cast(const SRC &src)
{
  stringstream ss;
  ss << src;
  DST r;
  ss >> r;
  return r;
}

int compute(unsigned size, int *va, int *vb)
{
  sort(va, va+size);
  sort(vb, vb+size);
  reverse(vb, vb+size);
  int sum = 0;
  for (unsigned i = 0; i < size; i++)
    sum += va[i]*vb[i];

  return sum;
}

static void read_vector(unsigned size, int *vector)
{
  string line;
  getline(cin, line);
  istringstream is(line);
  for (unsigned i = 0; i < size; i++)
    is >> vector[i];
}

int main(int argc, char **argv)
{
  string line;
  unsigned nof_cases;

  getline(cin, line);
  nof_cases = lexical_cast<unsigned>(line);
  unsigned case_ = 1;
  while (case_ <= nof_cases) {
    unsigned vs;

    getline(cin, line);
    vs = lexical_cast<unsigned>(line);

    int va[MAX_n], vb[MAX_n];
    read_vector(vs, va);
    read_vector(vs, vb);
 
    cout << "Case #"<< case_++ << ": " << compute(vs, va, vb) << endl;
  }

  return 0;
}

