#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <list>
#include <iterator>
#include <map>
#include <set>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <cctype>

typedef long long int64;

using namespace std;

int main()
{
    int numTestCase;
    scanf("%d", &numTestCase);
    for (int tc = 1; tc <= numTestCase; ++tc)
    {
        printf("Case #%d: ", tc);
        int n;
        scanf("%d", &n);
        double mind, mint;
        double ax = 0, ay = 0, az = 0, avx = 0, avy = 0, avz = 0;
        for (int i = 0; i < n; ++i)
        {
            double x, y, z, vx, vy, vz;
            scanf("%lf%lf%lf%lf%lf%lf", &x, &y, &z, &vx, &vy, &vz);
            ax += x;
            ay += y;
            az += z;
            avx += vx;
            avy += vy;
            avz += vz;
        }
        ax /= n;
        ay /= n;
        az /= n;
        avx /= n;
        avy /= n;
        avz /= n;
        double ad = sqrt(ax * ax + ay * ay + az * az);
        double av = sqrt(avx * avx + avy * avy + avz * avz);
        double cosa = (-ax * avx - ay * avy - az * avz) / (ad * av);
        if (ad < 1E-8 || av < 1E-8 || cosa <= 0)
        {
            mind = ad;
            mint = 0;
        }
        else
        {
            if (fabs(1.0 - cosa * cosa) < 1E-8)
            {
                mind = 0;
            }
            else
            {
                mind = ad * sqrt(1.0 - cosa * cosa);
            }
            mint = ad * cosa / av;
        }
        printf("%lf %lf\n", mind, mint);
    }
    return 0;
}
