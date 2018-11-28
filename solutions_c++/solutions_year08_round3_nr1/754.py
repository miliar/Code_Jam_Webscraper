#include <stdio.h>
#include <stdlib.h>

int main () {

    FILE* fin;
    FILE* fout;
    fin = fopen ("1.in","r");
    fout = fopen ("1.out","w");
    int n,nc,lc,p,k,l,list[1002],newlist[1002],c,min,sum,i,temp;
    fscanf (fin,"%d",&n);
    for (nc=0;nc<n;nc++) {
        fscanf (fin,"%d %d %d",&p,&k,&l);
        for (lc=0;lc<l;lc++) {
            fscanf (fin,"%d",&list[lc]);
        }  

        for (sum=0,lc=0;lc<l;lc++) {
            for (c=0,min=-1;c<l;c++) {
                if (min<list[c]) {
                   min=list[c];
                   temp=c;
                }
            }
            list[temp]=-1;
            //printf ("%d ",min);
            sum+=(min*(lc/k+1));
            //printf ("%d ",min*(lc/k+1));
        }
        fprintf (fout,"Case #%d: %d\n",nc+1,sum);
    }
    
    fclose(fin);
    fclose(fout);
    system ("pause");
}
