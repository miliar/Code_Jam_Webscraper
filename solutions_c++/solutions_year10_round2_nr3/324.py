#include <stdio.h>

int main() {
  int max = 25;
  int table[max+1];
  int debug = 0;
  int show_table = 0;
  for (int n = 2; n <= max; ++n) {
    if (debug) printf("testing for integer %d\n", n);
    // use bits.  n==2 means 1 option (1 bit).  n==3 means 2 (2 bits).  n==4 means 4 (3 bits).
    int n_bits = n-1;
    int pure_combinations = 0;
    for (int i = 0; i<(1<<n_bits); ++i) {
      if (debug) printf("s = %d (in binary)\n", i);
      // 2, 3, 2 3, 4, 2 4, 2 3 4, ...
      // test whether n is pure with respect to the set given by the bits in i
      int current = n;
      while (1) {
	// is current in s?
	// first bit (1) means 2
	// second bit (2) means 3
	// -> 1 << (current-2)
	int bit_to_test = current - 2;
	if (!(i & (1 << bit_to_test))) {
	  if (debug) printf("%d not in s\n", current);
	  break;
	}
	if (debug) printf("%d in s.  counting bits now to find where it is\n", current);
	int pos = 0;
	for (int bit = 0; bit <= bit_to_test; ++bit) {
	  if (i & (1 << bit)) {
	    pos += 1;
	  }
	}
	if (debug) printf("-> pos %d\n", pos);
	if (pos == 1) {
	  if (debug) printf("reached 1 - this is counted\n");
	  pure_combinations = (pure_combinations + 1) % 100003;
	  break;
	}
	current = pos;
      }
    }
    if (debug || show_table) printf("-> %d combinations for %d\n", pure_combinations, n);
    table[n] = pure_combinations;
  }

  int T;
  scanf("%d", &T);
  if (debug) printf("%d cases\n", T);
  for (int t = 0; t < T; ++t) {
    int n;
    scanf("%d", &n);
    if (debug) printf("testing %d\n", n);
    printf("Case #%d: %d\n", t+1, table[n]);
  }
}
