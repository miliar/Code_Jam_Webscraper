#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int width;
int cuts;
int lower, upper;
int lpx[100], lpy[100];
int upx[100], upy[100];
double area;


double getTrap(int x1, int y1, int x2, int y2, double end) {
    double rate = double(y2 - y1) / (x2 - x1);
    return 0.5 * (y1 + y1 + (end-x1)*rate) * (end - x1);
}

double getArea(double end) {
    double ans = 0.0;
    int i;
    for (i = 1; upx[i] < end; i++)
        ans+=0.5 * (upy[i] + upy[i-1]) * (upx[i] - upx[i-1]);
    ans+=getTrap(upx[i-1], upy[i-1], upx[i], upy[i], end);
    for (i = 1; lpx[i] < end; i++)
        ans-=0.5 * (lpy[i] + lpy[i-1]) * (lpx[i] - lpx[i-1]);
    ans-=getTrap(lpx[i-1], lpy[i-1], lpx[i], lpy[i], end);
    return ans;
}


double binSearch(double goal, double start, double end) {
    double curr = (start + end) / 2;
    if (end - start < 1e-7)
        return curr;
    if (getArea(curr) < goal)
        return binSearch(goal, curr, end);
    return binSearch(goal, start, curr);
}

int main() {
    int T, TT;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        int i;
        area = 0.0;
        scanf("%d %d %d %d", &width, &lower, &upper, &cuts);
        for (i = 0; i < lower; i++) {
            scanf("%d %d", &lpx[i], &lpy[i]);
            lpy[i]+=1000;
        }
        for (i = 0; i < upper; i++) {
            scanf("%d %d", &upx[i], &upy[i]);
            upy[i]+=1000;
        }
        for (i = 1; i < upper; i++)
            area += 0.5 * (upy[i] + upy[i-1]) * (upx[i] - upx[i-1]);
        for (i = 1; i < lower; i++)
            area -= 0.5 * (lpy[i] + lpy[i-1]) * (lpx[i] - lpx[i-1]);
        printf("Case #%d: \n", T, area, getArea(2.5));
        for (i = 1; i < cuts; i++) {
            printf("%lf\n", binSearch(area / cuts * i, 0, width));
        }
        
    }
}
