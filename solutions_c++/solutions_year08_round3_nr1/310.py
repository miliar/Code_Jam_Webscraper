#include <cassert>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <stdint.h>

#define MAX_P 1000
#define MAX_K 1000
#define MAX_L 1000

typedef uint64_t MY_UINT;

using namespace std;

typedef pair<MY_UINT, MY_UINT> letter;
template <class DST, class SRC>
static DST lexical_cast(const SRC &src)
{
  stringstream ss;
  ss << src;
  DST r;
  ss >> r;
  return r;
}


static bool letter_greater(const letter& a, const letter& b)
{
  return a.second > b.second;
}

MY_UINT  compute(MY_UINT P, MY_UINT K, MY_UINT L, MY_UINT *FREQ)
{

  if (getenv("MYDEBUG")) {
    cout << "P=" <<P << " K="<<K<<" L="<<L << endl;
    cout <<"FREQ=";
    for (MY_UINT i = 0; i < L; i++)
      cout <<FREQ[i]<< " ";
    cout << endl;
  }

  letter letters[MAX_L];
  for (MY_UINT i = 0; i < L; i++)
    letters[i] = make_pair(i, FREQ[i]);

  sort(letters, letters+L, letter_greater);

  if (getenv("MYDEBUG")) {
    cout << "letters" << endl;
    for (MY_UINT i = 0; i < L; i++)
      cout << letters[i].first << " " << letters[i].second << endl;
  }

  map<MY_UINT, MY_UINT> letter2count;

  MY_UINT l = 0;
  for (MY_UINT p = 0; p < P; p++)
    for (MY_UINT k = 0; k < K; k++) {
      if (getenv("MYDEBUG"))
	cout << "l=" << l << endl;
      assert(letter2count.find(letters[l].first) == letter2count.end());
      letter2count[letters[l++].first] = p+1;
      if (l == L)
	goto end;
    }

 end:
  MY_UINT sum = 0;
  for (MY_UINT i = 0; i < L; i++)
    sum += letter2count[i]*FREQ[i];
    
  return sum;
}

void read_P_K_L(MY_UINT &P, MY_UINT &K, MY_UINT &L)
{
  string line;
  getline(cin, line);
  istringstream is(line);
  is >> P >> K >> L;
}

void read_FREQ(MY_UINT L, MY_UINT *FREQ)
{
  string line;
  getline(cin, line);
  istringstream is(line);
  for (MY_UINT i = 0; i < L; i++)
    is >> FREQ[i];
}

int main(int argc, char **argv)
{
  string line;
  MY_UINT nof_cases;

  getline(cin, line);
  nof_cases = lexical_cast<MY_UINT>(line);
  MY_UINT case_ = 1;
  while (case_ <= nof_cases) {
    MY_UINT P, K, L;
    MY_UINT FREQ[MAX_L];
    read_P_K_L(P,K,L);
    read_FREQ(L, FREQ);
    cout << "Case #"<< case_++ << ": " << compute(P,K,L,FREQ) << endl;
  }

  return 0;
}

