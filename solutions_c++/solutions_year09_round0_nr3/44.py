#include <cstdio>
#include <cstring>

char *target = "welcome to code jam";
int target_length;
char buffer[600];
int length;
int mem[505][20];

int calc_ways(int buf_index, int target_index) {
  if (target_index == target_length) return 1;
  if (buf_index >= length) return 0;
  if (mem[buf_index][target_index] != -1) return mem[buf_index][target_index];
  int ans = 0;
  if (buffer[buf_index] == target[target_index]) {
    ans = calc_ways(buf_index + 1, target_index + 1) % 10000;
  }
  ans += calc_ways(buf_index + 1, target_index) % 10000;
  mem[buf_index][target_index] = ans % 10000;
  return ans % 10000;
}

int main(void) {
  int nC, cC;
  // Longest line is at most 500 chars...

  target_length = strlen(target);
  gets(buffer);
  sscanf(buffer, "%d", &nC);
  for (cC = 0; cC < nC; cC++) {
    gets(buffer);
    length = strlen(buffer);
    memset(mem, -1, sizeof(mem));
    printf("Case #%d: %04d\n", cC + 1, calc_ways(0, 0));
  }
}
