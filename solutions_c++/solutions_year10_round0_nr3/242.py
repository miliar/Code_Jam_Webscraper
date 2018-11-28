#include <stdio.h>
#include <vector>
#include <map>

void Solve(FILE *fin, FILE *fout) {
  int r, k, n;
  fscanf(fin, "%d %d %d", &r, &k, &n);
  std::vector<int> groups;
  for (int i = 0; i < n; ++i) {
    int x;
    fscanf(fin, "%d", &x);
    groups.push_back(x);
  }
  std::map<int, int> link;
  std::vector<int> count;
  // Try to find a cycle.
  int i;
  int cur = 0;
  for (i = 0; i < r; ++i) {
    if (link.find(cur) != link.end()) {
      // Cycle found!
      break; 
    }
    int c = 0;
    int pcur = cur;
    while (c <= k) {
      c += groups[cur++];
      if (cur == n) cur = 0;
      if (cur == pcur) break;
    }
    if (c > k) {
      cur = (cur ? cur -1: n-1);
      c -= groups[cur];
    }
    count.push_back(c);
    //printf("%d ", c);
    link[pcur] = count.size() - 1;
  }
  //printf("| ");
  uint64_t ans = 0;
  if (i == r) {
    // No cycle.
    for (int i = 0; i < count.size(); ++i) ans += count[i];
    //printf("no cycle\n");
  } else {
    int cycle_len = count.size() - link[cur];
    int cycles = (r-link[cur]) / cycle_len;
    int rest = r - link[cur] - cycle_len * cycles;   
    uint64_t pre_cost = 0;
    for (int i = 0; i < link[cur]; ++i) pre_cost += count[i];
    uint64_t cycle_cost = 0;
    for (int i = link[cur]; i < count.size(); ++i) cycle_cost += count[i];
    uint64_t post_cost = 0;
    int border = link[cur] + rest;
    for (int i = link[cur]; i < border; ++i) post_cost += count[i];
    //printf("cycle %llu %llu %llu %d\n", pre_cost, cycle_cost, post_cost, cycles);
    ans = pre_cost + cycles*cycle_cost + post_cost;
  }
  fprintf(fout, "%llu\n", ans); 
}

int main() {
  FILE *fin = fopen("input.txt", "r");
  FILE *fout = fopen("output.txt", "w");
  
  int test_cases_num;
  fscanf(fin, "%d", &test_cases_num);
  for (int i = 0; i < test_cases_num; ++i) {
    fprintf(fout, "Case #%d: ", i+1);
    Solve(fin, fout);
  }

  fclose(fout);
  return 0;
}
