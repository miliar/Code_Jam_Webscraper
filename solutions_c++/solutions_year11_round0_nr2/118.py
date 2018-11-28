#include <iostream>
#include <cstdio>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <sstream>

#define F(i,a,b) for(int i=a;i<b;++i)
#define rep(i,b) F(i,0,b)
#define all(a) a.begin(),a.end()

using namespace std;

int main() {
  int T;
  scanf("%d", &T);
  rep(t, T) {
    int C, D, N;
    scanf("%d", &C);
    map<set<char>, char> rxns;
    rep(c, C) {
      char buf[3];
      scanf(" %s ", buf);
      set<char> x;
      x.insert(buf[0]);
      x.insert(buf[1]);
      rxns[x] = buf[2];
    }
    scanf("%d", &D);
    set<pair<char, char> > opposed;
    rep (d, D) {
      char buf[2];
      scanf(" %s ", buf);
      opposed.insert(pair<char, char>(buf[0], buf[1]));
    }
    scanf("%d", &N);
    char seq[N];
    scanf(" %s ", seq);

    deque<char> res;

    rep(i, N) {
      res.push_back(seq[i]);
      // attempt rxn
      if (res.size() > 1) {
        set<char> lookup;
        lookup.insert(*(res.rbegin()));
        lookup.insert(*(res.rbegin()+1));
        if (rxns.find(lookup) != rxns.end()) {
          res.pop_back();
          res.pop_back();
          res.push_back(rxns[lookup]);
        }

        set<char> chars(res.begin(), res.end());

        for (set<pair<char, char> >::iterator it = opposed.begin();
            it != opposed.end();
            ++it) {
          if (chars.find(it->first) != chars.end() &&
              chars.find(it->second) != chars.end()) {
            res.clear();
          }
        }
      }
    }


    stringstream ret;
    if (res.size() == 0) {
      ret << "[]";
    } else {
      deque<char>::iterator it = res.begin();
      ret << "[" << *it;
      for (++it; it != res.end(); ++it) {
        ret << ", " << *it;
      }
      ret << "]";
    }
    printf("Case #%d: %s\n", t+1, ret.str().c_str());
  }
}
