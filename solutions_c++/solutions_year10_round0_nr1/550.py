#include<stdio.h>
int main()
{
    int T,N,K;
    int ncase = 1;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    scanf( "%d", &T);
    while(T--)
    {
        scanf("%d %d", &N,&K);
        int base = ( 1<<(N) );
        printf("Case #%d: ", ncase);
        if( (K+1)%base == 0)
            printf("ON\n");
        else
            printf("OFF\n");
        ncase++;
    }  

    return 0;
}
