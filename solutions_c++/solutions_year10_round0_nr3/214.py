#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, const char *argv[])
{
    int t;
    scanf("%d", &t);

    long r, k, n;
    vector<long> groups;
    vector<long> nextIndex;
    vector<long> income;
    long long total;

    int i;
    for (i = 0; i < t; i++)
    {
        scanf("%ld%ld%ld", &r, &k, &n);
        long j;
        groups.clear();
        for (j = 0; j < n; j++)
        {
            long tmp;
            scanf("%ld", &tmp);
            groups.push_back(tmp);
        }
        // finish reading, now solve it
        nextIndex.resize(n, 0);
        income.resize(n, 0);
        for (j = 0; j < n; j++)
        {
            // prepare nextIndex and income
            long end = (j + 1) % n;
            long people = groups[j];
            while((end != j) && (people + groups[end] <= k))
            {
                people += groups[end];
                end = (end + 1) % n;
            }
            nextIndex[j] = end;
            income[j] = people;
        }
        // let's go for r rounds
        long p = 0;
        total = 0;
        for (j = 0; j < r; j++)
        {
            total += income[p];
            p = nextIndex[p];
        }
        cout << "Case #" << i + 1 << ": " << total << endl;
    }
    return 0;
}
