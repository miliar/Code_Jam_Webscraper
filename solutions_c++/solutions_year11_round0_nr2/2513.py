#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <string>
#include <set>
#include <vector>

#define N 105
#define MAX_CHAR 100

using namespace std;

namespace {

  struct rules {
    set<char> opposed[MAX_CHAR];
    char comb[MAX_CHAR][MAX_CHAR];

    rules() {
      memset(comb, 0, sizeof(comb));
    }

    void add_combination(char base1, char base2, 
			 char non_base) {
      comb[base1][base2] = non_base;
      comb[base2][base1] = non_base;
    }

    void add_opposed(char a, char b) {
      opposed[a].insert(b);
      opposed[b].insert(a);
    }

  };

  class element_list {
    rules* r;
    multiset<char> s;
    vector<char> v;
    
    void add(char e) {
      s.insert(e);
      v.push_back(e);
    }

    void pop() {
      s.erase(s.find(v.back()));
      v.pop_back();
    }

    bool is_opposed() const {
      if (v.empty())
	return false;
      const set<char>& o = r->opposed[v.back()];
      for (set<char>::const_iterator it = o.begin(), end = o.end();
	   it != end; ++it)
	if (s.find(*it) != s.end())
	  return true;
      return false;
    }

    void clear() {
      s.clear();
      v.clear();
    }

    bool try_combine() {
      if (v.size() < 2)
	return false;
      char b1 = *--v.end();
      char b2 = *--(--v.end());
      char nb = r->comb[b1][b2];
      if (!nb)
	return false;
      pop();
      pop();
      add(nb);
      return true;
    }

  public:
    element_list(rules* r) : r(r) {}

    void append(char base) {
      add(base);
      while (try_combine()) {}
      if (is_opposed())
	clear();
    }

    string to_string() const {
      stringstream ss;
      ss << '[';
      for (size_t i = 0; i < v.size(); ++i) {
	if (i) ss << ", ";
	ss << v[i];
      }
      ss << ']';
      return ss.str();
    }
    
  };

  void solve(int test_case) {
    rules r;
    int c; scanf("%d", &c);
    for (int i = 0; i < c; ++i) {
      char s[4]; scanf("%s", s);
      r.add_combination(s[0], s[1], s[2]);
    }
    int d; scanf("%d", &d);
    for (int i = 0; i < d; ++i) {
      char s[3]; scanf("%s", s);
      r.add_opposed(s[0], s[1]);
    }

    element_list el(&r);
    char s[N + 1]; int n;
    scanf("%d%s", &n, s);
    for (int i = 0; i < n; ++i) {
      el.append(s[i]);
    }
    printf("Case #%d: %s\n", test_case, el.to_string().c_str());
  }
}

int main() {
  int n_tc; scanf("%d", &n_tc);
  for (int i = 1; i <= n_tc; ++i)
    solve(i);
  return 0;
}
