#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
    int i,j,k,temp,count,sum;
    int ar[2000][2]={0},val[1020]={0};
    int t,n;
    FILE* fin = fopen("D-large.in","r");
    FILE* fout=fopen("D-large.out","w");
    
    fscanf(fin,"%d",&t);
    for (i=1;i<=t;++i){
        for (j=0;j<=1500;++j){
            ar[j][0]=0;
            ar[j][1]=0;
        }
        fscanf(fin,"%d",&n);
        ar[0][0]=n;
        for (j=1;j<=n;++j) fscanf(fin,"%d",&ar[j][0]);
        count = 1;

        for (j=1;j<=n;++j){
            temp=0;
            k=j;
            if (ar[k][1]==0){
                while (ar[k][1]==0){
                      ar[k][1]=count;
                      temp++;
                      k = ar[k][0];
                }
                val[0]=count;
                val[count]=temp;
                count++;
            }
        }
        
        sum = 0;
        for (j=1;j<=val[0];++j){
            sum += val[j];
            if (val[j]==1) --sum;
            //fprintf(fout,"val[%d] = %d\n",j,val[j]);
        }
        fprintf(fout,"Case #%d: %.6lf\n",i,(double)sum);
    }
    return 0;
}
                  
