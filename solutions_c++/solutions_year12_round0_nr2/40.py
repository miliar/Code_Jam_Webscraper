#include <stdint.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <limits>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
using namespace std;

#define CHECK(expression) {                                             \
  if (!(expression)) {                                                  \
    std::cerr << "CHECK failed at "                                     \
              << __FILE__ << ":" << __LINE__ << "!\n"                   \
              << "Expression: " << #expression << std::endl;            \
    std::abort();                                                       \
  }                                                                     \
}

#define ABORT(message) {                                                \
    std::cerr << "Aborted at "                                          \
              << __FILE__ << ":" << __LINE__ << "!\n"                   \
              << "Message: " << message << std::endl;                   \
    std::abort();                                                       \
}

#define all(v) (v).begin(),(v).end()
#define forint(i,c,d) for (int i=(c); i<=(d); ++i)
#define forall(i,V) for (int i=0; i<(V).size(); ++i)
#define foritr(itr,V) for(__typeof(V.end()) itr=V.begin(); itr!=V.end(); ++itr)
#define showall(v) { cerr<<#v<<": ";forall(i, v)cerr<<(v)[i]<<" ";cerr<<endl; }
#define showvar(x) { cerr<<#x<<" = "<<(x)<<endl; }

typedef long long int64;
template<class T> void CheckMin(T&a, const T&b) { if (b<a) a=b; }
template<class T> void CheckMax(T&a, const T&b) { if (a<b) a=b; }

inline
bool Eoln(std::istream &in) { return in.peek() == '\n' || in.peek() == EOF; }

inline
bool SeekEoln(std::istream &in) {
  int c(0);
  while ((c = in.peek()) != EOF &&
         (c == ' ' || c == '\t' || c == '\r')) in.get();
  return c == EOF || c == '\n';
}

inline
bool SeekEof(std::istream &in) {
  int c(0);
  while ((c = in.peek()) != EOF &&
         (c == ' ' || c == '\t' || c == '\r' || c == '\n')) in.get();
  return c == EOF ;
}

inline
void Readln(std::istream &in) {
  int c(0);
  do c = in.get(); while (c != '\n' && c != EOF);
}


string SetFile(string s) {
  while (!s.empty() && s[0] <= ' ' ) s.erase(0, 1);
  while (!s.empty() && s[s.size() - 1] <= ' ' ) s.erase(s.size() - 1) ;
  const string::size_type p = s.find('.') ;
  if (p != string::npos) s = s.substr(0, p);
  CHECK(freopen((s + ".in" ).c_str(), "r", stdin) != NULL); 
  CHECK(freopen((s + ".out").c_str(), "w", stdout) != NULL);
  return s;
}
