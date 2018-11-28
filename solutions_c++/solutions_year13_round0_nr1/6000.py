#include <algorithm>
#include <cassert>
#include <cstdio>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

#define ASSERT_ for (;;) {}
#define PII pair<int, int>

#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)
using namespace std;

string solve(string &vc) {
  // Draw or not finished?
  string retval = "Draw";
  REP(i, vc.length())
    if (vc[i] == '.')
      retval = "Game has not completed";

  // Horizontal
  REP(i,4){
    bool same = true;
    char first = vc[4 * i];
    if (first == '.')
      continue;
    REP(j,4){
      if (vc[4*i + j] != first){
        same = false;
        break;
      }
    }
    if (same){
      return string(1,first);
    }
  }

  // Vertical
  REP(i,4) {
    bool same = true;
    char first = vc[i];
    if (first == '.')
      continue;
    REP(j,4) {
      if (vc[i + 4*j] != first){
        same = false;
        break;
      }
    }
    if (same) {
      return string(1,first);
    }
  }

  // Diagonal
  // First
  bool same = true;
  char first = vc[0];
  if (first != '.') {
    REP(i, 4) {
      if (vc[5*i] != first){
        same = false;
        break;
      }
    }
    if (same)
      return string(1,first);
  }

  same = true;
  first = vc[3];
  if (first != '.') {
    REP(i,4){
      if (vc[3*(i+1)] != first) {
        same = false;
        break;
      }
    }
    if (same)
      return string(1,first);
  }

  return retval;
}

int main() {
  int ntestcase;
  scanf("%d\n", &ntestcase);
  for (int test_id = 1; test_id <= ntestcase; test_id++) {
    vector<char> vc;
    char dummy;
    REP(i,16) {
      scanf("%c\n", &dummy);
      vc.push_back(dummy);
    }
    string vco(vc.begin(), vc.end());
    replace(vco.begin(), vco.end(), 'T', 'O');
    string vcx(vc.begin(), vc.end());
    replace(vcx.begin(), vcx.end(), 'T', 'X');
    string answer = solve(vco);
    if (answer == "O") {
      answer = "O won";
    } else {
      answer = solve(vcx);
      if (answer == "X")
        answer = "X won";
    }

    printf("Case #%d: %s\n", test_id, answer.c_str());
  }

  return 0;
}
