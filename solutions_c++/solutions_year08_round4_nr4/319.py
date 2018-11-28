#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#define INF 1000000000
using namespace std;

int comp(string cs) {
  int total = 0;
  for (int i = 0; i < cs.length(); i++) {
    if (i == 0 || cs[i] != cs[i-1]) 
      total++;
  }
  return total;
}

int find_min(int K, string S, int pos, string cs, vector<bool> used) {
  //  printf("find_min, string is %s\n", cs.c_str());
  if (pos == K) {
    return comp(cs);
  }
  int ntimes = S.length() / K;
  int tmin = INF;
  for (int i = 0; i < K; i++) {
    if (!used[i]) {
      used[i] = true;
      for (int j = 0; j < ntimes; j++) {
	cs[j*K + pos] = S[j*K + i];
      }
      tmin <?= find_min(K, S, pos+1, cs, used);
      used[i] = false;
    }
  }
  return tmin;
}

int main() {
  int N, K;
  string S;
  cin >> N;
  for (int cnum = 1; cnum <= N; cnum++) {
    cin >> K >> S;
    string ts;
    for (int i = 0; i < S.length(); i++)
      ts += " ";
    printf("Case #%d: %d\n", cnum, find_min(K, S, 0, ts, vector<bool>(K, false)));
  }
  return 0;
}
