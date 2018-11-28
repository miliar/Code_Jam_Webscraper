#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>

using namespace std;

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

int INF = 1000000;

int f[26];
int used[26];

string solve(const string& s) {
  string ans;
  rep(i, s.size()) {
    if(s[i] == ' ') {
      ans += ' ';
    }else {
      ans += 'a' + f[s[i] - 'a'];
    }
  }
  return ans;
}

void mapping(const string& s, const string& t) {
  rep(i, s.size()) {
    if(s[i] == ' ') {
      continue;
    }
    int in = s[i] - 'a';
    int out = t[i] - 'a';
    if(f[in] != -1 && f[in] != out) {
      cerr << in << " " << out << " " << f[in] << endl;
      throw "inconsistemnt";
    }
    f[in] = out;
    used[out] = 1;
  }
}

int main(){
  int t; scanf("%d\n", &t);
  rep(i, 26) {
    f[i] = -1;
    used[i] = 0;
  }
  mapping("y", "a");
  mapping("e", "o");
  mapping("q", "z");

  mapping("ejp mysljylc kd kxveddknmc re jsicpdrysi",
	  "our language is impossible to understand");
  mapping("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", 
	  "there are twenty six factorial possibilities");
  mapping("de kr kd eoya kw aej tysr re ujdr lkgc jv",
	  "so it is okay if you want to just give up");
  string unused_in;
  string unused_out;
  rep(i, 26) {
    if(used[i] == 0) {
      unused_in += 'a' + i;
    }
  }
  rep(i, 26) {
    if(f[i] == -1) {
      unused_out += 'a' + i;
    }
  }
  if(unused_in != "") {
    mapping(unused_out, unused_in);
  }

  for(int i = 1;i<=t;i++){
    string s; getline(cin, s);
    string ans = solve(s);
    cout << "Case #" << i << ": " << ans <<endl;
  }
  return 0;

}
