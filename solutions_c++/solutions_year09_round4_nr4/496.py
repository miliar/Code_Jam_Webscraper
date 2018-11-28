#include <iostream>
#include <cmath>
using namespace std;

#define MAX(a,b) ( (a)>(b) ? (a) : (b) )
#define MIN(a,b) ( (a)<(b) ? (a) : (b) )

struct circ {
   int x, y, r;
} c[4];

int main() {

int i, C, k, K;
double tmp1, tmp2, tmp3;

cin >> K;

for (k=1; k<=K; k++) {

cin >> C;
for (i=0; i<C; i++) {
   cin >> c[i].x;
   cin >> c[i].y;
   cin >> c[i].r;
}

if (C == 1) printf("Case #%d: %.6lf\n", k, (double)c[0].r);
else if (C == 2) printf("Case #%d: %.6lf\n", k, (double)MAX(c[0].r, c[1].r));
else {

tmp1 = MAX(sqrt(pow(c[0].x-c[1].x, 2.0) + pow(c[0].y-c[1].y, 2.0)) + c[0].r + c[1].r, c[2].r);
tmp2 = MAX(sqrt(pow(c[1].x-c[2].x, 2.0) + pow(c[1].y-c[2].y, 2.0)) + c[1].r + c[2].r, c[0].r);
tmp3 = MAX(sqrt(pow(c[0].x-c[2].x, 2.0) + pow(c[0].y-c[2].y, 2.0)) + c[0].r + c[2].r, c[1].r);

printf("Case #%d: %.6lf\n", k, MIN(MIN(tmp1, tmp2), tmp3)/2.0);

}

}

return 0;
}
