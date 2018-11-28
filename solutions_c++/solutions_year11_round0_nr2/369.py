#include <cstdio>
#include <cstring>

using namespace std;

const int maxL = 128;
const int maxN = 10240;

int nxt[maxN];
bool opp[maxN];

int main()
{
    //freopen("B2.in", "r", stdin);
    //freopen("B2.out", "w", stdout);

    int cas;
    char str[maxL];
    char res[maxL];

    scanf("%d", &cas);
    for(int cc = 0; cc < cas; cc++)
    {
        memset(nxt, -1, sizeof(nxt));
        memset(opp, false, sizeof(opp));

        int C, D, N;

        scanf("%d", &C);
        for(int i = 0; i < C; i++)
        {
            scanf("%s", str);

            int a = str[0] - 'A';
            int b = str[1] - 'A';
            int c = str[2] - 'A';

            nxt[a * 100 + b] = nxt[b * 100 + a] = c;
        }

        scanf("%d", &D);
        for(int i = 0; i < D; i++)
        {
            scanf("%s", str);

            int a = str[0] - 'A';
            int b = str[1] - 'A';

            opp[a * 100 + b] = opp[b * 100 + a] = true;
        }

        scanf("%d", &N);
        scanf("%s", str);

        int top = -1;

        for(int i = 0; i < N; i++)
        {
            res[++top] = str[i];

            bool ok = true;
            while(ok)
            {
                ok = false;
                if(top >= 1)
                {
                    int last = (res[top - 1] - 'A') * 100 + (res[top] - 'A');
                    if(nxt[last] != -1)
                    {
                        res[top - 1] = nxt[last] + 'A';
                        top--;
                        ok = true;
                    }
                }
            }

            if(top >= 1)
            {
                for(int i = 0; i < top; i++)
                {
                    int last = (res[i] - 'A') * 100 + (res[top] - 'A');
                    if(opp[last])
                    {
                        top = -1;
                        break;
                    }
                }
            }
        }

        printf("Case #%d: [", cc + 1);
        for(int i = 0; i <= top; i++)
        {
            if(i) printf(", ");
            printf("%c", res[i]);
        }
        printf("]\n");
    }
    return 0;
}
