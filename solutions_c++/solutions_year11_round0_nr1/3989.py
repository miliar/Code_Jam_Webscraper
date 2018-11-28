#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>
using namespace std;
int main()
{
    int t,n,i,nt,aux,tO,tB,pO,pB,tcur,inc;
    char c;
    fflush(stdin);
    scanf("%i",&nt);
    for (t = 0;t<nt;t++)
    {
        tcur = 0;
        pO = 1;
        pB = 1;
        tO = 0;
        tB = 0;
        scanf("%i\n",&n);
        for (i = 0;i < n;i++)
        {
            scanf("%c %i ",&c,&aux);
            if (c == 'O')
            {
                inc = abs(aux-pO)+1;
                if (tO+inc > tcur)
                {
                    tcur = tO+inc;
                }
                else
                    tcur++;
                tO = tcur;
                pO = aux;
            }
            else
            {
               inc = abs(aux-pB)+1;
                if (tB+inc > tcur)
                {
                    tcur = tB+inc;
                }
                else
                    tcur++;
                tB = tcur;
                pB = aux;
            }
        }
        printf("Case #%i: %i\n",t+1,tcur);
    }
    return 0;
}
