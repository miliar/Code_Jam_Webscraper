#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;

#define sqr(x) ((x)*(x))
const int N = 20000;
pii d[N];
int dd[N];
pdd pos[N];

bool check(int N, int W, int L)
{
    for (int i = 0; i < N; i++) {
        for (int j = i+1; j < N; j++)
            if (sqr(pos[i].first-pos[j].first)+sqr(pos[i].second-pos[j].second) < sqr(dd[i] + dd[j]))
                return false;
        if (pos[i].first > W || pos[i].second > L)
            return false;
    }
    return true;
}

int main()
{
    int cases;
    scanf("%d", &cases);
    for (int T = 1; T <= cases; ++T) {
        int N, W, L;
        scanf("%d%d%d", &N, &W, &L);
        for (int i = 0; i < N; i++)
            scanf("%d", &d[i].first), d[i].second = i, dd[i] = d[i].first;
        sort(d, d+N);
        double y = 0;
        bool first = true;
        for (int i = 0; i < N; ) {
            double x = -d[i].first, yy = y;
            for (; i < N && x+d[i].first <= W; ++i) {
                if (first) {
                    pos[d[i].second] = pdd(x + d[i].first, 0);
                    yy = max(yy, y + d[i].first);
                }
                else {
                    pos[d[i].second] = pdd(x + d[i].first, y + d[i].first);
                    yy = max(yy, y + 2 * d[i].first);
                }
                x += d[i].first * 2;
            }
            first = false;
            y = yy;
        }
        if (! check(N, W, L)) {
            for (int i = N; --i >= 0; ) {
                for(;;) {
                    bool flag = true;
                    pos[i].first = 1.0*rand()/RAND_MAX*W;
                    pos[i].second = 1.0*rand()/RAND_MAX*L;
                    for (int j = i; ++j < N; )
                        if (sqr(pos[i].first-pos[j].first)+sqr(pos[i].second-pos[j].second) < sqr(d[i].first + d[j].first)+1e-9) {
                            flag = false;
                            break;
                        }
                    if (flag) break;
                }
            }
        }
        printf("Case #%d:", T);
        for (int i = 0; i < N; i++)
            printf(" %lf %lf", pos[i].first, pos[i].second);
        puts("");
    }
}
