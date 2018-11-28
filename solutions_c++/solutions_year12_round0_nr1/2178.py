#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <set>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <fstream>
#include <numeric>
#include <limits.h>
#include <iomanip>
#include <assert.h>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef long long ll;

#define ITE(v) typeof(v.begin())
#define FOR(i,n) for(int i = 0; i < n; i++)
#define FORIT(it,v) for(ITE(v) it = v.begin(); it != v.end(); it++)
#define ALL(v) v.begin(), v.end()
#define SZ(v) int(v.size())
#define pb push_back
#define SQR(a) ((a)*(a))

#define INF 0x3f3f3f3f
#define EPS (1e-9)

inline int cmp(double a, double b = 0.0) {
  if (fabs(a-b) <= EPS) return 0;
  if (a < b) return -1;
  return 1;
}

string enc[] = {
  "ejp mysljylc kd kxveddknmc re jsicpdrysi",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
  "de kr kd eoya kw aej tysr re ujdr lkgc jv",
  "z"};

string decr[] = {
  "our language is impossible to understand",
  "there are twenty six factorial possibilities",
  "so it is okay if you want to just give up",
  "q"};

char tra[256];
bool vis[256];
bool rvis[256];

int main() {
  FOR(i,256) tra[i] = i;
  FOR(i,4) FOR(j,SZ(enc[i])) {
    tra[enc[i][j]] = decr[i][j];
    vis[enc[i][j]] = true;
    rvis[decr[i][j]] = true;
  }
  int cnt = 0;
  for (char c = 'a'; c <= 'z'; c++) {
    if (rvis[c] == false) {
      tra['q'] = c;
      vis['q'] = true;
      cnt++;
    }
  }
  //cout << cnt << endl;
  for (char c = 'a'; c <= 'z'; c++) {
    //cout << c << endl;
    assert(vis[c] == true);
  }
  int ncases;
  cin >> ncases;
  getchar();
  FOR(kk, ncases) {
    printf("Case #%d: ", kk+1);
    string s;
    getline(cin, s);
    FOR(i, SZ(s)) s[i] = tra[s[i]];
    cout << s << endl; 
  }
  return 0;
}
