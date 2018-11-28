#include <stdio.h>
#include <stdlib.h>

#define N 50
#define M 50

#define swap(a, b) do { int t=a; a=b; b=t; } while(0)

int area2(int x1,int y1, int x2, int y2)
{
    if ((x1 >= x2 && y1 <= y2 ) ||
            (x1 <= x2 && y1 >= y2)) {
        return x1*y2*2 - x2*y2 - y1*x1 - (x1-x2)*(y2-y1);
    } else if (x1 >= x2 && y1 >= y2) {
        if (x2*y1 >= x1*y2) {
            return x1*y1 - x2*(y1-y2)*2 - x2*y2 - (x1-x2)*(y1-y2);
        } else {
            return x1*y1 - y2*(x1-x2)*2 - x2*y2 - (x1-x2)*(y1-y2);
        }
    } else {
        swap(x1, x2);
        swap(y1, y2);
        if (x2*y1 >= x1*y2) {
            return x1*y1 - x2*(y1-y2)*2 - x2*y2 - (x1-x2)*(y1-y2);
        } else {
            return x1*y1 - y2*(x1-x2)*2 - x2*y2 - (x1-x2)*(y1-y2);
        }
    }
}

int main(void)
{
    int ncase;
    scanf("%d", &ncase);

    for (int casen=0; casen < ncase; casen++) {
        int x0, y0, x1, y1, x2, y2;
        x0 = y0 = 0;

        int n, m;
        int A;
        scanf("%d %d %d", &n, &m, &A);




        for (x1 = 0; x1<=n; x1++)
            for(y1=0; y1<=m; y1++) {
                for(x2=0; x2<=n; x2++)
                    for(y2=0; y2<=m; y2++) {
                        if (area2(x1, y1, x2, y2) == A) {
                            goto found;
                        }
                    }
            }

found:
	    printf("Case #%d: ", casen+1);

        if (x1 == n+1) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d %d %d %d %d %d\n", 0, 0, x1, y1, x2, y2);
        }

    }
    return 0;
}
