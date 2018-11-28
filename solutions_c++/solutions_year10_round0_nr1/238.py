
#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    int a, b;
    cin >> a >> b;
    printf("Case #%d: ", i+1);
    if ((b+1) % (1 << a) == 0) {
      printf("ON\n");
    } else {
      printf("OFF\n");
    }
  }
}
