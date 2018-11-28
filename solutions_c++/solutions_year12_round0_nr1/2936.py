// Problem A. Speaking in Tongues.cpp : Defines the entry point for the console application.
//

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;

#define forab(i,a,b) for(int i = (a); i <= (int)(b); i++)
#define forn(i,n) for(int i = 0; i < (int)(n); i++)
// need declare it for vc, vc can not use <typeof> keyword
#define foreach(it,c) for(it = c.begin(); it != c.end(); ++it)

#define all(a) (a).begin(), (a).end()
#define sz(a) (int)(a).size()
#define zero(a) memset(a, 0, sizeof(a))

#define pb push_back
#define mp make_pair

int t;

map<char, char> maps;

void Init() {
  maps['a'] = 'y';
  maps['b'] = 'h';
  maps['c'] = 'e';
  maps['d'] = 's';
  maps['e'] = 'o';
  maps['f'] = 'c';
  maps['g'] = 'v';
  maps['h'] = 'x';
  maps['i'] = 'd';
  maps['j'] = 'u';
  maps['k'] = 'i';
  maps['l'] = 'g';
  maps['m'] = 'l';
  maps['n'] = 'b';
  maps['o'] = 'k';
  maps['p'] = 'r';
  maps['q'] = 'z';
  maps['r'] = 't';
  maps['s'] = 'n';
  maps['t'] = 'w';
  maps['u'] = 'j';
  maps['v'] = 'p';
  maps['w'] = 'f';
  maps['x'] = 'm';
  maps['y'] = 'a';
  maps['z'] = 'q';
}

string Solve(string G) {
  string res = "";
  for (int i = 0; i < G.size(); i++) {
    if (G[i] != ' ')
      res += maps[G[i]];
    else
      res += ' ';
  }
  return res;
}

int main() {
  //freopen("1.in", "r", stdin);
  //freopen("1.out", "w", stdout);

  freopen("A-small-attempt0.in", "r", stdin);
  freopen("A-small-attempt0.out", "w", stdout);
  //freopen("X-large.in", "r", stdin);
  //freopen("X-large.out", "w", stdout);

  Init();
  char line[200];
  cin >> t;
  cin.getline(line, 200);
  for (int cc = 1; cc <= t; cc++) {
    cin.getline(line, 200);
    cout << "Case #" << cc << ": " << Solve(line) << endl;
  }
  return 0;
}
