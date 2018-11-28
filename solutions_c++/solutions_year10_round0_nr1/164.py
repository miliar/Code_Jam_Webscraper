#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
    int N,K,T,caso;

    for(scanf("%d",&T), caso = 1; caso <= T; caso++)
    {
        scanf("%d %d",&N,&K);
        int b = (1<<N);

        printf("Case #%d: %s\n",caso,(K >= b-1 && ((K-b+1)%b) == 0) ? "ON" : "OFF");
    }

    return(0);
}

