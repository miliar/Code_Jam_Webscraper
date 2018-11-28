// CPPFLAGS=-std=gnu++0x -W -Wall -g -O2
#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define foreach(i,c) for(auto i=(c).begin();i!=(c).end();++i)
template<class T> bool in(T e, const set<T>& s) { return s.find(e) != s.end(); }

int m, n;
vector<vector<char> > B;

bool ok(int i, int j, char c) {
  if (i >= m || j >= n) return false;
  if (B[i][j] != '#') return false;
  B[i][j] = c;
  return true;
}

int main() {
  int tests; scanf("%d",&tests);
  for (int t=1;t<=tests;++t) {
    printf("Case #%d:\n",t);
    scanf("%d %d",&m,&n);
    B = vector<vector<char> >(m, vector<char>(n));
    int i, j;
    for (i=0;i<m;++i) for (j=0;j<n;++j) scanf(" %c",&B[i][j]);
    for (i=0;i<m;++i) for (j=0;j<n;++j) if (B[i][j]=='#') {
      if (!(ok(i,j,'/')&&ok(i,j+1,'\\')&&ok(i+1,j,'\\')&&ok(i+1,j+1,'/'))) {
        printf("Impossible\n");
        goto next_test;
      }
    }
    for (i=0;i<m;++i) {
      for (j=0;j<n;++j) printf("%c",B[i][j]); printf("\n");
    }
next_test:;
  }
}
