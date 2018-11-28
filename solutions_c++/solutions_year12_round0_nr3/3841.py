#include <cstdio>
#include <algorithm>
#include <boost/lexical_cast.hpp>

int main() {
    const int POW10[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        int a, b; scanf("%d%d", &a, &b);
        int l = boost::lexical_cast<std::string>(a).size();
        int lmin = POW10[l - 1];

        int total = 0;
        for (int i = a; i <= b; i++) {
            int recs[10];
            int recn = 0;
            for (int j = 1; j <= l; j++) {
                int ii = i % POW10[j] * POW10[l - j] + i / POW10[j];
                if (ii > i && ii >= lmin && ii <= b) {
                    recs[recn++] = ii;
                }
            }
            std::sort(recs, recs + recn);
            total += std::unique(recs, recs + recn) - recs;
        }
        printf("Case #%d: %d\n", t + 1, total);
    }
}
