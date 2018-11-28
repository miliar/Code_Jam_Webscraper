#include<stdio.h>

int main(int argc, char * argv[])
{
    int t, r, k, n, g[1000];
    int i, j, a, gi, ki, e;
    FILE *fpin,*fpout;
    fpin=fopen("C-small-attempt0.in", "r");
    fpout=fopen("C_out.txt", "w");
    fscanf(fpin, "%d\n", &t);
    for(i=0; i<t; i++)
    {
        fscanf(fpin, "%d %d %d\n", &r, &k, &n);
        for(j=1; j<n; j++)
            fscanf(fpin, "%d ", &g[j-1]);
        fscanf(fpin, "%d\n", &g[j-1]);
        e=gi=0;
        for(j=0; j<r; j++)
        {
            ki=0;
            for(a=0; a<n; a++)
            {
                if(ki+g[gi]>k)
                    break;
                ki+=g[gi];
                gi=(gi+1)%n;
            }
            e=e+ki;
        }
        fprintf(fpout, "Case #%d: %d\n", i+1, e);
    }
    return 0;
}
