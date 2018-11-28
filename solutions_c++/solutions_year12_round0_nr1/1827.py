#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <numeric>
#include <utility>

using namespace std;

const string in[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
		      "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		      "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
const string out[3] = {"our language is impossible to understand",
		       "there are twenty six factorial possibilities",
		       "so it is okay if you want to just give up"};

int main(void) {
  map <char, char> i2o;
  set <char> iseen, oseen;
  for (int i = 0; i < 3; i++)
    for (int j = 0; j < (int) in[i].length(); j++) {
      i2o[in[i][j]] = out[i][j];
      iseen.insert(in[i][j]);
      oseen.insert(out[i][j]);
    }
  cerr << i2o.size() << endl;
  for (char c = 'a'; c <= 'z'; c++) {
    if (!iseen.count(c)) cerr << "not iseen: " << c << endl;
    if (!oseen.count(c)) cerr << "not oseen: " << c << endl;
  }
  i2o['z'] = 'q';
  i2o['q'] = 'z';
  
  int T; cin >> T;
  string s; getline(cin, s);
  for (int t = 1; t <= T; t++) {
    getline(cin, s);
    for (int i = 0; i < (int) s.length(); i++)
      s[i] = i2o[s[i]];
    printf("Case #%d: %s\n", t, s.c_str());
  }
}
