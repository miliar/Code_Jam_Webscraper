#include <cstdio>
#include <cassert>

#include <algorithm>

using namespace std;

#define MAXN 1004

struct Circle {
   int id;
   int radius;
   double x, y;
   bool operator<(const Circle& c) const {
      return id < c.id;
   }
};

struct CmpRadius {
   bool operator()(const Circle& c1, const Circle& c2) const {
      if (c1.radius != c2.radius) return c1.radius > c2.radius;
      return c1.id < c2.id;
   }
};

int N;
int W, L;
Circle C[MAXN];

int main(int argc, char* argv[]) {
   int TC;
   scanf("%d", &TC);
   for (int tc = 1; tc <= TC; ++tc) {
      scanf("%d %d %d", &N, &W, &L);
      for (int i = 0; i < N; ++i) {
         C[i].id = i;
         scanf("%d", &C[i].radius);
      }

      sort(C, C+N, CmpRadius());
      int sign = 1;
      double curx = 0.0;
      double cury = 0.0;
      C[0].x = curx;
      C[0].y = cury;
      double yrad = C[0].radius;
      curx += C[0].radius;
      for (int i = 1; i < N; ++i) {
         if (curx + sign * C[i].radius > W ||
             curx + sign * C[i].radius < 0) {
            if (sign > 0)
               curx = W;
            else
               curx = 0;
            sign = -sign;
            cury += C[i].radius + yrad;
            yrad = C[i].radius;
         }
         else
            curx += sign * C[i].radius;
         C[i].x = curx;
         C[i].y = cury;
         curx += sign * C[i].radius;
//       fprintf(stderr, " %.2lf %.2lf\n", C[i].x, C[i].y);
      }

      sort(C, C+N);
      printf("Case #%d:", tc);
      for (int i = 0; i < N; ++i) {
         printf(" %.3lf %.3lf", C[i].x, C[i].y);

         assert(C[i].x >= 0 && C[i].x <= W);
         assert(C[i].y >= 0 && C[i].y <= L);

      }
      printf("\n");
   }
   return 0;
}
