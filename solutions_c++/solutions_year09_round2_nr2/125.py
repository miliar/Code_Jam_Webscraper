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
using namespace std;

#define all(V) (V).begin(),(V).end()
#define rall(V) (V).rbegin(),(V).rend()
#define _foreach(it, a, b) for (typeof(a) it = a; it < b; ++it)
#define foreach(x...) _foreach(x)
#define fu(a, b) foreach(a, 0, b)
#define MSET(a, b) memset(a, b, sizeof(a))

char buf[50];
char buf2[50];
int main() {
  int _42;
  scanf("%d", &_42);
  for (int _41 = 0; _41 < _42; _41++) {
    printf("Case #%d: ", _41+1);
    scanf(" %s", buf);
    strcpy(buf2, buf);
    int n = strlen(buf);
    if (next_permutation(buf2, buf2+n))
      printf("%s\n", buf2);
    else {
      int menor;
      sort(buf, buf+n);
      for (menor = 0; buf[menor] == '0'; menor++);
      printf("%c0", buf[menor]);
      foreach(i, 0, menor)
        printf("%c", buf[i]);
      foreach(i, menor+1, n)
        printf("%c", buf[i]);
      printf("\n");
    }
  }
  return 0;
}
