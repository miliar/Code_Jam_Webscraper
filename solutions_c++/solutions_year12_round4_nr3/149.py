// g++ -Wall -O2

#include <vector>
#include <stack>
#include <cstdio>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        fprintf(stderr, "Case #%d\n", testcase);
        int N;
        scanf("%d", &N);
        vector<int> a(N - 1);
        for (int i = 0; i < N - 1; ++i)
        {
            scanf("%d", &a[i]);
            --a[i];
        }
        vector<int> earliest(N, N);
        for (int i = N - 2; i >= 0; --i)
            earliest[a[i]] = i;
        vector<int> b(N, -1);
        bool impossible = false;
        vector<int> ans(N);
        stack<int> stk;
        ans[N - 1] = 1000000000;
        b[N - 1] = ans[N - 1] - 1;
        stk.push(N - 1);
        for (int i = N - 2; i >= 0; --i)
        {
            while (stk.top() < a[i])
                stk.pop();
            if (stk.top() != a[i])
            {
                impossible = true;
                break;
            }
            if (b[a[i]] < 0)
            {
                b[a[i]] = ans[a[i]] - (int)(((long long)(ans[a[a[i]]] - ans[a[i]]) * (a[i] - earliest[a[i]]) + a[a[i]] - a[i] + 1) / (a[a[i]] - a[i]));
            }
            ans[i] = b[a[i]];
            stk.push(i);
        }
        printf("Case #%d:", testcase);
        if (impossible)
            printf(" Impossible\n");
        else
        {
            for (int i = 0; i < N; ++i)
                printf(" %d", ans[i]);
            putchar('\n');
        }
    }
    return 0;
}
