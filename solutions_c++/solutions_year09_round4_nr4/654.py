#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

double calcForTwo(int x0, int y0, int r0, int x1, int y1, int r1) {
    return 0.5 * (sqrt((x0-x1)*(x0-x1) + (y0-y1)*(y0-y1)) + r0 + r1);
}


int x[40], y[40], r[40];

int main() {

    int T; scanf("%d", &T);
    for (int t=0; t<T; t++) {
        
        int N; scanf("%d", &N);
        for (int i=0; i<N; i++)
            scanf("%d%d%d", &x[i], &y[i], &r[i]);
            
        double result = 0;
        if (N==1) {
            result = r[0];
        }
        else if (N==2) {
            result = max(r[0], r[1]);
        }
        else if (N==3) {
            double r0 = max(calcForTwo(x[0], y[0], r[0], x[1], y[1], r[1]), double(r[2]));
            double r1 = max(calcForTwo(x[0], y[0], r[0], x[2], y[2], r[2]), double(r[1]));
            double r2 = max(calcForTwo(x[1], y[1], r[1], x[2], y[2], r[2]), double(r[0]));
            result = min(min(r0, r1), r2);
        }
        
        printf("Case #%d: %lf\n", t+1, result);
    }
    
    return 0;
}
