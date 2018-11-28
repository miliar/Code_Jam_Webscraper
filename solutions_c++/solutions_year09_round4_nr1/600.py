#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
    int caso,T,N,m[64],r;
    char s[64];

    scanf("%d",&T);
    for(caso = 1; caso <= T; caso++)
    {
        scanf("%d",&N);
        for(int i = 0; i < N; i++)
        {
            scanf("%s",s);
            m[i+1] = 0;
            for(int j = 0; j < N; j++)
                if (s[j] == '1')
                    m[i+1] = j+1;
        }
        /*
        for(int i = 1; i <= N; i++)
            printf("[%d]",m[i]);
        printf("\n");
        */

        r = 0;
        for(int i = 1; i <= N; i++)
        {
            if (m[i] <= i) continue;
            for(int j = i+1; j <= N; j++)
                if (m[j] <= i)
                {
                    int temp = m[j];
                    for(int k = j; k > i; k--)
                        m[k] = m[k-1];
                    m[i] = temp;
                    r += (j-i);
                    break;
                }
        }
        /*
        for(int i = 1; i <= N; i++)
            printf("[%d]",m[i]);
        printf("\n");
        */

        printf("Case #%d: %d\n",caso,r);
    }

    return(0);
}

