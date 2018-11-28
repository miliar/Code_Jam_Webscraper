#include <iostream>
#include <stdio.h>
#include <set>
using namespace std;
char words[5010][16];
int main()
{
    int L, D, N;
    int i,j,k;
    char str[1000];
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w", stdout);



    scanf("%d %d %d", &L, &D, &N);
    for (i = 0; i < D; i ++)
        scanf("%s", words[i]);
    for ( i = 1; i <= N; i ++)
    {
        set <char> sset[15];
        int nbit = 0;
        bool bLeftPara = false;

        scanf("%s", str);
        int len = strlen(str);
        for (j = 0; j < len ; j ++)
        {
            if (str[j] =='(')
                bLeftPara = true;
            else if (str[j] ==')')
            {
                bLeftPara = false;
                nbit ++;
            }
            else if (bLeftPara)
                 sset[nbit].insert(str[j]);
            else
                sset[nbit++].insert(str[j]);
        }
        int cnt = 0;
        for (j = 0; j < D; j ++)
        {
            bool match = true;
            for (k = 0; k < L; k ++)
                if (sset[k].find(words[j][k]) == sset[k].end())
                {
                    match = false;
                    break;
                }
            if (match) cnt ++;
        }
        printf("Case #%d: %d\n", i,cnt);
    }
    return 0;
}
