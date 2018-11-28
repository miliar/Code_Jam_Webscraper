#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int M;
int G[10000], C[10000];
int I[10000];
int store[10000][2];
char done[10000][2];

const int INF = 10000;

int compute(int i, int V)
{
  if (done[i][V]) return store[i][V];
  if (i >= (M-1)/2)
    return I[i] == V ? 0 : INF;
  // AND
  int ans = INF;
  if (G[i] == 1 || C[i] == 1) {
    for (char v1 = 0; v1 <= 1; v1++)
      for (char v2 = 0; v2 <= 1; v2++)
	if ((v1 && v2) == V)
	  ans <?= compute(2*i+1, v1) + compute(2*i+2, v2) + (G[i] == 1 ? 0 : 1);
  }
  // OR
  if (G[i] == 0 || C[i] == 1) {
    for (char v1 = 0; v1 <= 1; v1++)
      for (char v2 = 0; v2 <= 1; v2++)
	if ((v1 || v2) == V)
	  ans <?= compute(2*i+1, v1) + compute(2*i+2, v2) + (G[i] == 0 ? 0 : 1);
  }
  done[i][V] = true;
  return store[i][V] = ans;
}

int main(void)
{
  int N;
  cin >> N;
  string line;
  for (int c = 1; c <= N; c++) {
    memset(done, 0, sizeof(done));
    int V;
    cin >> M >> V;
    for (int i = 0; i < (M-1)/2; i++)
      cin >> G[i] >> C[i];
    for (int i = 0; i < (M+1)/2; i++)
      cin >> I[i+(M-1)/2];
    int ans = compute(0, V);
    if (ans < INF)
      printf("Case #%d: %d\n", c, ans);
    else
      printf("Case #%d: IMPOSSIBLE\n", c);
  }
}
