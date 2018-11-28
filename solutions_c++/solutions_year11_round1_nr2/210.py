/*
 * Author: ahxgw
 * Created Time:  2011-5-21 10:03:29
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
const int MaxL = 12;

int T, N, M;
char s[MaxN][MaxL];
char d[28];
bool vst[MaxL];
int cnt[26];
bool sel[MaxN];
int total;
int p[MaxN];

int main()
{
    freopen("B.out", "w", stdout);
    scanf("%d", &T);
    for (int _ = 1; _ <= T; _++)
    {
        scanf("%d%d", &N, &M);
        for (int i = 0; i < N; i++)
            scanf("%s", s[i]);
        printf("Case #%d:", _);
        while (M--)
        {
            scanf("%s", d);
            memset(p, 0, sizeof(p));
            for (int i = 0; i < N; i++)
            {
                memset(vst, 0, sizeof(vst));
                memset(cnt, 0, sizeof(cnt));
                total = 0;
                for (int j = 0; j < N; j++)
                {
                    if (strlen(s[i]) == strlen(s[j]))
                    {
                        sel[j] = 1;
                        for (int k = 0; s[j][k]; k++)
                            cnt[s[j][k] - 'a']++;
                        total++;
                    }
                    else
                        sel[j] = 0;
                }
                int t = 0;
                while (total > 1)
                {
                    while (cnt[d[t] - 'a'] == 0)
                        t++;
                    bool flag = 1;
                    for (int j = 0; s[i][j]; j++)
                        if (s[i][j] == d[t])
                        {
                            vst[j] = 1;
                            flag = 0;
                        }
                    p[i] += flag;
                    for (int j = 0; j < N; j++) if (sel[j])
                    {
                        for (int k = 0; s[j][k]; k++)
                        {
                            if (vst[k] == 1 && s[j][k] != s[i][k])
                            {
                                sel[j] = 0;
                                total--;
                                for (int m = 0; s[j][m]; m++)
                                    cnt[s[j][m] - 'a']--;
                                break;
                            }
                            else if (vst[k] == 0 && s[j][k] == d[t])
                            {
                                sel[j] = 0;
                                total--;
                                for (int m = 0; s[j][m]; m++)
                                    cnt[s[j][m] - 'a']--;
                                break;
                            }
                        }
                    }
                    t++;
                }
            }
            int mx = -1, pos = -1;
            for (int i = 0; i < N; i++)
                if (p[i] > mx)
                {
                    mx = p[i];
                    pos = i;
                }
            printf(" %s", s[pos]);
        }
        puts("");
    }

    return 0;
}
