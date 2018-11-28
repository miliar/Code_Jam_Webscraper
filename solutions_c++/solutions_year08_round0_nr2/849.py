#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

struct Trip
{
    int type;
    int from;
    int to;
};

const int BufferSize = 10000;

int n;
int t;
int na, nb;
char buf[BufferSize];
Trip trips[BufferSize];
int availA[BufferSize];
int availB[BufferSize];
int needA;
int needB;

bool Compare(const Trip &t1, const Trip &t2)
{
    return t1.from < t2.from;
}

int main()
{
    scanf("%d", &n);
    for (int index = 1; index <= n; ++index)
    {
        scanf("%d", &t);
        scanf("%d %d", &na, &nb);
        for (int i = 0; i < na; ++i)
        {
            trips[i].type = 0;

            int hour, min;
            scanf("%2d:%2d", &hour, &min);
            trips[i].from = hour*60 + min;

            scanf("%2d:%2d", &hour, &min);
            trips[i].to = hour*60 + min;
        }

        for (int i = na; i < na + nb; ++i)
        {
            trips[i].type = 1;

            int hour, min;
            scanf("%2d:%2d", &hour, &min);
            trips[i].from = hour*60 + min;

            scanf("%2d:%2d", &hour, &min);
            trips[i].to = hour*60 + min;
        }

        sort(trips, trips + na + nb, Compare);

        int len = 24 * 60;
        fill_n(availA, len, 0);
        fill_n(availB, len, 0);
        needA = 0;
        needB = 0;
        int k = 0;
        for (int i = 0; i < len; ++i)
        {
            if (i != 0)
            {
                availA[i] += availA[i-1];
                availB[i] += availB[i-1];
            }

            while (k < na + nb && trips[k].from == i)
            {
                if (trips[k].type == 0)
                {
                    if (availA[i] == 0)
                    {
                        ++availA[i];
                        ++needA;
                    }

                    --availA[i];
                    ++availB[trips[k].to + t];
                }
                else
                {
                    if (availB[i] == 0)
                    {
                        ++availB[i];
                        ++needB;
                    }

                    --availB[i];
                    ++availA[trips[k].to + t];
                }

                ++k;
            }
        }

        printf("Case #%d: %d %d\n", index, needA, needB);
    }

    return 0;
}