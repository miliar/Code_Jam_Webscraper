#include <iostream>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

typedef unsigned long long MY_UINT; 
typedef long long MY_INT;
#define MAX_D 13

enum {
  OP_NONE = 0,
  OP_ADD,
  OP_SUB,
  OP_LAST
};

static bool is_debug = getenv("MYDEBUG") != NULL;

template <class DST, class SRC>
static DST lexical_cast(const SRC &src)
{
  stringstream ss;
  ss << src;
  DST r;
  ss >> r;
  return r;
}

static inline bool is_ugly(MY_INT n)
{
  if (is_debug)
    cout <<"n="<<n<<endl;
  n = abs(n);
  return n == 0 || n % 2 == 0 || n % 3 == 0 || n % 5 == 0|| n % 7 == 0;
}

static MY_INT do_op(int op, MY_INT a, MY_INT b)
{
  switch (op) {
  case OP_ADD:
    return a+b;
  case OP_SUB:
    return a-b;
  }
}
static MY_INT eval(unsigned nof_digits, const char *exp)
{
  MY_INT prev = 0, cur = 0;
  int last_op = OP_ADD;

  for (unsigned i =0 ; i < nof_digits; i++) {
    cur *= 10;
    cur += exp[i*2]-'0';

    if (exp[i*2+1] != OP_NONE || i == nof_digits-1) {
      prev = do_op(last_op, prev, cur);
      cur = 0;
      last_op = exp[i*2+1];
    }
  }

  return prev;
}

unsigned count = 0;
static void go(unsigned nof_digits, unsigned rest_nof_digits, char *cur_digit, char *digits, MY_INT &sum)
{

  if (rest_nof_digits == 1) {
    ::count++;
    //cout << "count=" << ::count << endl;
    if (is_debug) {
      
      const char* dig2str[OP_LAST] = {"", "+", "-"};
      cout << "per:" << endl;
      for (unsigned i = 0; i < nof_digits; i++)
	cout <<digits[i*2] << dig2str[digits[i*2+1]];
      cout << endl;
    }

    if (is_ugly(eval(nof_digits, digits)))
	sum++;
    return;
  }

  for (int i = 0; i < OP_LAST; i++) {
    cur_digit[1] = i;
    go(nof_digits,rest_nof_digits-1, cur_digit+2, digits, sum);
  }
}

MY_INT compute(const string &line)
{
  if (is_debug) {
    cout << "in:" << line << endl;
  }

  char digits[MAX_D*2];
  unsigned count = 0;
  unsigned nof_digits = line.size();
  memset(digits, 0, sizeof(digits));
  for (unsigned i = 0; i < nof_digits; i++)
    digits[i*2] = line[i];

  MY_INT sum = 0;
  go(nof_digits, nof_digits, digits, digits, sum);
  return sum;

}


int main(int argc, char **argv)
{
  string line;
  unsigned nof_cases;

  getline(cin, line);
  nof_cases = lexical_cast<unsigned>(line);
  unsigned case_ = 1;
  while (case_ <= nof_cases) {
    getline(cin, line);
    ::count = 0;
    cout << "Case #"<< case_++ << ": " << compute(line) << endl;
  }

  return 0;
}

