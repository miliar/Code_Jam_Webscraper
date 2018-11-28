#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

int pos[100000];
int cnt[100000];

int num[100000];
double newP[100000];

int C, D;

bool check(int num[], int count, double t)
{
    memset(newP, 0, sizeof(newP));

    newP[0] = num[0] - t;
    double nextP = newP[0] + D;

    for (int i = 1; i < count; i++)
    {
        if (num[i] > nextP)
        {
            if (fabs(num[i] - nextP) > t)
            {
//                printf("%f\n", fabs(num[i] - nextP));
                newP[i] = num[i] - t;
                nextP = newP[i] + D;
            }
            else
            {
                newP[i] = nextP;
                nextP = newP[i] + D;
            }
        }
        else
        {
            if (fabs(num[i] - nextP) > t)
            {
                return false;
            }
            else
            {
                newP[i] = nextP;
                nextP = newP[i] + D;
            }
        }
    }
    return true;
}

int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    int T;
    int cases = 1;
    scanf("%d", &T);

    double lowt = 0.0, maxt = 1000.0;
    while (T-- > 0)
    {
        scanf("%d %d", &C, &D);
//        printf("%d %d\n", C, D);
        for (int i = 0; i < C; i++)
        {
            scanf("%d %d", &pos[i], &cnt[i]);
//            printf("%d %d\n", pos[i], cnt[i]);
        }

        int count = 0;
        for (int i = 0; i < C; i++)
        {
            for (int j = 0; j < cnt[i]; j++)
            {
                num[count++] = pos[i];
            }
        }
        sort(num, num + count);

        lowt = 0.0, maxt = 1000.0;
        double midt;
        while ((maxt - lowt) > 1e-12)
        {
            midt = (lowt + maxt) / 2;
            if (check(num, count, midt) == true)
            {
                maxt = midt;
//                printf("midt %f\n", midt);
            }
            else
            {
                lowt = midt;
            }
        }
        printf("Case #%d: %f\n", cases++, lowt);
    }

    return 0;
}
