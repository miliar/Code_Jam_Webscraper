#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <map>
using namespace std;

const int MaxN = 36;

int n, m;
vector<int> sused[MaxN];

int L[MaxN];

map<long long, int> dp[MaxN];
map<long long, bool> flag[MaxN];


int broj(long long s) {
  int cnt = 0;
  for (int i = 0; i < 36; i++)
    if (s & (1LL << i)) cnt++;
  return cnt;
}

int memoiz(int v, long long s) {
  if (v == 1) return broj(s) + 1;
  else if (flag[v][s]) return dp[v][s];
  else {
    int sol = -1;
    long long nbr = 0;
    for (int i = 0; i < sused[v].size(); i++) {
      int w = sused[v][i];
      if (L[w] == L[v] + 1){
	nbr |= (1LL << w);
      }
      else if (L[w] == L[v]) s |= (1LL << w);
    }

    int trB = broj(s);
    for (int i = 0; i < sused[v].size(); i++) {
      int w = sused[v][i];
      if (L[w] != L[v] + 1) continue;

      int tr = trB;
      if (w != 1) {
	// go to w
	for (int j = 0; j < sused[w].size(); j++) {
	  int vb = sused[w][j];
	  if (L[vb] != L[w] - 1) continue;

	  if (!(s & (1LL << vb)) && vb != v) tr++;
	}
      }

      int ttry = memoiz(w, nbr ^ (1LL << w));
      if (ttry != -1){
	ttry += tr;
	if (ttry > sol) sol = ttry;
      }
    }

    flag[v][s] = true;
    dp[v][s] = sol;

    return sol;
  }
}


int main() {
  int testC; scanf("%d", &testC);
  for (int ttt = 1; ttt <= testC; ttt++) {
    for (int i = 0; i < MaxN; i++) sused[i].clear();

    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; i++) {
      int a, b;
      scanf("%d,%d", &a, &b);
      sused[a].push_back(b);
      sused[b].push_back(a);
    }

    for (int i = 0; i < n; i++) L[i] = -1;
    queue<int> kju;
    kju.push(0);
    L[0] = 0;
    while (!kju.empty()) {
      int top = kju.front(); kju.pop();
      for (int i = 0; i < sused[top].size(); i++) {
	int w = sused[top][i];
	if (L[w] == -1){
	  L[w] = L[top] + 1;
	  kju.push(w);
	}
      }
    }

    for (int i = 0; i < MaxN; i++) {
      dp[i].clear();
      flag[i].clear();
    }

    int sol = memoiz(0, 0);
    printf("Case #%d: %d %d\n", ttt, L[1] - 1, sol);
  }

  return 0;
}

