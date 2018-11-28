#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>

using namespace std;

void count(const char* str, int sum[4]) {
  sum[0] = 0; sum[1] = 0; sum[2] = 0; sum[3] = 0;
  // printf("[%c%c%c%c]\n", str[0], str[1], str[2], str[3]);
  for (int i=0; i<4; i++) {
    switch (str[i]) {
    case 'X': sum[0]++; break;
    case 'O': sum[1]++; break;
    case 'T': sum[2]++; break;
    case '.': sum[3]++; break;
    }
  }
}

void p(int sum[4]) {
  printf("%d %d %d %d\n", sum[0], sum[1], sum[2], sum[3]);
}

bool check(int tc, int sum[4]) {
  if (sum[0] + sum[2] == 4) {
    printf("Case #%d: X won\n", tc);
    return true;
  }
  if (sum[1] + sum[2] == 4) {
    printf("Case #%d: O won\n", tc);
    return true;
  }
  return false;
}

void go(int tc) {
  string line;
  char map[4][4];
  for (int i=0; i<4; i++) {
    cin >> line;
    const char* str = line.c_str();
    for (int j=0; j<4; j++) {
      map[i][j] = str[j];
    }
  }
  // cin >> line;

  int sum[4]= {0, 0, 0, 0};
  bool incomplete = false;

  // rows
  for (int i=0; i<4; i++) {
    count(map[i], sum);
    // p(sum);
    if (check(tc, sum)) return;
    incomplete = incomplete | sum[3] > 0;
  }

  // cols
  for (int i=0; i<4; i++) {
    char nums[4] = { map[0][i], map[1][i], map[2][i], map[3][i] };
    count(nums, sum);
    // p(sum);
    if (check(tc, sum)) return;
    incomplete = incomplete | sum[3] > 0;
  }

  // diag
  {
    char nums[4] = { map[0][0], map[1][1], map[2][2], map[3][3] };
    count(nums, sum);
    // p(sum);
    if (check(tc, sum)) return;
    incomplete = incomplete | sum[3] > 0;
  }
  {
    char nums[4] = { map[3][0], map[2][1], map[1][2], map[0][3] };
    count(nums, sum);
    // p(sum);
    if (check(tc, sum)) return;
    incomplete = incomplete | sum[3] > 0;
  }

  if (incomplete) {
    printf("Case #%d: Game has not completed\n", tc);
  }
  else {
    printf("Case #%d: Draw\n", tc);
  }
}

int main() {
  string line;
  cin >> line;
  int tc = atoi(line.c_str());
  for (int i=0; i<tc; i++) {
    go(i+1);
  }
}

