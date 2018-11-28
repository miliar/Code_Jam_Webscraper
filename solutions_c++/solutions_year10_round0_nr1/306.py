#include<cstdio>
using namespace std;

int main()
{
    FILE *fin, *fout;
    fin = fopen("A-large.in","r");
    fout = fopen("A-large.out","w");
    unsigned int T, N, K;
    fscanf(fin,"%d",&T);
    int t;
    for (t=1; t<=T; t++)
    {
        fscanf(fin,"%d%d",&N,&K);
        int i;
        unsigned int x=1;
        for (i=0; i<N; i++)
            x <<= 1;
        x--;
        K &= x;
        if (K == x)
            fprintf(fout,"Case #%d: ON\n",t);
        else
            fprintf(fout,"Case #%d: OFF\n",t);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
