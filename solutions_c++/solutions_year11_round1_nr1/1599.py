#include <iostream>
#include <cmath>

using namespace std;

int T, N, Pd, Pg;

int solve() {
  if (Pg == 100)
    return (Pd == 100);
  //for (int X = 0; X <= (Pg*N)/(100-Pg); X++) {
  for (int X = 0; X <= 100*N; X++) {
    for (int x = 0; x <= X; x++) {
      for (int D = 1; D <= N; D++) {
	if (100*x-Pg*X == Pg*D - Pd*D) {

	  // sanity check
	  int d = Pd*D/100;
	  int G = X + D;
	  int g = x + d;
	  if (100*g/G != Pg) break;
	  if (100*d/D != Pd) break;
	  if (d > D) break;
	  if (g > G) break;
	  if (d < 0) break;
	  if (g < 0) break;
	  if ((d + x)*100/G != Pg)
	    printf("Error.\n");
	  return 1;
	}
      }
    }
  }
  return 0;
}

int main() {
  cin >> T;
  for (int i = 0; i < T; i++) {
    cin >> N >> Pd >> Pg;
    if (solve())
      printf("Case #%d: Possible\n", i+1);
    else
      printf("Case #%d: Broken\n", i + 1);
  }
}
