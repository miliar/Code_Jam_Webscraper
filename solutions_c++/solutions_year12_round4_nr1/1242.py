#include<stdio.h>
int d[100000], l[100000],f[100000];
int n;
int main(){
    FILE *inf, *outf;
    inf = fopen("a.in","r");
    outf = fopen("a.out","w");
    int ii,nn,i,j,now,use;
    fscanf(inf, "%d", &nn);
    d[0]=0;
    for (ii=0;ii<nn;ii++){
        fscanf(inf,"%d", &n);
        for (i=1;i<=n;i++)
            fscanf(inf,"%d %d",&d[i], &l[i]);
        fscanf(inf,"%d",&d[n+1]);
        f[1]=d[1]+d[1];
        bool flag =false;
        if (f[1]>=d[n+1]) flag =true;
        for (i=2;i<=n;i++){
            f[i]=0;
            if (flag)break;
            for (j=1;j<i;j++)
                if(f[j]>=d[i]){
                    use=d[i]-d[j];
                    if(use>l[i])use=l[i];
                    if(f[i]<d[i]+use) f[i]=d[i]+use;
                }
            if (f[i]>=d[n+1]) flag =true;
        }
        //printf("%d %d\n",f[n],d[n+1]);
        if (flag)
            fprintf(outf,"Case #%d: YES\n", ii+1);
        else
            fprintf(outf,"Case #%d: NO\n", ii+1);
    }
    fclose(inf);
    fclose(outf);
}
