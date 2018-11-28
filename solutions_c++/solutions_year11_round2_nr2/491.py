#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

const double EPS = 1e-8;

int main() {
    freopen("D:\\TopCoder\\gcj2011\\R1\\B.in", "r", stdin);
    freopen("D:\\TopCoder\\gcj2011\\R1\\B.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ca++) {
        int C, D;
        scanf("%d %d", &C, &D);
        int P[C], V[C], tot = 0;
        for (int i = 0; i < C; i++) {
            scanf("%d %d", &P[i], &V[i]);
            tot += V[i];
        }
        
        double ans = 0, low = 0, up = D * tot;
        //cout << low << "-->" << up << endl;//
        while (fabs(up - low) > EPS) {
            double mid = (up + low) / 2;
            double lft = P[0] - mid, rgt;
            bool flag = true;
            for (int i = 0; i < C; i++) {
                if (V[i] == 0) continue;
                if (P[i] > lft && P[i] - mid > lft) lft = P[i]-mid;
                else if (P[i] < lft && lft-mid > P[i]) {
                    flag = false;
                    break;
                }
                rgt = lft + (V[i]-1) * D;
                //cout << " " << i << "," << mid << ": " << P[i] << "," << V[i] << "  " << lft << "-->" << rgt << endl;//
                if (rgt > P[i] && rgt-mid > P[i]) {
                    flag = false;
                    break;
                }
                lft = rgt + D;
            }
            if (flag) up = mid;
            else low = mid;
            //cout << mid << " = " << flag << ": " << low << "-->" << up << endl;//
            ans = mid;
        } 
        printf("Case #%d: %.7lf\n", ca, ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}


