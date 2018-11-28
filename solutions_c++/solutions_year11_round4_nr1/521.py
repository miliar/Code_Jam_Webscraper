#include <map>
#include <cstdio>

#define ITERATE(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int X, S, R, t, N;
        scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
        map<int, int> speeds;
        int sum = 0;
        for (int i = 0; i < N; ++i)
        {
            int B, E, w;
            scanf("%d%d%d", &B, &E, &w);
            speeds[w] += E - B;
            sum += E - B;
        }
        if (sum < X)
            speeds.insert(pair<int, int>(0, X - sum));
        double runLeft = (double)t;
        double time = 0.0;
        ITERATE (it, speeds)
        {
            double runSpeed = it->first + R;
            double runLen = runSpeed * runLeft;
            if (runLen <= it->second)
            {
                double walkDur = (it->second - runLen) / (it->first + S);
                time += runLeft + walkDur;
                runLeft = 0.0;
            }
            else
            {
                double runDur = it->second / runSpeed;
                time += runDur;
                runLeft -= runDur;
            }
        }
        printf("Case #%d: %.16e\n", testcase, time);
    }
    return 0;
}
