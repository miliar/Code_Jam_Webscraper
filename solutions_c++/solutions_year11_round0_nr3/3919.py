//Fruit of Light
//FoL CC
//Mandarine
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
  vector <int> v;
  int t;
  scanf ("%d", &t);
  for (int I = 0; I<t; I++) {
    printf ("Case #%d: ", I+1);
    int n, m = 1000032, sum = 0, x;
    scanf ("%d", &n);
    v.resize(n);
    for (int i = 0; i < n; i++) {
      int temp;
      scanf ("%d", &temp);
      if (!i) x = temp;
      else x ^= temp;
      m = min (m, temp);
      sum += temp;
    }
    if (!x) printf ("%d\n", sum-m);
    else printf ("NO\n");
  }
  return 0;
}