#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
#define E 1e-5
#define MAXSIZE 36

const double PI = 2 * acos(0);
#define steplen (PI/180)

typedef struct cir {
    double r, x, y;
    int put;
} circle;

circle sp[MAXSIZE];
double W, H, miny, minx, totalarea;

//represent the distance of the vertex

double getdis(int i, int j) {
    return sqrt((sp[i].x - sp[j].x)*(sp[i].x - sp[j].x)+(sp[i].y - sp[j].y)*(sp[i].y - sp[j].y));
}

double right_angle(double x, double y) {
    return sqrt(x * x - y * y);
}

int can_put(int current, double x, double y) {
    if (x < sp[current].r || x > W - sp[current].r || y < sp[current].r || y > H - sp[current].r)
        return 0;
    sp[current].x = x;
    sp[current].y = y;
    for (int i = 0; i < current; i++) {
        if (sp[i].put > 0 && getdis(i, current) < sp[current].r + sp[i].r - E) //check whether it overlap with other circle
            return 0;
    }
    return 1;
}

int put_circle(int current, double x, double y) {
    int color;
    sp[current].x = x;
    sp[current].y = y;
    sp[current].put = 1;
    totalarea += PI * sp[current].r * sp[current].r;
    printf(" %.1lf %.1lf", x, y);
    color = rand() % 16;
    if (color == 0) color++;
    return 1;
}

int check_ok(double x, double y) {
    if (miny > y) {
        miny = y;
        minx = x;
    } else if (miny == y) {
        if (minx >= x)
            minx = x;
    }
    return 1;
}

int pad(int current) {
    double x, y;
    int i;
    double j;

    if (can_put(current, sp[current].r, sp[current].r))
        return put_circle(current, sp[current].r, sp[current].r);
    if (current == 0) return 0;
    for (i = 0; i < current; i++) {
        if (sp[i].put) {

            for (j = 0.0; j < 2 * PI; j += steplen) {
                x = sp[i].x + (sp[i].r + sp[current].r) * cos(j);
                y = sp[i].y + (sp[i].r + sp[current].r) * sin(j);
                if (can_put(current, x, y))
                    check_ok(x, y);
            }
        }

    }
    if (miny < H)
        put_circle(current, minx, miny);
    return 1;
}

bool compare(circle a, circle b) {
    return a.r > b.r;
}

int main() {
    int T;
    scanf("%d", &T);
    int i, n;
    for (int t = 1; t <= T; t++) {
        scanf("%d%lf%lf", &n, &W, &H);
        printf("Case #%d:", t);
        for (i = 0; i < n; i++)
            scanf("%lf", &sp[i].r);
        sort(sp, sp + n, compare);
        totalarea = 0;
        for (i = 0; i < n; i++) {
            sp[i].put = 0;
            miny = H + 1;
            minx = W + 1;
            pad(i);
        }
        printf("\n");
    }
    return 0;
}