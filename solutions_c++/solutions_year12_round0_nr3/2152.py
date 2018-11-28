#include<stdio.h>
int main(){
    int t,n,i,j,ans,a,b,k;
    int f[10];

    FILE *inf, *outf;
    inf = fopen("c.in","r");
    outf = fopen("c.out","w");

    fscanf(inf,"%d",&n);
    for (t=0;t<n;t++){
        fscanf(inf,"%d %d",&a, &b);
        ans =0;
        int tmp, l=0, p=1;
        for (tmp=a;tmp>9;l++) {
            tmp/=10;
            p*=10;
        }
        for (i=a;i<b;i++){
            tmp =i;
            int top=0;
            for (j=0;j<l;j++){
                int x = tmp/p;
                tmp = (tmp - x*p)*10 + x;
                if (tmp>i && tmp<=b) {
                    for (k=0;k<top;k++)
                        if(f[k]==tmp)break;
                    if (k==top){
                        ans++;
                        f[k]=tmp;
                        top++;
                    }
                }
            }
        }
        fprintf(outf,"Case #%d: %d\n", t+1,ans);
    }
}
