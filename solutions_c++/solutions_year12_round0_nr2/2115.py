#include<stdio.h>
int main(){
    int nn,ii,x,n,m,p;
    FILE *inf, *outf;
    inf = fopen("b.in","r");
    outf = fopen("b.out","w");

    fscanf(inf,"%d", &nn);
    for(ii=0;ii<nn;ii++){
        fscanf(inf,"%d %d %d", &n, &m, &p);
        int min1 = 3*p;
        if (p>0) min1-=2;
        int min2 = min1;
        if (p>1) min2-=2;

        int ans =0;
        for (int i=0;i<n;i++){
            fscanf(inf,"%d", &x);
            if (x>=min1) ans++; else
                if (x>=min2 && m>0){
                    ans++;
                    m--;
                }
        }
        fprintf(outf,"Case #%d: %d\n",ii+1,ans);
    }
}
