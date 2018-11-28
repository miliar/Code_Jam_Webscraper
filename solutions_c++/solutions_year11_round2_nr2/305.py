#include <cstdio>
#include <string>
#include <vector>
#include <memory.h>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;



int main() {

    int t;
    int c;
    int d;

    vector<double> poses;

    scanf("%d", &t);

    for (int test = 1;test <= t;++test) {

        scanf("%d%d", &c, &d);

        double a;
        int b;

        poses.clear();

        for (int i = 0;i < c;++i) {
            scanf("%lf%d", &a, &b);
            for (int j = 0;j < b;++j)
                poses.push_back(a);
        }

        double left = 0.0;
        double right = d * poses.size() + 1.0;

        while (right - left > 1e-7) {

            double middle = (left + right) / 2;

            bool test = true;

            double ll = -1e100;

            for (int i = 0;i < poses.size();++i) {
                if (poses[i] + middle <= ll) {
                    test = false;
                    break;
                }
                ll = max(ll, poses[i] - middle) + d;
            }

            if (test)
                right = middle;
            else
                left = middle;
        }

        printf("Case #%d: %.7lf\n", test, left);
    }

    return 0;
}
