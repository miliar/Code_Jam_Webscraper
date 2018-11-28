#include <stdio.h>
#include <stdint.h>

int nRuns;
int64_t cap;
int nGroups;
int groups[2000];

int nextGroupAtHead[1000];
int64_t groupTotal[1000];

int main(void) {
  int nC, cC;

  scanf("%d", &nC);
  for (cC = 0; cC < nC; ++cC) {
    int64_t total = 0;
    scanf("%d%lld%d", &nRuns, &cap, &nGroups);
    for (int i = 0; i < nGroups; ++i) {
      scanf("%d", &groups[i]);
      groups[i + nGroups] = groups[i];
      total += groups[i];
    }

    if (total <= cap) {
      printf("Case #%d: %lld\n", cC + 1, (int64_t)nRuns * total);
      continue;
    }

    int end = 0;
    total = groups[0];
    for (int start = 0; start < nGroups; ++start) {
      while (total + groups[end + 1] <= cap) {
        total += groups[end + 1];
        ++end;
      }
      groupTotal[start] = total;
      nextGroupAtHead[start] = (end + 1) % nGroups;
      total -= groups[start];
    }

    int64_t money = 0;
    int group = 0;
    for (int i = 0; i < nRuns; ++i) {
      money += groupTotal[group];
      group = nextGroupAtHead[group];
    }
    printf("Case #%d: %lld\n", cC + 1, money);
  }
  return 0;
}
