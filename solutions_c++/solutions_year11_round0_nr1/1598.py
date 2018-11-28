/*
 * Author: ahxgw
 * Created Time:  2011-5-7 10:00:02
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

int T, N;
char typ[MaxN][2];
int pos[MaxN];
int p1, p2;
int ans;

int main()
{
    freopen("A.out", "w", stdout);
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++)
    {
        scanf("%d", &N);
        for (int i = 0; i < N; i++)
            scanf("%s%d", typ[i], &pos[i]);
        p1 = p2 = 1;
        ans = 0;
        for (int i = 0; i < N; i++)
        {
            if (typ[i][0] == 'O')
            {
                int j = i + 1;
                while (j < N && typ[j][0] == 'O')
                    j++;
                int mov = abs(p1 - pos[i]) + 1;
                ans += mov;
                p1 = pos[i];
                if (j == N)
                    continue;
                if (abs(p2 - pos[j]) < mov)
                    p2 = pos[j];
                else if (p2 > pos[j])
                    p2 -= mov;
                else
                    p2 += mov;
            }
            else
            {
                int j = i + 1;
                while (j < N && typ[j][0] == 'B')
                    j++;
                int mov = abs(p2 - pos[i]) + 1;
                ans += mov;
                p2 = pos[i];
                if (j == N)
                    continue;
                if (abs(p1 - pos[j]) < mov)
                    p1 = pos[j];
                else if (p1 > pos[j])
                    p1 -= mov;
                else
                    p1 += mov;
            }
        }
        printf("Case #%d: %d\n", _, ans);
    }

    return 0;
}
