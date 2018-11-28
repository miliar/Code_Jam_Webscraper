#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
//#include <list>
#include <set>
#include <sstream>

#include <cstdio>
#include <cstring>
#include <climits>
#include <cassert>

#define FOR(i,s,n) for (int i = (int)(s); i < (int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define MP make_pair
#define cerr if (0) cerr

using namespace std;

#define signum(v) (v > 0 ? +1 : (v < 0 ? -1 : 0))

bool match_destroy_rule(const vector<char>& list, const string& rule, int& pos) 
{
  const char NotFound = '#';
  char last = list.back();
  char opposed = NotFound;
  if (rule[0] == last) {
    opposed = rule[1];
  } else if (rule[1] == last) {
    opposed = rule[0];
  }
  
  if (opposed == NotFound) return false;
  
  for (int i = list.size()-1; i >= 0; --i) {
    if (list[i] == opposed) {
      pos = i;
      return true;
    }
  }
  
  return false;
}

void destroy_pairs(vector<char>& list, const vector<string>& rules)
{
  if (list.size() <= 1) return;

  REP(i, rules.size()) {
    int pos = -1;
    if (match_destroy_rule(list, rules[i], pos)) {
      //list.erase(list.begin()+pos, list.end());
      list.clear();
      return;
    }
  }
}

bool match_combine_rule(const char c1, const char c2, const string& rule) 
{
  return ((c1 == rule[0] && c2 == rule[1]) ||
	  (c2 == rule[0] && c1 == rule[1]));
}

void combine_pairs(vector<char>& list, const vector<string>& rules)
{
  if (list.size() <= 1) return;

  REP(i, rules.size()) {
    if (match_combine_rule(list[list.size()-1],
			   list[list.size()-2],
			   rules[i])) {
      list.pop_back();
      list.pop_back();
      list.push_back(rules[i][2]);
      return;
    }
  }
}

string to_str(const vector<char>& list)
{
  if (list.empty()) return "[]";

  stringstream ss;
  ss << "[" << list[0];
  FOR(i, 1, list.size()) {
    ss << ", " << list[i];
  }
  ss << "]";
  
  return ss.str();
}

int main()
{
  int T, C, D, N;
  
  cin >> T;

  REP(i, T) {
    cin >> C;
    
    vector<string> combine;
    REP(j, C) {
      string str;
      cin >> str;
      combine.PB(str);
    }

    cin >> D;
    vector<string> destroy;
    REP(j, D) {
      string str;
      cin >> str;
      destroy.PB(str);
    }

    cin >> N;
    string elements;
    cin >> elements;
    
    vector<char> list;
    REP(pos, elements.length()) {
      list.PB(elements[pos]);
      combine_pairs(list, combine);
      destroy_pairs(list, destroy);
    }

    cout << "Case #" << i+1 << ": " << to_str(list) << endl;
  }
  
  return 0;
}
