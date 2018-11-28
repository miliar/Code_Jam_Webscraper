#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <numeric>
#include <sstream>

using namespace std;

int dr[]={0,1,0,-1,1,1,-1,-1};
int dc[]={1,0,-1,0,1,-1,1,-1};
template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

void solve_case();

int main() {
  int T; scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    solve_case();
  }
}

#define MAXN 1010

int N;
int A[MAXN];
int C[10010];

bool can(int L) {
  memset(C, 0, sizeof(C));
  for(int i = 0; i < N; i++) {
    C[A[i]]++;
  }
  int ON = 0;
  queue<int> q;
  for(int i = 0; i <= 10000; i++) {
    while(!q.empty() && q.front() == i) {
      q.pop();
      ON++;
    }
    while(C[i] > ON) {
      for(int k = 0; k < L; k++) {
        if(C[i + k]-- == 0) {
          return false;
        }
      }
      q.push(i + L);
    }
    ON = min(ON, C[i]);
  }
  return true;
}

void solve_case() {
  cin >> N;
  if(!N) {
    printf("0\n");
    return;
  }
  for(int i = 0; i < N; i++) cin >> A[i];
  sort(A, A + N);
  int lo = 1;
  int hi = N;
  while(lo < hi) {
    int md = (lo + hi + 1) / 2;
    if(can(md)) {
      lo = md;
    } else {
      hi = md - 1;
    }
  }
  printf("%d\n", lo);
}
