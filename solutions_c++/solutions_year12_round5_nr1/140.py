#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

#define sz(c) ((int) (c).size())
#define pb push_back
#define mp make_pair
#define f first
#define s second

int n;
pair < pair <int,int>, int > a[1111];

void solve(int testcase) {
  printf("Case #%d:", testcase);
  eprintf("Case #%d:", testcase);
  scanf("%d", &n);
  for (int i=0; i<n; ++i)
    scanf("%d", &a[i].f.f);
  for (int i=0; i<n; ++i)
    scanf("%d", &a[i].f.s);
  for (int i=0; i<n; ++i) {
    a[i].s = i;
    a[i].f.s = -a[i].f.s;
  }
  sort(a, a + n);
  for (int i=0; i<n; ++i) 
    printf(" %d", a[i].s);
  printf("\n");
  for (int i=0; i<n; ++i) 
    eprintf(" %d", a[i].s);
  eprintf("\n");
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; ++i)
    solve(i);
  return 0;
}
