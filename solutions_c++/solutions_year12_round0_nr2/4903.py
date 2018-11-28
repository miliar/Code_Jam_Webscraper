# include <stdio.h>
# include <math.h>

FILE *fin = fopen("dene.in","r");
FILE *fout = fopen("dene.out","w");

int t,n,s,p;
int glr[101];

int main()
{
    int sol;
    int i, j, ti, tj, st;

    fscanf(fin,"%d",&t);

    for(i=1; i<=t; i++) {
        fscanf(fin,"%d%d%d",&n,&s,&p);

        sol = 0;
        st = 0;

        for(j=0; j<n; j++) {
            fscanf(fin,"%d",&tj);
            ti = tj/3;
            if(2*p-(tj-ti) > 2 || tj == 0) continue;
            else
            if(p-ti == 1) {
                if(3*ti == tj) {
                    st++;
                    if(st > s) continue;
                }
            } else
            if(p-ti == 2)  {
                st++;
                if(st > s) continue;
            }
            sol++;
        }
        if(p == 0) sol = n;
        fprintf(fout,"Case #%d: %d\n",i,sol);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
