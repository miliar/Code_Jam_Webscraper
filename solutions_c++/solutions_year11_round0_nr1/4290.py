/* 
 * Compiler GNU GCC (C++)
 */

#include <cstdlib>
#include <cstdio>

using namespace std;

#define my_max(x, y) ((x)>(y)?(x):(y))

struct TData
{
    char c;
    int v;
};

int main() {
    int oIndex, bIndex, bPushNr, oPushNr, round;
    int i, iM, n, nM, no, nb, ix;
    char c;
    int v;
    TData data[100];

    scanf("%d", &iM);
    for(i=1; i<=iM; ++i)
    {
        scanf("%d", &nM);
        no = nM; nb = nM;
        for(n = 0; n<nM; ++n)
        {
            scanf(" %c %d", &c, &v);
            data[n].c = c;
            data[n].v = v;
            if ('O' == c && no == nM) no = n; else
            if ('B' == c && nb == nM) nb = n;
        }
        oIndex = 1; bIndex = 1;
        round = 0;
        bPushNr = 0; oPushNr = 0;
        ix = 0;
        while(bPushNr !=0 || oPushNr !=0 || no<nM || nb<nM)
        {
            if ((0 == bPushNr) && (nb<nM))
            {
                //ustaw numerek
                bPushNr = data[nb].v;
                //znajdz kolejny
                for(n = nb+1; n<nM; ++n)
                {
                    if ('B' == data[n].c)
                    {
                        break;
                    }
                }
                nb = n;
            }
            if ((0 == oPushNr) && (no<nM))
            {
                //ustaw numerek
                oPushNr = data[no].v;
                //znajdz kolejny
                for(n = no+1; n<nM; ++n)
                {
                    if ('O' == data[n].c)
                    {
                        break;
                    }
                }
                no = n;
            }

            round++;
            if ('O' == data[ix].c && (data[ix].v == oPushNr) && (oPushNr == oIndex))
            {
                //lets press
                oPushNr = 0;
                ix++;
                if (bPushNr > bIndex) bIndex++;
                if (bPushNr < bIndex) bIndex--;
                continue;
            } else
            if ('B' == data[ix].c && (data[ix].v == bPushNr) && (bPushNr == bIndex))
            {
                //lets press
                bPushNr = 0;
                ix++;
                if (oPushNr > oIndex) oIndex++;
                if (oPushNr < oIndex) oIndex--;
                continue;
            }
            if (bPushNr > bIndex) bIndex++;
            if (bPushNr < bIndex) bIndex--;
            if (oPushNr > oIndex) oIndex++;
            if (oPushNr < oIndex) oIndex--;
        }

        printf("Case #%d: %d\n", i, round);
    }
    return 0;
}

