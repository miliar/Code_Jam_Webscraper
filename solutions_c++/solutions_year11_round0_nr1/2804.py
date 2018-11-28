#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"

using namespace std;

int main() {
  int T; scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    fprintf(stderr, "Case #%d of %d...\n", Ti, T);
    int N; scanf("%d", &N);
    int time = 0;
    int Op = 1, Bp = 1, Ota = 0, Bta = 0;
    for (int i = 1; i <= N; ++i) {
        char r; int p; scanf(" %c %d", &r, &p);
        int tu, tn;
        if (r == 'O') {
            tn = abs(p-Op)+1;
            tu = max(tn-Ota,1);
            Bta += tu;
            Ota = 0;
            Op = p;
            fprintf(stderr, "%c: tn = %d, tu = %d, Ota = %d, Bta = %d\n", r, tn, tu, Ota, Bta);
        } else {
            tn = abs(p-Bp)+1;
            tu = max(tn-Bta,1);
            Ota += tu;
            Bta = 0;
            Bp = p;
            fprintf(stderr, "%c: tn = %d, tu = %d, Ota = %d, Bta = %d\n", r, tn, tu, Ota, Bta);
        }
        time += tu;
        fprintf(stderr, "time = %d\n", time);
    }

    printf("Case #%d: %d\n", Ti, time);
  }
  return 0;
}
