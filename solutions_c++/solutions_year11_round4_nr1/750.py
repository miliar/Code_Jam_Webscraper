//#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int nCase;
    scanf("%d", &nCase);

    for (int iCase = 1; iCase <= nCase; ++iCase) {
        unsigned X, S, R, t, N;
        scanf("%u%u%u%u%u", &X, &S, &R, &t, &N);

        //vector<unsigned> B, E, w;
        map<unsigned, unsigned> m;
        unsigned sw = 0;
        for (unsigned i = 0; i < N; ++i) {
            unsigned Bi, Ei, wi;
            scanf("%u%u%u", &Bi, &Ei, &wi);
            // B.push_back(Bi);
            // E.push_back(Ei);
            // w.push_back(wi);
            unsigned l = Ei - Bi;
            m[wi] += l;
            sw += l;
        }
        m[0] = X - sw;

        map<unsigned,unsigned>::iterator it = m.begin(), eit = m.end();
        double ans = 0.0, rt = 0.0;
        for (; it != eit; ++it) {
            double s = it->first;
            double l = it->second;
            if (fabs(rt - t) < 1e-12) {
                ans += l / (S+s);
            } else {
                double tt = l / (R+s);
                double t1 = min(t - rt, tt);
                double l1 = (R+s) * t1;
                double l2 = l - l1;
                ans += (l1 / (R+s)) + (l2 / (S+s));
                rt += t1;
                // printf("%lf %lf -> %lf\n", l, s, ans);
            }
        }

        printf("Case #%d: %.9lf\n", iCase, ans);
    }
}

