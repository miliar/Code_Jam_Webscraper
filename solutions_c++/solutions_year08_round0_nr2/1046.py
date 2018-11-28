#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int getmax(vector<pair<int, int> > plan) {
    sort(plan.begin(), plan.end());
    int max = 0, val = 0;
    for (int i = 0; i < plan.size(); i ++) {
        val += plan[i].second;
        max >?= val;
    }
    return max;
}

int main() {
    int n;
    scanf("%d", &n);
    for (int c = 1; c <= n; c ++) {
        int t, na, nb;
        scanf("%d %d %d", &t, &na, &nb);
        vector<pair<int, int> > aa, bb;
        for (int i = 0; i < na; i ++) {
            int a, b, c, d;
            scanf("%d:%d %d:%d", &a, &b, &c, &d);
            aa.push_back(pair<int, int>(60 * a + b, 1));
            bb.push_back(pair<int, int>(60 * c + d + t, -1));
        }
        for (int i = 0; i < nb; i ++) {
            int a, b, c, d;
            scanf("%d:%d %d:%d", &a, &b, &c, &d);
            aa.push_back(pair<int, int>(60 * c + d + t, -1));
            bb.push_back(pair<int, int>(60 * a + b, 1));
        }
        printf("Case #%d: %d %d\n", c, getmax(aa), getmax(bb));
    }
    return 0;
}
