/* Rajat Goel (C++) */
#include <algorithm>
#include <iostream>
#include <iterator>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef pair<int,int>  pii;
typedef long long      LL;
typedef long double    LD;
const int  INF  =      INT_MAX / 2 - 1;
const LL   LINF =      LLONG_MAX / 2 - 1;
const LD   EPS  =      1e-7;
#define loop(i, n)     for (int i = 0; i < int(n); ++i)
#define foreach(i, a)  for (typeof((a).begin()) i = (a).begin();i != (a).end(); ++i)
template<typename T>
inline int fCMP(T x, T y = 0, T tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int main(int argc, char *argv[]) {
	int T; scanf(" %d", &T);
	for (int X = 1; X <= T; ++X) {
    int C; scanf(" %d", &C);
    map<pair<char, char>, char> Cmap; 
    loop (i, C) {
      char str[4];
      scanf(" %s", str);
      Cmap[make_pair(str[0], str[1])] = str[2];
      Cmap[make_pair(str[1], str[0])] = str[2];
    }

    int D; scanf(" %d", &D);
    list<pair<char, char> > Dlist;
    loop (i, D) {
      char str[3];
      scanf(" %s", str);
      Dlist.push_back(make_pair(str[0], str[1]));
    }

    int len; scanf(" %d", &len);
    char str[len + 1];
    scanf(" %s", str);

    char stck[1000]; int pos = 0;
    for (const char* ptr = str; *ptr; ++ptr) {
      stck[pos++] = *ptr;
      
      while (pos >= 2) {
        pair<char, char> id(stck[pos - 2], stck[pos - 1]);
        map<pair<char, char>, char>::const_iterator it = Cmap.find(id);

        if (it != Cmap.end()) {
          --pos;
          --pos;
          stck[pos++] = it->second;
        } else {
          break;
        }
      }

      vector<bool> occurs(256, false);
      loop (i, pos) {
        occurs[stck[i]] = true;
      }

      bool erase = false;
      foreach (it, Dlist) {
        if (occurs[it->first] && occurs[it->second]) {
          erase = true;
          break;
        }
      }

      if (erase) {
        pos = 0;
      }
    }

    string out = "[";
    loop (i, pos) {
      out += string(1, stck[i]);
      if (i != pos - 1) {
        out += ", ";
      }
    }
    out += "]";

		printf("Case #%d: %s\n", X, out.c_str());
	}
	return 0;
}
