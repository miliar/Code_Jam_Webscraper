#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <list>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
  int ncases;
  scanf("%d\n", &ncases);
  for (int j = 0; j < ncases; ++j) {
    int n;
    scanf("%d", &n);
    int smallest = 9999999;
    int sum = 0;
    int previous = 0;
    for (int i = 0; i < n; ++i) {
      int atual;
      scanf("%d", &atual);
      if (atual < smallest) smallest = atual;
      sum += atual;
      previous = atual ^ previous;
    }
    printf("Case #%d: ", j + 1);
    if (previous == 0) {
      printf("%d\n", sum - smallest);
    }
    else printf("NO\n");
  }
}
