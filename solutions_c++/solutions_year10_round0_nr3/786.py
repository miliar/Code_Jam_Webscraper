#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <cassert>
using namespace std;
int sizes[1000];
void problem(int id)
{
    int r, k, n;
    assert(3 == scanf("%d%d%d", &r, &k, &n));
    for (int i = 0; i < int (n); ++i)
        assert(1 == scanf("%d", sizes + i));
    vector < pair < int, long long > > cache(n);
    int pos = 0;
    long long acc = 0;
    for (int i = 0; i < int (r); ++i) {
        if (cache[pos].first) {
            int diter = i - cache[pos].first;
            long long dacc = acc - cache[pos].second;
            int d = (r - i) / diter;
            if (d) {
                i += d * diter;
                assert(i <= r);
                acc += d * dacc;
                i--;
                continue;
            }
        }
        cache[pos] = pair < int, long long >(i, acc);
        long long have = 0;
        int spos = pos;
        while ((!have || pos != spos) && have + sizes[pos] <= k) {
            have += sizes[pos];
            pos = (pos + 1) % n;
        }
        acc += have;
    }
    printf("Case #%d: ", id + 1);
    printf("%lld\n", acc);
}
int main(int argc, char **argv)
{
    int n;
    assert(1 == scanf("%d", &n));
    int id = 0;
    while (n--) {
        problem(id++);
    }
    return 0;
}
