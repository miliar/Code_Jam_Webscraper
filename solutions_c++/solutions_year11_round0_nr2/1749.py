#include <stdio.h>
#include <stdlib.h>

using namespace std;

int List[50000];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test = 0;
    scanf("%d", &test);
    for(int i = 0; i < test; i++)
    {
        int Table[100][100], Map_del[100][100];
        for(int i2 = 0; i2 < 90; i2++)
        {
            for(int j2 = 0; j2 < 90; j2++)
            {
                Table[i2][j2] = -1;
                Map_del[i2][j2] = -1;
            }
        }
        int Ob;
        scanf("%d", &Ob);
        for(int j = 0; j < Ob; j++)
        {
            char x[6];
            scanf("%s", x);
            Table[x[0]-'A'][x[1]-'A'] = x[2] - 'A';
            Table[x[1]-'A'][x[0]-'A'] = x[2] - 'A';
        }
        int Del;
        scanf("%d", &Del);
        for(int j = 0; j < Del; j++)
        {
            char x[6];
            scanf("%s", x);
            Map_del[x[0] - 'A'][x[1] - 'A'] = 1;
            Map_del[x[1] - 'A'][x[0] - 'A'] = 1;
        }
        int N;
        scanf("%d", &N);
        int list = 0;
        for(int j = 0; j < N; j++)
        {
            char t[3];
            scanf("%1s", t);
            int now = t[0] - 'A';
            if(list > 0 && Table[now][List[list-1]] > -1)
            {
                List[list-1] = Table[now][List[list-1]];
                continue;
            }
            int flag_ex = 0;
            for(int k = 0; k < list; k++)
            {
                if(Map_del[now][List[k]] == 1)
                {
                    list = 0;
                    flag_ex = 1;
                    break;
                }
            }
            if(flag_ex == 1)
                continue;
            List[list++] = now;
        }
        printf("Case #%d: [", i + 1);
        for(int j = 0; j < list; j++)
        {
            printf("%c", 'A' + List[j]);
            if(j < list-1)
                printf(", ");
        }
        printf("]\n");
    }

    return 0;
}
