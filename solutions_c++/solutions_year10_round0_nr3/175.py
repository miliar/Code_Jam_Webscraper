#include <stdio.h>
#include <memory.h>

long long* groups = new long long[1000];
long long* visited = new long long[1000];
long long* peopleTaken = new long long[1001];

int main()
{
    int T;
    scanf("%d", &T);

    for (int tc = 1; tc <= T; ++tc)
    {
        long long R, k, N;
        scanf("%lld %lld %lld", &R, &k, &N);

        long long totalPeopleQueueing = 0;
        memset(visited, 0xFF, 1000*sizeof(long long));
        memset(peopleTaken, 0, 1000*sizeof(long long));

        for (int i = 0; i < N; ++i)
        {
            scanf("%lld", &groups[i]);
            totalPeopleQueueing += groups[i];
        }

        if (totalPeopleQueueing <= k)
        {
            long long money = totalPeopleQueueing * R;
            printf("Case #%d: %lld\n", tc, money);
        }
        else
        {
            long long money = 0;
            long long nextGroup = 0;

            for (int t = 0; t < R; ++t)
            {
                if (visited[nextGroup] == -1)
                {
                    // prlong longf(" >>> Ride #%d: Ride with first group %d found by the first time.\n", t + 1, nextGroup);

                    visited[nextGroup] = t;

                    while (peopleTaken[t] + groups[nextGroup] <= k)
                    {
                        peopleTaken[t] += groups[nextGroup];
                        // prlong longf(" >>> %d people took from group %d of %d, total = %d\n", groups[nextGroup], nextGroup, N, peopleTaken[t]);

                        nextGroup = (nextGroup + 1) % N;
                    }

                    money += peopleTaken[t];
                }
                else
                {
                    long long cycleSize = t - visited[nextGroup];
                    long long cycleMoney = 0;

                    for (long long visit = visited[nextGroup]; visit < t; ++visit)
                    {
                        cycleMoney += peopleTaken[visit];
                    }

                    // prlong longf(" >>> Found cycle (length = %d, from = %d, to = %d, peopleTaken = %d)\n", cycleSize, visited[nextGroup] + 1, t, cycleMoney);

                    long long remainingRuns = R - t;
                    long long numOfCycles = remainingRuns / cycleSize;

                    // prlong longf(" >>> Cycle money (cycles = %d) = %d\n", numOfCycles, numOfCycles * cycleMoney);

                    money += numOfCycles * cycleMoney;

                    long long lastCyclePartLength = remainingRuns % cycleSize;

                    // prlong longf(" >>> Last cycle part (length = %d)\n", lastCyclePartLength);

                    for (long long visit = visited[nextGroup]; visit < visited[nextGroup] + lastCyclePartLength; ++visit)
                    {
                        money += peopleTaken[visit];
                        // prlong longf(" >>> Last cycle took %d more people\n", peopleTaken[visit]);
                    }
                    break;
                }
            }

            printf("Case #%d: %lld\n", tc, money);
        }
    }

    return 0;
}
