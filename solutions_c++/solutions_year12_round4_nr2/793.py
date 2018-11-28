#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <stdlib.h>
#include <stdio.h>

#define MAXS 1000

static int nstudents;
static long matx, maty;
static long r[MAXS+1];
static long sx[MAXS+1];
static long sy[MAXS+1];

int main(void)
{
    int ncases;

    std::cin >> ncases;
    std::cin.ignore();
    for (int casenr = 1; casenr <= ncases; casenr++) {
      std::cin >> nstudents >> matx >> maty;
      std::cin.ignore();
      matx *= 1000;
      maty *= 1000;
      for (int i = 0; i < nstudents; i++) {
          std::cin >> r[i];
          r[i] *= 1000;
      }
      std::cin.ignore();

    retry:
      fprintf(stderr, "Trying...\n");
      for (int i = 0; i < nstudents; i++) {
          int t;
          for (t = 0; t < 100; t++) {
                long x = lrand48() % (matx+1);
                long y = lrand48() % (maty+1);
                int j;
                for (j = 0; j < i; j++) {
                    long dx = abs(sx[j] - x);
                    long dy = abs(sy[j] - y);
                    long mr = r[i] + r[j];
                    if (dx*dx + dy*dy < mr * mr) {
                        break;
                    }
                }
                if (j == i) {
                    sx[i] = x;
                    sy[i] = y;
                    break;
                }
          }
          if (t == 100)
              goto retry;
      }

      fprintf(stderr, "Case #%d: ", casenr);
      fprintf(stdout, "Case #%d: ", casenr);
      for (int i = 0; i < nstudents; i++) {
          fprintf(stderr, " %ld.%03ld %ld.%03ld", sx[i] / 1000, sx[i] % 1000, sy[i] / 1000, sy[i] % 1000);
          fprintf(stdout, " %ld.%03ld %ld.%03ld", sx[i] / 1000, sx[i] % 1000, sy[i] / 1000, sy[i] % 1000);
      }
      fprintf(stderr, "\n");
      fprintf(stdout, "\n");
    }
}
