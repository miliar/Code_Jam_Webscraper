#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int inf = 99999999;

int S, Q;
char s[101][105], q[1001][105];

int main()
{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
        int i, j, k;
        int r, t = 0;
        scanf("%d", &r);
        while(r--)
        {
                scanf("%d", &S);
                gets(s[0]);
                for(i = 1; i <= S; ++i) gets(s[i]);
                scanf("%d", &Q);
                gets(q[0]);
                for(i = 1; i <= Q; ++i) gets(q[i]);

                int m = inf;
                int d[1001][101];
                char match[1001][101] = {0};

                for(i = 1; i <= Q; ++i)
                        for(j = 1; j <= S; ++j)
                                match[i][j] = (strcmp(q[i], s[j]) == 0) ? 1 : 0;

                fill(d[0], d[Q + 1], inf);
                for(i = 1; i <= Q; ++i)
                        for(j = 1; j <= S; ++j)
                        {
                                if(match[i][j]) continue;
                                if(i == 1) d[i][j] = 0;
                                else
                                {
                                        for(k = 1; k <= S; ++k)
                                                d[i][j] = min(d[i][j], d[i - 1][k] + (j != k));
                                }
                                if(i == Q) m = min(m, d[i][j]);
                        }
                if(m == inf) m = 0;
                printf("Case #%d: %d\n", ++t, m);
        }

        return 0;
}
