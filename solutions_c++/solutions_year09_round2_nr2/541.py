#include <cstdio>
#include <string.h>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAXL = 30;

void solve(char* num) {
  int len;
  int d[10] = {0};
  int after[MAXL+1][10];
  int min;
  int i, j;
  
  len = strlen(num);
  for (j = len-1; j >= 0; --j) {
    ++d[num[j] - '0'];
    for (i = 0; i < 10; ++i)
      after[j][i] = d[i];
  }

  for (j = len - 1; j >= 0; --j) {
    min = num[j] - '0';

    for (i = min + 1; i < 10; ++i)
      if (after[j][i] != 0)
	break;
    if (i != 10)
      break;
  }
  if (j >= 0) {
    num[j] = '0' + i;
    --after[j][i];

    for (min = 0; after[j][min] == 0; ++min);
    for (i = j + 1; i < len; ++i) {
      while (after[j][min] == 0) ++min;
      num[i] = '0' + min;
      --after[j][min];
    }

    printf("%s\n", num);
  }
  else 
    solve(num - 1);
}

int main () {
  int t;
  char num[MAXL + 2];
  
  scanf("%d\n", &t);
  for (int i = 1; i <= t; ++i) {
    scanf("%s\n", num+1);
    printf("Case #%d: ", i);
    num[0] = '0';
    solve(num+1);
  }
}
