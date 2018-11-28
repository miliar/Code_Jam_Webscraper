#include<stdio.h>
#include<stdlib.h>
#include<math.h>



int main(){
    int i,j,k,count,temp,min,sum,res;
    int can[1500]={0};
    int t,n;
    FILE* fin=fopen("C-large.in","r");
    FILE* fout=fopen("C-large.out","w");
    
    fscanf(fin,"%d",&t);
    for (i=1;i<=t;++i){
        fscanf(fin,"%d",&n);
        can[0]=n;
        for (j=1;j<=n;++j) fscanf(fin,"%d",&can[j]);
        
        temp = 0;
        sum = 0;
        min = 2000000;
        for (j=1;j<=n;++j){
            if (can[j] < min) min = can[j];
            sum += can[j];
            temp = temp^can[j];
        }
        res = sum - min;
        fprintf(fout,"Case #%d: ",i);
        if (temp != 0) fprintf(fout,"NO\n");
        else if (temp == 0) fprintf(fout,"%d\n",res);
    }
    
    return 0;
}
    
