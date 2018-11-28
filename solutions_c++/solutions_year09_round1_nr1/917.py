#ifdef _MSC_VER
#pragma warning(disable:4996)
template<typename _Type>
int __builtin_popcount(_Type x) {
  static int count[256] = {
    0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8
  };
  int c = 0;
  while ( x ) {
    c += count[x & 0xFF];
    x >>= 8;
  }
  return c;
}
#endif
#include "string"
#include "limits"
#include "bitset"
#include "vector"
#include "queue"
#include "stack"
#include "list"
#include "map"
#include "set"
#include "algorithm"
#include "functional"
#include "numeric"
#include "utility"
#include "sstream"
#include "iostream"
#include "complex"
#include "stdio.h"
#include "float.h"
#include "math.h"
#include "stdlib.h"
#include "assert.h"
#include "stdarg.h"
#include "string.h"
#include "time.h"
#include "ctype.h"
using namespace std;

#define SIZE(N, V) int N = static_cast<int>((V).size())
#define GSIZE(N, V) (N) = static_cast<int>((V).size())
#define ALL(V) (V).begin(), (V).end()
#define UNIQUE(C) {sort(ALL(C)); C.resize(unique(ALL(C)) - C.begin());}
#define CAST(X, Y) {stringstream ss; ss << (X); ss >> (Y);}

#define READ_INT(X) scanf("%d", &(X))
#define READ_I64(X) scanf("%lld", &(X))
#define READ_STRING(X) scanf("%s", stringReader)
#define READ_VECTOR(X, N, T) { T ASDQWEASD; for ( int asdqweasd = 0; asdqweasd < N && cin >> ASDQWEASD; ++asdqweasd ) X.push_back(ASDQWEASD); }
#define READ_LINE(N) { N = 0; for ( char* ptr = stringReader; scanf("%c", ptr) == 1; ++ptr, ++N ) if ( *ptr == '\n' || *ptr == '\r' ) { *ptr = 0; break; } }
//#define READ_LINE() for ( char* ptr = stringReader; scanf("%c", ptr) == 1; ++ptr ) if ( *ptr == '\n' || *ptr == '\r' ) { *ptr = 0; break; }

typedef long long i64;
template<typename _Type>
_Type oo() { return numeric_limits<_Type>::has_infinity ? numeric_limits<_Type>::infinity() : (numeric_limits<_Type>::max() / 2); }
template<typename _Type>
bool oo(_Type x) { return x >= oo<_Type>(); }
const double eps = 1e-9;
const double bs_high = 1LL << numeric_limits<double>::digits;

#define FILE_NAME "xxx"

#define TEST_FILE

#ifndef _DEBUG
#define OUT_FILE
#endif

static char stringReader[2097152];

string fix(const string& s) {
  string res = s;
  sort(ALL(res));
  return res.substr(res.find_first_not_of("0"));
}

typedef map<string, bool> Memo;
Memo memo[11];
/*
struct Number {
  int base;
  string value;
  bool operator<(const Number& b) const {
    if ( value.size() == b.value.size() ) return value < b.value;
    return value.size() < b.value.size();
  }
  string times(int b) {
    string n;
    int carry = 0;
    for ( int i = 0, GSIZE(N, value); i < N; ++i ) {
      int res = (value[N - i - 1] - '0') * b + carry;
      n.push_back((res % base) + '0');
      carry = res / base;
    }
    reverse(ALL(n));
    return n;
  }
  Number operator*(const Number& b) const {
    Number small = operator <(b) ? *this : b;
    Number big = operator <(b) ? b : *this;
    for ( int i = 0, GSIZE(N, small.value); i < N; ++i ) {
    }
    return *this;
  }
  Number operator+(const Number& b) const {
    Number n;
    n.base = base;
    SIZE(N, value);
    SIZE(M, b.value);
    int carry = 0;
    for ( int i = 0; i < max(N, M); ++i ) {
      int va = 0;
      int vb = 0;
      if ( i < N ) va = value[N - i - 1] - '0';
      if ( i < M ) vb = b.value[M - i - 1] - '0';
      int res = va + vb + carry;
      n.value.push_back((res % base) + '0');
      carry = res / base;
    }
    if ( carry ) n.value.push_back(carry + '0');
    reverse(ALL(n.value));
    return n;
  }
};
*/
string sq(int d, int base) {
  int value = d * d;
  string res;
  if ( value >= base ) res.push_back((value / base) + '0');
  res.push_back((value % base) + '0');
  return res;
}
string add(const string& a, const string& b, int base) {
    string n;
    SIZE(N, a);
    SIZE(M, b);
    int carry = 0;
    for ( int i = 0; i < max(N, M); ++i ) {
      int va = 0;
      int vb = 0;
      if ( i < N ) va = a[N - i - 1] - '0';
      if ( i < M ) vb = b[M - i - 1] - '0';
      int res = va + vb + carry;
      n.push_back((res % base) + '0');
      carry = res / base;
    }
    if ( carry ) n.push_back(carry + '0');
    reverse(ALL(n));
    return n;
}
string apply(const string& number, int base) {
  string res;
  for ( int i = 0, GSIZE(N, number); i < N; ++i ) {
    string dsq = sq(number[i] - '0', base);
    res = add(res, dsq, base);
  }
  return res;
}
bool isHappy(const string& original, vector<string>& path, int base) {
  string number = fix(original);
  if ( number == "1" ) return true;
  Memo::const_iterator it = memo[base].find(number);
  if ( it != memo[base].end() ) return it->second;
  if ( find(ALL(path), number) != path.end() ) return memo[base][number] = false;
  path.push_back(number);
  bool next = isHappy(apply(number, base), path, base);
  return memo[base][number] = next;
}

string toBase(int n, int base) {
  string nb;
  while ( n ) {
    nb.push_back((n % base) + '0');
    n /= base;
  }
  reverse(ALL(nb));
  return nb;
}

int main() {
#ifdef TEST_FILE
  freopen(FILE_NAME".in", "rt", stdin);
#endif
#ifdef OUT_FILE
  freopen(FILE_NAME".out", "wt", stdout);
#endif
  int TESTS; scanf("%d\n", &TESTS);
  int test = 0;
  while ( test < TESTS ) {
    ++test;
    int N;
    READ_LINE(N);
    stringstream ss(stringReader);
    vector<int> bases;
    for ( int x; ss >> x; bases.push_back(x) );
    int sol = 1;
    bool ok = false;
    SIZE(B, bases);
    while ( !ok ) {
      ++sol;
      string ssol;
      ok = true;
      for ( int i = 0; i < B && ok; ++i ) {
        vector<string> path;
        ok = isHappy(toBase(sol, bases[i]), path, bases[i]);
      }
    }
    printf("Case #%d: %d\n", test, sol);
  }
  return 0;
}
