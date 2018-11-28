#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int comb[30][30];
int anul[30][30];
int q[1000];
int qsize = 0;

int main()
{
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        int i, j;
        for (i = 0; i < 30; i++)
        {
            for (j=0; j < 30; j++)
            {
                comb[i][j] = -1;
                anul[i][j] = 0;
            }
        }
        int count;
        char seq[1000];
        int a, b, c;
        scanf("%d", &count);
        for (i = 0; i < count; i++)
        {
            scanf("%s", seq);
            a = seq[0] - 'A';
            b = seq[1] - 'A';
            c = seq[2] - 'A';
            comb[a][b] = c;
            comb[b][a] = c;
        }
        scanf("%d", &count);
        for (i = 0; i < count; i++)
        {
            scanf("%s", seq);
            a = seq[0] - 'A';
            b = seq[1] - 'A';
            anul[a][b] = 1;
            anul[b][a] = 1;
        }
        scanf("%d", &count);
        scanf("%s", seq);
        qsize = 0;
        for (i = 0; i < count; i++)
        {
            a = seq[i] - 'A';
            if (qsize == 0)
            {
                q[qsize++] = a;
            }
            else
            {
                if (comb[q[qsize-1]][a] != -1)
                {
                    q[qsize-1] = comb[q[qsize-1]][a];
                }
                else
                {
                    for (j = 0; j < qsize; j++)
                    {
                        if (anul[q[j]][a]) break;
                    }
                    if (j < qsize)
                    {
                        qsize = 0;
                    }
                    else
                    {
                        q[qsize++] = a;
                    }
                }
            }
        }
        printf("Case #%d: [", t+1);
        if (qsize > 0)
        {
            printf("%c", q[0] + 'A');
            for (i = 1; i < qsize; i++)
            {
                printf(", %c", q[i] + 'A');
            }
        }
        printf("]\n");
    }
    return 0;
}
