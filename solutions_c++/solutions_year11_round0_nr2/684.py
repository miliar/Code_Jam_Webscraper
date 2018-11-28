#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int opp[30][30];
char cmb[30][30];
char ans[200];
char str[200];
char s[5];

void init()
{
    for(int i = 0; i < 30; i++)
        for(int j = 0; j < 30; j++)
        {
            opp[i][j] = 0;
            cmb[i][j] = '#';
        }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int cases, u, n, i, j, top;
    scanf("%d", &cases);
    for(u = 1; u <= cases; u++)
    {
        init();
        scanf("%d", &n);
        for(j = 1; j <= n; j++)
        {
            scanf("%s", s);
            cmb[s[1] - 'A'][s[0] - 'A'] = cmb[s[0] - 'A'][s[1] - 'A'] = s[2];
        }
        scanf("%d", &n);
        for(j = 1; j <= n; j++)
        {
            scanf("%s", s);
            opp[s[1] - 'A'][s[0] - 'A'] = opp[s[0] - 'A'][s[1] - 'A'] = 1;
        }
        scanf("%d", &n);
        scanf("%s", str);
        top = -1;
        for(i = 0; i < n; i++)
        {
            if(!i)
            {
                ans[++top] = str[i];
                continue;
            }
            if(top >= 0 && cmb[str[i] - 'A'][ans[top] - 'A'] != '#')
                ans[top] = cmb[str[i] - 'A'][ans[top] - 'A'];
            else
                ans[++top] =str[i];
            if(top >= 0)
            {
                for(j = 0; j < top; j++)
                    if(opp[ans[j] - 'A'][ans[top] - 'A'])
                        break;
                if(j < top)
                    top = -1;
            }
        }
        printf("Case #%d: [", u);
        for(i = 0; i <= top; i++)
        {
            if(i)
                printf(" ");
            printf("%c", ans[i]);
            if(i != top)
                printf(",");
        }
        printf("]\n");
    }
    return 0;
}
