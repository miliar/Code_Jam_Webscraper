#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 200;

int main()
{
    int T, N, S, P, ans, s, lower, upper;

    scanf("%d", &T);

    for(int t = 1; T--; ++t)
    {
        ans = s = 0;
        scanf("%d%d%d", &N, &S, &P);

        upper = P+max(P-1, 0)*2;
        lower = P+max(P-2, 0)*2;

        for(int i = 0; i < N; i++)
        {
            int total;
            scanf("%d", &total);

            if(total < upper ) //try to be surprising
            {
                if(s < S && total >= lower ) ++ans, ++s;
            }
            else ++ans;
        }
        printf("Case #%d: %d\n", t, ans);
    }


    return 0;
}

