#include <cstdio>
#include <set>

using namespace std;

int T;

int main() {
  scanf("%d", &T);

  for(int t = 1; t <= T; t++) {
    int a, b;
    scanf("%d %d", &a, &b);

    int d = 0;
    int l = 1;
    int aa = a;
    while(aa > 0) {
      aa /= 10;
      d++;
      l *= 10;
    }

    int r = 0;

    for(int i = a; i < b; i++) {
      int f = 1;
      int g = l;

      for(int j = 1; j <= d; j++) {
	f *= 10;
	g /= 10;

	set<int> o;

	int n = (i*f) % l;

	if(n < l/10)
	  continue;

	n += (i/g);

	if(n > i && n <= b) {
	  o.insert(n);
	  fprintf(stderr, "couple %d: %d, %d\n", j, i, n);
	}

	r += o.size();
      }
    }

    printf("Case #%d: %d\n", t, r);
  }
}

