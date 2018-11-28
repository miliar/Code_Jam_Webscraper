#include <stdio.h>

int main(int argc, char * argv[])
{
    int t,n,k;
    int m,i;
    FILE *fpin,*fpout;
    fpin=fopen("A-large.in", "r");
    fpout=fopen("out.txt", "w");
    fscanf(fpin, "%d\n", &t);
    for(i=0; i<t; i++)
    {
        fscanf(fpin, "%d %d", &n, &k);
        m=2;
        while(--n)
            m=2*m;
        while(k>m)
            k-=m;
        fprintf(fpout, "Case #%d: ", i+1);
        if(k==m-1)
            fprintf(fpout, "ON\n");
        else
            fprintf(fpout, "OFF\n");
    }
    return 0;
}
