#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

const int maxn = 128;
const int chSize = 256;

int list[maxn];
bool base[chSize];
int comb[chSize][chSize];
bool opp[chSize][chSize];
char s[maxn];
int cas, tot, n;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    memset(base, 0, sizeof(base));
    base['Q'] = 1;
    base['W'] = 1;
    base['E'] = 1;
    base['R'] = 1;
    base['A'] = 1;
    base['S'] = 1;
    base['D'] = 1;
    base['F'] = 1;
    scanf("%d",&cas);
    for (int run = 1; run<=cas; run++ )
    {
        memset(comb, -1, sizeof(comb));
        scanf("%d",&n);
        for (int i = 0; i<n; i++ )
        {
            scanf("%s",s);
            comb[s[0]][s[1]] = s[2];
            comb[s[1]][s[0]] = s[2];
        }
        memset(opp, 0, sizeof(opp));
        scanf("%d",&n);
        for (int i = 0; i<n; i++ )
        {
            scanf("%s",s);
            opp[s[0]][s[1]] = 1;
            opp[s[1]][s[0]] = 1;
        }
        scanf("%d",&n);
        scanf("%s",s);
        tot = 0;
        for (int i=0; i<n; i++ )
        {
            if (tot == 0) 
            { 
                list[tot++] = s[i];
                continue;
            }
            int ch1 = list[tot-1], ch2 = s[i];
            if (comb[ch1][ch2]>=0)
                list[tot-1] = comb[ch1][ch2];
            else
            {
                bool oppExist = 0;
                for (int j = 0; j<tot; j++ )
                    if (opp[list[j]][ch2]) oppExist = 1;
                if (oppExist) tot = 0;
                else list[tot++] = ch2;
            }
        }
        printf("Case #%d: [",run);
        for (int i=0; i<tot; i++ )
            if (i<tot-1) printf("%c, ",list[i]);
            else printf("%c",list[i]);
        printf("]\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
