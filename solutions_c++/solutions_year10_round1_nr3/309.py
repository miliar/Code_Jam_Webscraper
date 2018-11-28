#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long huge;

huge vence(huge A, huge B)
{
    if (A == B) return(0);
    if (A < B) return(vence(B,A));
    if (A >= 2*B) return(1);

    if (vence(B,A-B)) return(0);
    return(1);
}

int main(void)
{
    int caso,C;
    huge A1,A2,B1,B2;

    for(caso = 1, scanf("%d",&C); caso <= C; caso++)
    {
        scanf("%lld %lld %lld %lld",&A1,&A2,&B1,&B2);

        huge r = 0;
        for(huge a = A1; a <= A2; a++)
            for(huge b = B1; b <= B2; b++)
                r += vence(a,b);

        printf("Case #%d: %lld\n",caso,r);
    }

    return(0);
}

