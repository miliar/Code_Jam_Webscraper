#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <math.h>
#include <string>
using namespace std;

#define all(V) (V).begin(),(V).end()
#define rall(V) (V).rbegin(),(V).rend()
#define _foreach(it, a, b) for (typeof(a) it = a; it != b; ++it)
#define foreach(x...) _foreach(x)
#define fu(a, b) foreach(a, 0, b)
#define MSET(a, b) memset(a, b, sizeof(a))

char buf[500];
vector<int> temp;
int conta(char *b) {
  int i;
  int ult = 0;
  for (i = 0; b[i]; i++)
    if (b[i] == '1') ult = i;
  return ult;
}
int main() {
  int _42;
  scanf("%d", &_42);
  fu(_41, _42) {
    printf("Case #%d: ", _41+1);
    int N;
    scanf("%d", &N);
    temp.clear();
    fu(i, N) {
      scanf(" %s", buf);
      temp.push_back(conta(buf));
    }
    int r = 0;
    for (int i = 0; i < N; i++) {
      int j;
      for (j = i; j < N; j++) {
        if (temp[j] <= i)
          break;
      }
      r += (j-i);
      for (j--; j >= i; j--)
        swap(temp[j], temp[j+1]);
    }
    printf("%d\n", r);
  }
  return 0;
}
