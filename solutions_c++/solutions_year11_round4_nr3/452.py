// CPPFLAGS=-std=gnu++0x -W -Wall -g -O2
#include <algorithm>
#include <cassert>
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

int composite[1001];

int main() {
  int i, j;
  composite[1]=1;
  for (i=2;i<=1000;++i) if (!composite[i]) {
    for (j=i+i;j<=1000;j+=i) composite[j]=1;
  }

  int tests; if (scanf("%d",&tests)!=1) return 1;
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    int N; if(scanf("%d",&N)!=1) return 2;
    int m = (N==1), M = 1;
    for (i = 2; i <= N; ++i) if (!composite[i]) {
      ++m;
      for (int n=N;n>=i;n/=i) ++M;
    }
    printf("%d\n",M-m);
  }
}
