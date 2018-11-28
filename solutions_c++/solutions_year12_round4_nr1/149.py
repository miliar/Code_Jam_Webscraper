// g++ -Wall -O2

#include <vector>
#include <stack>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int N;
        scanf("%d", &N);
        vector<int> pos(N + 1);
        vector<int> len(N);
        for (int i = 0; i < N; ++i)
            scanf("%d%d", &pos[i], &len[i]);
        int D;
        scanf("%d", &D);
        pos[N] = D;
        vector<int> radius(N, 0);
        stack<int> s;
        radius[0] = pos[0];
        s.push(0);
        bool ans = false;
        while (!s.empty())
        {
            int t = s.top();
            s.pop();
            for (int i = t + 1; ; ++i)
            {
                if (pos[t] + radius[t] < pos[i])
                    break;
                if (i >= N)
                {
                    ans = true;
                    goto l_done;
                }
                int rnew = min(pos[i] - pos[t], len[i]);
                if (rnew > radius[i])
                {
                    radius[i] = rnew;
                    s.push(i);
                }
            }
        }
    l_done:
        printf("Case #%d: %s\n", testcase, ans ? "YES" : "NO");
    }
    return 0;
}
