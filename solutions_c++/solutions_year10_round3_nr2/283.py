

#include<vector>
#include<sstream>
#include<iostream>
#include<cstring>
#include<cmath>
#include<string>
#include<map>


using namespace std;

int Y1[1003], Y2[1003];

int main() {
    //  freopen("B-small1.in", "r", stdin);
    //   freopen("B-small.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int nth = 1; nth <= cas; nth++) {
        double C, P, L;
        scanf("%lf%lf%lf", &L, &P, &C);
        double K = P / L;
        int ans = 0;
        while (K > C) {
            K = sqrt(K);
            ans++;
        }
        printf("Case #%d: %d\n", nth, ans);
    }
    return 0;
}
