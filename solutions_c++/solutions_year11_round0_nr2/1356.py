// B small CZM1.0
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

#define oo 1000000000
const static int maxN = 1000;

char ele[maxN], elecount;
char com[26][26];
bool opp[26][26];

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    int T;
    int C, D, N;
    int i, j;
    char s[maxN];
    int cas = 1;
    char ch;
    bool flag;
    scanf("%d", &T);
    while (T--)
    {
        memset(com, 0, sizeof(com));
        memset(opp, 0, sizeof(opp));
        scanf("%d", &C);
        for (i = 0; i < C; i++)
        {
            scanf("%s", s);
            com[ s[0]-'A' ][ s[1]-'A' ] = s[2];
            com[ s[1]-'A' ][ s[0]-'A' ] = s[2];
        }
        scanf("%d", &D);
        for (i = 0; i < D; i++)
        {
            scanf("%s", s);
            opp[ s[0]-'A' ][ s[1]-'A' ] = true;
            opp[ s[1]-'A' ][ s[0]-'A' ] = true;
        }
        scanf("%d", &N);
        scanf("%s", s);
        elecount = 0;
        for (i = 0; i < N; i++)
        {
            ch = s[i];
            while (elecount > 0 && com[ ch-'A' ][ ele[elecount-1]-'A' ])
            {
                ch = com[ ch-'A' ][ ele[elecount-1]-'A' ];
                elecount--;
            }
            flag = false;
            for (j = 0; j < elecount; j++)
            {
                if (opp[ ch-'A' ][ ele[j]-'A' ])
                {
                    flag = true;
                }
            }
            if (flag)
            {
                elecount = 0;
            }
            else
            {
                ele[elecount++] = ch;
            }
        }
        printf("Case #%d: [", cas++);
        for (i = 0; i < elecount; i++)
        {
            if (!i)
            {
                printf("%c", ele[i]);
            }
            else
            {
                printf(", %c", ele[i]);
            }
        }
        printf("]\n");
    }
    return 0;
}
