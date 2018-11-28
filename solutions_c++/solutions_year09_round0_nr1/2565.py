#include <iostream>
#include <stdio.h>
#include <set>
using namespace std;
char words[5010][16];
int main()
{
    int L, D, N;
    int total;
    int i,j,k;
    char str[1000];
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w", stdout);


    int last;
    scanf("%d %d %d", &L, &D, &N);
    for (i = 0; i < D; i ++)
    {
        scanf("%s", words[i]);
    }
    for ( i = 1; i <= N; i ++)
    {
        scanf("%s", str);
        set <char> chset[15];
        int len = strlen(str);
        int bits = 0;
        bool bBracket = false;

        for (j = 0; j < len ; j ++)
        {
            if (str[j] =='(')
            {
                bBracket = true;
            }
            else if (str[j] ==')')
            {
                bBracket = false;
                bits ++;
            }
            else if (bBracket)
            {
                chset[bits].insert(str[j]);
            }
            else
            {
                chset[bits++].insert(str[j]);

            }
        }
        total = 0;
        for (j = 0; j < D; j ++)
        {
            bool isok = true;
            for (k = 0; k < L; k ++)
                if (chset[k].find(words[j][k]) == chset[k].end())
                {
                    isok = false;
                    break;
                }
            if (isok) total ++;
        }
        printf("Case #%d: %d\n", i,total);
    }
    return 0;
}
