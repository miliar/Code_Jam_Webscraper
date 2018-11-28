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
  scanf("%c", t);
  return t;
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
void print(T t);

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


int pow(int x, int y) {
  int ans  = 1;
  for (int i =  0; i < y; ++i) {
    ans *= x;
  }
  return ans;
}

void solve(int testN) {
  //ToDo --- code here.
  printf("Case #%d: ", testN);
  int n = nextInt();
  int m = nextInt();
  vector<int> from = nextVectorInt(m);
  vector<int> to = nextVectorInt(m);
  for (int i  = 0; i < m; ++i) {
    --from[i];
    --to[i];
  }
  set< set<int> > verticesS;
  for (int i = 0; i < n; ++i) {
    set<int> cur;
    for (int j = 0; j < n; ++j) {
      bool sameside = true;
      for (int w = 0; w < m; ++w) {
	bool ok = true;
	if (j != from[w] && j != to[w]) {
	  for (int c1 = (from[w] + 1) % n; c1 !=to[w]; ++c1, c1 %= n) {
	    if (c1 == i) {
	      ok = !ok;
	    }
	    if (c1 == j) {
	    ok = !ok;
	    }
	  }
	}
	if (!ok) {
	  sameside = false;
	  break;
	}
      }
      if (sameside) {
	cur.insert(j);
      }
    }
    verticesS.insert(cur);
  }

  vector< vector<int> > vertices;
  for (set< set<int> >::iterator i = verticesS.begin(); i != verticesS.end(); ++i) {
    vertices.push_back(vector<int>());
    for (set<int>::iterator j = i->begin(); j != i->end(); ++j) {
      vertices.back().push_back(*j);
    }
  }
  vector<int> color(n);
  vector<int> lastgood;
  for (int nc = 1; nc <= n; ++nc) {
    int max = pow(nc, n);
    bool good = false;
    for (int imask = 0; imask < max; ++imask) {
      int mask = imask;
      for (int p = 0; p < n; ++p) {
	color[p] = mask % nc;
	mask /= nc;
      }
      
      // check
      bool ok = true;
      for (int i = 0; i < vertices.size(); ++i) {
	for (int col = 0; col < nc; ++col) {
	  bool was = false;
	  for (int j = 0; j < vertices[i].size(); ++j) {
	    if (color[vertices[i][j]] == col) {
	      was = true;
	      break;
	    }
	  }
	  if (!was) {
	    ok = false;
	    break;
	  }
	}
      }
      if (ok) {
	good = true;
	lastgood = color;
	break;
      }
    }
    if (!good) {
      println(nc - 1);
      for (int i = 0; i < n; ++i) {
	print(lastgood[i] + 1);
	print(string(" "));
      }
      println(string(""));
      return;
    }
  }
}




///Eof
