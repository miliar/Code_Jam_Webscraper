/*
 * Author: ahxgw
 * Created Time:  2011-5-7 10:33:28
 * Description: 
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) fprintf(stderr, "%s: %I64d\n", #v, (long long)(v))
#define SZ(v) ((int)(v).size())
#define p_b push_back
#define m_p make_pair
const int maxint = -1u>>1;
template<class T> void toMax(T &a, T b) {if (b > a) a = b;}
template<class T> void toMin(T &a, T b) {if (b < a) a = b;}

const int MaxN = 110;
const int CH = 257;

int T, C, D, N;
char q[MaxN];
int cnt;
char com[CH][CH];
bool opp[CH][CH];
char s[MaxN];

int main()
{
    freopen("B.out", "w", stdout);
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++)
    {
        cnt = 0;
        memset(com, 0, sizeof(com));
        memset(opp, 0, sizeof(opp));
        scanf("%d", &C);
        for (int i = 0; i < C; i++)
        {
            scanf("%s", s);
            com[s[0]][s[1]] = s[2];
            com[s[1]][s[0]] = s[2];
        }
        scanf("%d", &D);
        for (int i = 0; i < D; i++)
        {
            scanf("%s", s);
            opp[s[0]][s[1]] = 1;
            opp[s[1]][s[0]] = 1;
        }
        scanf("%d%s", &N, s);
        for (int i = 0; i < N; i++)
        {
//            printf("%c %d\n", s[i], cnt);
            bool oppl = 0;
            q[cnt++] = s[i];
            while (cnt > 1 && com[q[cnt - 1]][q[cnt - 2]])
            {
                q[cnt - 2] = com[q[cnt - 1]][q[cnt - 2]];
                cnt--;
                oppl = 1;
            }
            if (oppl) continue;
            for (int j = 0; j < cnt - 1; j++)
                if (opp[q[j]][s[i]])
                {
                    cnt = 0;
                    break;
                }
        }
        printf("Case #%d: [", _);
        int i;
        for (i = 0; i < cnt - 1; i++)
            printf("%c, ", q[i]);
        if (i == cnt - 1)
            printf("%c]\n", q[i]);
        else
            printf("]\n");
    }

    return 0;
}
