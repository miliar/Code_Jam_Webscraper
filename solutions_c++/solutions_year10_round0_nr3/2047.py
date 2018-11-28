#include <cstdio>
#include <iostream>

using namespace std;

typedef long long i64;

const int MaxG = 10240;

int R, K, G;
int g[MaxG], cnt[MaxG];

i64 solve()
{
  scanf("%d %d %d", &R, &K, &G);
  i64 total = 0;
  for (int i = 0; i < G; i++) {
    scanf("%d", &g[i]);
    g[i+G] = g[i];
    total += g[i];
    if (g[i] > K) fprintf(stderr, "g[%d]>%d !!!\n", g[i], K);
  }

  if (total <= K)
    return total*R;

  i64 res = 0;
  int offset = 0;
  for (int i = 0; i < G; i++) {
    int left = K;
    while (left >= g[offset])
      left -= g[offset++];
    offset %= G;
    res += (K-left);
    R--;
    if (R == 0)
      return res;
  }
  int offset0 = offset;

  int L = 0;
  do {
    int left = K;
    while (left >= g[offset])
      left -= g[offset++];
    cnt[L++] = K-left;
    //    printf("%d ", cnt[L-1]);
    offset %= G;
  } while (offset != offset0);
  //  puts("");

  for (int i = 0; i < L; i++)
    res += i64((R+L-1-i)/L)*cnt[i];

  return res;
}

int main()
{
  int N;
  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    cout << "Case #" << (i+1) << ": " << solve() << endl;
  }
  return 0;
}
