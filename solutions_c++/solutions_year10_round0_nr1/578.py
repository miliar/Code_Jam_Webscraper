#include <cstdio>
#include <string>

using namespace std;

int main () {
  int tests;
  int n, k;
  scanf("%d", &tests);
  for (int test = 0; test < tests; ++test) {
    scanf("%d %d", &n, &k);
    int status = (k+1)%(1<<n);
    printf("Case #%d: ", test+1);
    if (status == 0)
	printf("ON\n");
    else
        printf("OFF\n");
  }
};
