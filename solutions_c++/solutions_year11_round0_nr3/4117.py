#include <iostream>
#include <queue>
#include <cstdio>
#include <cstdlib>
using namespace std;

long calculate(queue<long> q)
{
    long sum = q.front();
    q.pop();
    while(q.size() != 0)
    {
        long a;
        a = q.front();
        q.pop();
        sum ^= a;
    }
    return sum;
}

long sum(queue<long> q)
{
    long s = 0;
    while(q.size() != 0)
    {
        s += q.front();
        q.pop();
    }
    return s;
}

int compare(const void * a, const void * b)
{
    return ( *(long*)a > *(long*)b ? 1 : -1);
}

int main()
{
    //freopen("test.in", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, N;
    scanf("%d", &T);
    int i, j, k;
    for(k = 1; k <= T; k++)
    {
        queue<long> sean;
        queue<long> patrick;
        char result[100];
        scanf("%d", &N);
        long candy[N];
        for(i = 0; i < N; i++)
        {
            scanf("%ld", &candy[i]);
        }
        qsort(candy, N, sizeof(long), compare);
        patrick.push(candy[0]);
        for(i = 1; i < N; i++)
        {
            sean.push(candy[i]);
        }
        sprintf(result, "NO");
        while(sean.size() >= 1)
        {
            //cout << "XOR " << calculate(sean) << " " << calculate(patrick) << endl;
            //cout << "SUM " << sum(sean) << " " << sum(patrick) << endl;
            if(calculate(sean) != calculate(patrick))
            {
                patrick.push(sean.front());
                sean.pop();
            }
            else
            {
                sprintf(result, "%ld", sum(sean));
                break;
            }
        }
        printf("Case #%d: %s\n", k, result);
    }
    return 0;
}
