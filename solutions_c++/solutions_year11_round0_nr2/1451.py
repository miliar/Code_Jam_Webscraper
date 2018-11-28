#include <cstdio>

char comb[30][30];
char opp[30][30];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int ti = 1; ti <= tc; ti++)
    {
        int c, d, n;
        char buf[200];
        char e[200];
        int ee = 0;

        for(int i = 0; i < 30; i++)
        for(int j = 0; j < 30; j++)
        {
        comb[i][j] = opp[i][j] = 0;
        }
        scanf("%d", &c);
        for(int i = 0; i < c; i++)
        {
            scanf("%s", buf);
            comb[buf[0]-'A'][buf[1]-'A'] = buf[2];
            comb[buf[1]-'A'][buf[0]-'A'] = buf[2];
        }
        scanf("%d", &d);
        for(int i = 0; i < d; i++)
        {
            scanf("%s", buf);
            opp[buf[0]-'A'][buf[1]-'A'] = 1;
            opp[buf[1]-'A'][buf[0]-'A'] = 1;
        }
        scanf("%d", &n);
        scanf("%s", buf);
        for(int i = 0; i < n; i++)
        {

            e[ee++] = buf[i];
            if(ee>=2)
            {
                if(comb[e[ee-1]-'A'][e[ee-2]-'A'])
                {
                    ee-=2;
                    e[ee++] = comb[e[ee+1]-'A'][e[ee]-'A'];
                    continue;
                }
                for(int j = 0; j < ee-1; j++)
                {
                    if(opp[e[j]-'A'][e[ee-1]-'A'])
                    {
                        ee=0;
                        break;
                    }
                }
            }
        }
        printf("Case #%d: [", ti);
        for(int i = 0; i < ee; i++)
        {
            if(i)printf(", ");
            printf("%c", e[i]);
        }
        printf("]\n");
    }

}
