#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define maxN 20000

using namespace std;

int N, D;
int d[maxN], l[maxN], r[maxN];

int main()
{
    int T;
    cin >> T;
    for (int z = 1; z <= T; z++)
    {
        memset(r, 0, sizeof r);
        cin >> N;
        for (int i = 0; i < N; i++)
            cin >> d[i] >> l[i];
        cin >> D;
        r[0] = min(l[0], d[0]);
        for (int i = 0; i < N; i++)
            if (r[i])
                for (int j = i + 1; j < N; j++)
                    if (d[i] + r[i] >= d[j])
                        r[j] = max(r[j], min(l[j], d[j] - d[i]));
        bool ans = false;
        for (int i = 0; i < N; i++)
            if (r[i] && r[i] + d[i] >= D)
            {
                ans = true;
                break;
            }
        printf("Case #%d: ", z);
        if (ans)
            puts("YES");
        else
            puts("NO");
    }
    return 0;
}