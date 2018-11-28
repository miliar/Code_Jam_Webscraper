#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

    template<class T>
T ABS(T a)
{
    return a < 0 ? -a : a;
}

int N;
pair<char, int> a[1000];

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 0; tc < T; tc++)
    {
        printf("Case #%d: ", tc + 1);

        scanf("%d", &N);
        for (int i = 0; i < N; i++)
        {
            static char tmp[100];
            scanf("%s%d", tmp, &a[i].second);
            a[i].first = tmp[0];
        }

        int pi = 1, pj = 1;
        int ci = 0;
        for (; ci < N && a[ci].first != 'O'; ci++) ;
        int cj = 0;
        for (; cj < N && a[cj].first != 'B'; cj++) ;

        int t = 0;
        while (ci < N || cj < N)
        {
            if (ci < N && cj < N)
            {
                int di = ABS(pi - a[ci].second);
                int dj = ABS(pj - a[cj].second);

                if (di < dj)
                {
                    if (ci < cj)
                    {
                        pi = a[ci].second;
                        if (pj < a[cj].second)
                        {
                            pj += (di + 1);
                            if (pj > a[cj].second)
                            {
                                pj = a[cj].second;
                            }
                        }
                        else
                        {
                            pj -= (di + 1);
                            if (pj < a[cj].second)
                            {
                                pj = a[cj].second;
                            }
                        }
                        for (ci++; ci < N && a[ci].first != 'O'; ci++) ;
                        t += (di + 1);
                    }
                    else
                    {
                        pi = a[ci].second;
                        pj = a[cj].second;
                        for (cj++; cj < N && a[cj].first != 'B'; cj++) ;
                        t += (dj + 1);
                    }
                }
                else 
                {
                    if (ci < cj)
                    {
                        pi = a[ci].second;
                        pj = a[cj].second;
                        for (ci++; ci < N && a[ci].first != 'O'; ci++) ;
                        t += (di + 1);                        
                    }
                    else
                    {
                        pj = a[cj].second;
                        if (pi < a[ci].second)
                        {
                            pi += (dj + 1);
                            if (pi > a[ci].second)
                            {
                                pi = a[ci].second;
                            }
                        }
                        else
                        {
                            pi -= (dj + 1);
                            if (pi < a[ci].second)
                            {
                                pi = a[ci].second;
                            }
                        }
                        for (cj++; cj < N && a[cj].first != 'B'; cj++) ;
                        t += (dj + 1);
                    }
                }
            }
            else if (ci < N)
            {
                int di = ABS(pi - a[ci].second);
                pi = a[ci].second;    
                for (ci++; ci < N && a[ci].first != 'O'; ci++) ;
                t += (di + 1);
            }
            else
            {
                int dj = ABS(pj - a[cj].second);
                pj = a[cj].second;
                for (cj++; cj < N && a[cj].first != 'B'; cj++) ;
                t += (dj + 1);
            }
        }
        printf("%d\n", t);
    }
    return 0;
}

