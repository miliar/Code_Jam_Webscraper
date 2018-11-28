#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <functional>
#include <utility>
#include <cctype>
#include <vector>
#include <list>

using namespace std;

typedef unsigned long long ullong;
typedef long long llong;
typedef list<int> EdgeList;
typedef vector<EdgeList> AdjList;
typedef pair<int, int> ii;
typedef vector<ii> vii;

#define FOR_EDGE(adj,v,it) for (EdgeList::iterator it = adj[v].begin(); \
    it != adj[v].end(); ++it)

int main() {
  setvbuf(stdin, NULL, _IOFBF, 10000);
  setvbuf(stdout, NULL, _IOFBF, 10000);
 
  set<char> mapped;
  map<char, char> tran;
  tran['a'] = 'y';
  mapped.insert('y');
  tran['o'] = 'e';
  mapped.insert('e');
  tran['z'] = 'q';
  mapped.insert('q');
  string srcs[] = {string("ejp mysljylc kd kxveddknmc re jsicpdrysi"),
    string("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"),
    string("de kr kd eoya kw aej tysr re ujdr lkgc jv")};
  string dsts[] = {string("our language is impossible to understand"),
    string("there are twenty six factorial possibilities"),
    string("so it is okay if you want to just give up")};
  for (int i = 0; i < 3; ++i) {
    for (int j = 0; j < srcs[i].size(); ++j) {
      if (isalpha(srcs[i][j])) {
        tran[srcs[i][j]] = dsts[i][j];
        mapped.insert(dsts[i][j]);
      }
    }
  }
  bool done = false;
  for (int i = 0; i < 26 && !done; ++i) {
    char ch = 'a' + i;
    if (tran.count(ch) == 0) {
      for (int j = 0; j < 26 && !done; ++j) {
        if (mapped.count('a' +j) == 0) {
          tran[ch] = 'a' + j;
          done = true;
          break;
        }
      }
    }
  }

  int n_cases;
  scanf("%d", &n_cases);
  string ln;
  getline(cin, ln);
  for (int ctr =0; ctr < n_cases; ++ctr) {
    printf("Case #%d: ", ctr+1);
    getline(cin, ln);
    for (int i = 0; i < ln.size(); ++i) {
      if (isalpha(ln[i])) {
        putchar(tran[ln[i]]);
      } else {
        putchar(ln[i]);
      }
    }
    putchar('\n');
  }
  

  return 0;
}
