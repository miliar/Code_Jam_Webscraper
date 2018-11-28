#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

void check_opposed(const map<pair<char, char>, char> &r, vector<char> &o) {
  map<pair<char, char>, char>::const_iterator it;
  for(int i = 0; i < o.size() - 1; i++) {
    it = r.find(pair<char, char>(o[i], o.back()));
    if (it != r.end()) {
      o.clear();
      return;
    }
  }
}

string eval_list(istream &in) {
  string res = "";
  map<pair<char, char>, char> rules, opposed;
  vector<char> order;
  int c;
  char q, w, e;
  in >> c;
  for(; c > 0; c--) {
    in >> q >> w >> e;
    rules[pair<char, char>(q, w)] = e;
    rules[pair<char, char>(w, q)] = e;
  }
  in >> c;
  for(; c > 0; c--) {
    in >> q >> w;
    opposed[pair<char, char>(q, w)] = 0;
    opposed[pair<char, char>(w, q)] = 0;
  }
  in >> c;
  map<pair<char, char>, char>::iterator it;
  for(; c > 0; c--) {
    in >> q;
    order.push_back(q);
    if (rules.size() > 0) {
      while(order.size() > 1) {
        it = rules.find(pair<char, char>(order.back(), order[order.size() - 2]));
        if (it != rules.end() && (*it).second != 0) {
          order.pop_back();
          order.pop_back();
          order.push_back((*it).second);
        } else {
          break;
        }
      }
    }
    if (order.size() > 1 && opposed.size() > 0) check_opposed(opposed, order);
  }

  for(int i = 0; i < order.size(); i++) {
    res += order[i];
    if (i + 1 < order.size()) {
      res += ", ";
    } else {
      break;
    }
  }
  return res;
}

int main() {
  ifstream in("B.in");
  ofstream out("B.out");
  int t;
  in >> t;
  for (int i = 1; i <= t; i++) {
    out << "Case #" << i << ": [" << eval_list(in) << "]" << endl;
  }
  in.close();
  out.close();
  return 0;
}
