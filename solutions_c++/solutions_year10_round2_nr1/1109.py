#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <ext/hash_map>
#include <ext/hash_set>

using namespace std;
using namespace __gnu_cxx;

static bool debug = false;

struct Voidify {
  template<class T>
  void operator&(const T& a) { }
};

#define LOG() !debug ? (void) 0 : Voidify() & cerr

namespace __gnu_cxx {
  template <>
  class hash<std::string> {
  public:
    size_t operator()(const std::string& x) const {
      return __gnu_cxx::hash<const char*>()(x.c_str());
    }
  };
}

bool baseName(const string& s, string* base) {
  size_t idx = s.rfind('/');
  if (idx != string::npos && idx > 0) {
    *base = s.substr(0, idx);
    LOG() << "basename for: " << s << " -> " << *base << endl;
    return true;
  }
  LOG() << "no basename for: " << s << endl;
  return false;
}

int addRecursive(const string& dir, hash_set<string>* all) {
  if (all->find(dir) != all->end()) {
    return 0;
  }

  string base;
  int res = 0;
  if (baseName(dir, &base)) {
    res += addRecursive(base, all);
  }
  LOG() << "adding: " << dir << endl;
  all->insert(dir);
  return res + 1;
}

int main() {
  int T;
  cin >> T;

  for (int64_t cnum = 1; cnum <= T;  ++cnum) {
    cout << "Case #"  << cnum << ": ";

    int N, M;
    cin >> N >> M;
    hash_set<string> dirs;
    string s;
    for (int i = 0; i < N; ++i) {
      cin >> s;
      addRecursive(s, &dirs);
    }
    LOG() << "-------------------------" << endl;

    int sum = 0;
    for (int i = 0; i < M; ++i) {
      cin >> s;
      sum += addRecursive(s, &dirs);
    }

    cout << sum << endl;
  }
  return 0;
}
