#include <iostream>
#include <cstdio>
#include <cstring>
#include <set>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;

    scanf("%d", &t);

    for (int tt = 1; tt <= t; ++tt)
    {
        int a, b;
        scanf("%d%d", &a, &b);

        long long res = 0;
        for (int i = a; i <= b; ++i)
        {
            int t = i;
            char st[10];
            sprintf(st, "%d", t);
            int l = strlen(st);
            int k = 1;
            for (int j = 1; j != l; ++j)
            {
                k *= 10;
            }
            set<int> s;
            for (int j = 1; j != l; ++j)
            {
                int r = t % 10;
                t = t / 10 + k * r;
                if (s.find(t) == s.end() && t >= a && t <= b && i < t)
                {
                    ++res;
                    s.insert(t);
                    //printf("%d %d\n", i, t);
                }
            }
        }

        printf("Case #%d: %lld\n", tt, res);
    }

    return 0;
}
