#include <cstdio>
#include <vector>

#define MAXN 100

#define ITERATE(it, x) for(__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int C;
        scanf("%d", &C);
        vector<vector<int> > combined(26);
        ITERATE (it, combined)
            it->assign(26, -1);
        for (int i = 0; i < C; ++i)
        {
            char buf[4];
            scanf("%s", buf);
            combined[buf[0] - 'A'][buf[1] - 'A'] = buf[2] - 'A';
            combined[buf[1] - 'A'][buf[0] - 'A'] = buf[2] - 'A';
        }
        int D;
        scanf("%d", &D);
        vector<vector<bool> > opposed(26);
        ITERATE (it, opposed)
            it->assign(26, false);
        for (int i = 0; i < D; ++i)
        {
            char buf[3];
            scanf("%s", buf);
            opposed[buf[0] - 'A'][buf[1] - 'A'] = true;
            opposed[buf[1] - 'A'][buf[0] - 'A'] = true;
        }
        int N;
        scanf("%d", &N);
        char invoked[MAXN + 1];
        scanf("%s", invoked);
        vector<int> elemList;
        for (int i = 0; i < N; ++i)
        {
            elemList.push_back(invoked[i] - 'A');
            int l = (int)elemList.size();
            if (l >= 2)
            {
                int com = combined[elemList[l - 1]][elemList[l - 2]];
                if (com >= 0)
                {
                    elemList.pop_back();
                    elemList.back() = com;
                }
                else
                {
                    for (int j = 0; j < l - 1; ++j)
                    {
                        if (opposed[elemList[l - 1]][elemList[j]])
                        {
                            elemList.clear();
                            break;
                        }
                    }
                }
            }
        }
        printf("Case #%d: [", testcase);
        if (!elemList.empty())
        {
            putchar(elemList[0] + 'A');
            for (int i = 1; i < (int)elemList.size(); ++i)
                printf(", %c", elemList[i] + 'A');
        }
        printf("]\n");
    }
    return 0;
}
