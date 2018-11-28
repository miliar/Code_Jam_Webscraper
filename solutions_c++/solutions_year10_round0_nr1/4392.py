#include<stdio.h>
#include<math.h>
int main(){
    int t,n,k,j;
    FILE *i=fopen("A-small-attempt0.in","r");
    FILE *o=fopen("A-small-attempt0.out","w");
    //cin>>T;
    fscanf(i,"%d",&t);
    for(int j=1;j<=t;j++){
               fscanf(i,"%d %d",&n,&k);
               int a=pow(2,n)-1;
               if((a&k)==a) fprintf(o,"Case #%d: ON\n",j);
               else  fprintf(o,"Case #%d: OFF\n",j);
    }
    return 0;
}
