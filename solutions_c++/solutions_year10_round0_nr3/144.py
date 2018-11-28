#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#define SIZE 1024

using namespace std;

int pos[SIZE], get[SIZE], group[SIZE];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int C = 0, T;

    scanf("%d", &T);
    while (T--)
    {
        int R, k, N;
        scanf("%d %d %d", &R, &k, &N);
        for (int i = 0; i < N; i++)
            scanf("%d", &group[i]);
        memset(get, 0, sizeof(get));
        memset(pos, -1, sizeof(pos));
        for (int i = 0; i < N; i++)
        {
            int j = i;
            get[i] = group[i];
            while (get[i] <= k)
            {
                j = (j + 1) % N;
                get[i] += group[j];
                if (j == i)break;
            }
            get[i] -= group[j];
            pos[i] = j;
        }
        long long res = 0;
        int flag = 0;
        for (int i = 0; i < R; i++)
        {
            res += get[flag];
            flag = pos[flag];
        }
        cout << "Case #" << ++C << ": " << res << endl;
    }

    return 0;
}
