#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    int T, N, S, p, ti;
    scanf("%d",&T);
    for (int tn=1; tn<=T; tn++)
    {
        int res = 0;
        scanf("%d %d %d ",&N, &S, &p);

        int ok = 0;
        int nie = 0;
        int moze = 0;
        while (N--)
        {
            scanf("%d",&ti);
            int a = ti/3;
            if (ti == a*3)
            {
                if (a >= p)
                    ok++;
                else if (a+1 == p && a>0)
                    moze++;
            }
            else if (ti == a*3+1)
            {
                if (a+1 >= p)
                    ok++;
            }
            else //if (ti == a*3+2)
            {
                if (a+1 >= p)
                    ok++;
                else if (a+2 == p)
                    moze++;
            }
        }
        res = ok + min(moze, S);

        printf("Case #%d: %d\n", tn, res);
    }
}
