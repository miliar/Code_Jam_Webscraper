#include <stdio.h>

int main()
{
    int T,N,K;
    int i=0,standard;

    scanf("%d",&T);
    while(i!=T)
    {
        scanf("%d%d",&N,&K);
        printf("Case #%d: ",i+1);
        standard=1;
        standard=(standard<<N)-1;
        if((standard&K)==standard) printf("ON\n");
        else printf("OFF\n");
        i++;
    }
}
