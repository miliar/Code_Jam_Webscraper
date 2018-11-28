
#include <string.h>
#include <stdio.h>
#include <algorithm>

struct SGroup{
  int cap;
  int next;
};

static void buildIndex(SGroup* groups, int n, int cap)
{
  SGroup shiftedGroups[2002];
  memcpy(shiftedGroups, groups, n * sizeof(SGroup));
  memcpy(shiftedGroups + n, groups, n * sizeof(SGroup));
  for (int i = 0; i < n; i++) {
    int tmp_cap = cap, j = i;
    int count   = 0;
    while (j < 2 * n && count < n) {
      tmp_cap -= shiftedGroups[j].cap;
      if (tmp_cap < 0) break;
      j++;
      count++;
    }
    /* next entering group */
    groups[i].next = j % n;
  }
}

static long long calcEarn(SGroup* groups, int n, int start, int run)
{
  long long earned = 0;
  int cur_start    = start;
  
  for (int i = 0 ; i < run; i++) {
    int j = cur_start;
    do {
      earned += groups[j].cap;
      j = (j + 1) % n;
    } while (j != groups[cur_start].next);
    cur_start = groups[cur_start].next;
  }
  return earned;
}

static void calcPeriodGroups(SGroup* groups, int n, int&start, int&period, long long& earnp)
{
  int mask[1001];
  memset(mask, 0, sizeof(mask));
  
  int cur_group = 0;
  while (mask[cur_group] != 1) {
    mask[cur_group] = 1;
    cur_group       = groups[cur_group].next;
  }
  start = cur_group;
  
  memset(mask, 0, sizeof(mask));
  cur_group = start;
  period     = 0;
  earnp      = 0;
  while (mask[cur_group] != 1) {
    mask[cur_group]  = 1;
    earnp           += calcEarn(groups, n, cur_group, 1);
    cur_group        = groups[cur_group].next;
    ++period;
  }
}


static long long solve(SGroup* groups, int n, int cap, int run)
{
  int period, start;
  long long earnp;
  calcPeriodGroups(groups, n, start, period, earnp);

  long long earned = 0;
  int next_group   = 0;
  while (next_group != start) {
    earned += calcEarn(groups, n, next_group, 1);
    next_group = groups[next_group].next;
    --run;
  }
  int total_p = run / period;
  earned += (long long)total_p * earnp;
  run = run % period;
  earned += calcEarn(groups, n, start, run);
  return earned;
}

int main()
{
  int t;
  SGroup groups[1001];

  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    int run, cap, n;
    scanf("%d%d%d", &run, &cap, &n);
    for (int k = 0; k < n; k++)
      scanf("%d", &groups[k].cap);
    buildIndex(groups, n, cap);
    printf("Case #%d: %lld\n", i, solve(groups, n, cap, run));
  } 



}