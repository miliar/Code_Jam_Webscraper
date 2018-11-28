#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

int C, M, N;
vector<vector<bool> > avail;
vector<vector<int> > best;

bool allowed(int r, int mask) {
  for (int i = 0; i < N-1; i++) {
    if ((mask & (1<<i)) && (mask & (1<<(i+1)))) {
      return false;
    }
  }
  for (int i = 0; i < N; i++) {
    if ((mask & (1<<i)) && !avail[r][i])
      return false;
  }
  return true;
}

bool allowed2(int mask1, int mask2) {
  for (int i = 0; i < N-1; i++) {
    if ((mask1 & (1<<i)) && (mask2 & (1<<(i+1))))
      return false;
    if ((mask2 & (1<<i)) && (mask1 & (1<<(i+1))))
      return false;
  }
  return true;
}

int count(int mask) {
  int ret = 0;
  for (int i = 0; i < N; i++) {
    if (mask & (1<<i)) {
      ret++;
    }
  }
  return ret;
}

int main() {
  scanf("%d", &C);
  for (int cnum = 1; cnum <= C; cnum++) {
    scanf("%d%d", &M, &N);
    avail = vector<vector<bool> >(M, vector<bool>(N));
    for (int i = 0; i < M; i++) {
      string s;
      cin >> s;
      for (int j = 0; j < N; j++) {
	avail[M-i-1][j] = (s[j] == '.' ? true : false);
      }
    }
    
    best = vector<vector<int> >(M, vector<int>(1<<N, 0));
    for (int i = 0; i < (1<<N); i++) {
      if (allowed(0, i)) {
	best[0][i] = count(i);
      }
    }
    for (int i = 1; i < M; i++) {
      for (int j = 0; j < (1<<N); j++) {
	for (int k = 0; k < (1<<N); k++) {
	  if (allowed2(j, k) && allowed(i, k)) {
	    best[i][k] >?= best[i-1][j] + count(k);
	  }
	}
      }
    }
    
    int ans = 0;
    for (int i = 0; i < M; i++) {
      for (int j = 0; j < (1<<N); j++) {
	ans >?= best[i][j];
      }
    }
    printf("Case #%d: %d\n", cnum, ans);
  }
  return 0;
}
