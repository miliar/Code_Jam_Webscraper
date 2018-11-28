// Actual code is in the very bottom of the file.

// template.hpp starts
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <typeinfo>
using namespace std;

typedef long long i64;

int next(int *dummy = 0) {
  int t;
  scanf("%d", &t);
  return t;
}

string next(string *dummy = 0) {
  char t[1000];
  scanf("%s", t);
  return string(t);
}

i64 next(i64 *dummy = 0) {
  i64 t;
  scanf("%lld", &t);
  return t;
}

double next(double *dummy = 0) {
  double t;
  scanf("%lf", &t);
  return t;
}

template<class T>
vector<T> nextVector(int n, T *dummy = 0) {
  vector<T> ans(n);
  for (int i = 0; i < n; ++i) {
    ans[i] = next((T*)0);
  }
  return ans;
}

int nextInt() {
  return next((int *) 0);
}

string next() {
  return next((string *) 0);
}

i64 nextLong() {
  return next((i64 *) 0);
}

double nextDouble() {
  return next((double *) 0);
}

vector<int> nextVectorInt(int n) {
  return nextVector(n, (int*) 0);
}

vector<double> nextVectorDouble(int n) {
  return nextVector(n, (double*) 0);
}

vector<i64> nextVectorLong(int n) {
  return nextVector(n, (i64*) 0);
}

vector<string> nextVectorString(int n) {
  return nextVector(n, (string*) 0);
}


void print(int x) {
  printf("%d", x);
}

void print(i64 x) {
  printf("%lld", x);
}

void print(string x) {
  printf("%s", x.c_str());
}

void print(double x) {
  printf("%lf", x);
}

template<class T1, class T2>
void print(pair<T1, T2> &x) {
  printf("(");
  printf(x.first);
  printf(", ");
  printf(x.second);
  printf(")");
}


typedef char True;
typedef long long False;

template<typename T>
True hasIteratorCheck(T * t, typename T::iterator* dummy = 0) { }

template<typename T>
False hasIteratorCheck(void *) { }

template<typename T>
struct HasIterator {
  static const bool value = sizeof(hasIteratorCheck<T>((T*)0)) == sizeof(True);
};

template <bool B>
struct EnableIf {
  typedef char type;
};

template <>
struct EnableIf<false> {};

template <bool B>
struct DisableIf {
  typedef char type;
};

template <>
struct DisableIf<true> {};

template <class T>
void _smart_print(T x, typename DisableIf<HasIterator<T>::value>::type* dummy = 0) {
  print(x.to_s());
}  

template <class T>
void _smart_print(T x, typename EnableIf<HasIterator<T>::value>::type* dummy = 0) {
  printf("[");
  for (typename T::iterator i = x.begin(); i != x.end(); ++i) {
    if (i == x.begin()) {
      printf(" ");
    } else {
      printf(", ");
    }
    print(*i);
  }
  printf(" ]"); 
}

template <class T>
void print(T t) {
  _smart_print(t);
}

template <class T>
void println(T t) {
  print(t);
  printf("\n");
}
/// template.hpp ends

/// multitest_by_n.hpp starts
void solve(int testN = 0);

int main() {
  int tN = nextInt();
  for (int testN = 1; testN <= tN; ++testN) {
    solve(testN);
  }
  return 0;
}
/// multitest_by_n.hpp ends

/// Proble source:




void solve(int testN) {
  printf("Case #%d:\n", testN);
  //ToDo --- code here.
  int n  = nextInt();
  vector<string> table = nextVectorString(n);
  vector<double> wp(n);
  vector<double> owp(n);
  vector<double> oowp(n);
  vector<double> rpi(n);
  vector<int> nplayed(n);
  for (int i  = 0; i < n; ++i) {
    int tot = 0;
    int win = 0;
    for (int j =  0; j < n; ++j) {
      if (table[i][j] != '.') {
	++nplayed[i];
      }
      if (table[i][j] == '1') {
	++win;
      }
    }
    wp[i] = win / (double) nplayed[i];
  }
  //  println(wp);
  for (int i = 0; i < n; ++i) {
    double cowp = 0;
    for (int j =  0; j < n; ++j) {
      if (table[i][j] != '.') {
	cowp += (wp[j] * nplayed[j] - (1 - table[i][j] + '0')) / (nplayed[j] - 1);
      }
    }
    owp[i] = cowp / (double) nplayed[i];
  }

  for (int i = 0; i < n; ++i) {
    double coowp = 0;
    for (int j =  0; j < n; ++j) {
      if (table[i][j] != '.') {
	coowp += owp[j];
      }
    }
    oowp[i] = coowp / (double) nplayed[i];
  }

  for (int i = 0; i < n; ++i) {
    rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
  }

  for (int i = 0; i < n; ++i) {
    println(rpi[i]);
  }
}




///Eof
