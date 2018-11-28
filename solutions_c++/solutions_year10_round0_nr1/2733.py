#include<stdio.h>

FILE *inf,*ouf;

int main(){
    
    int n ,k,t,i,ii=0;
    bool tag;
    inf = fopen("A-large.in","r");  
    ouf = fopen("A-large.out","w");
    
    fscanf(inf,"%d",&t);
    while(ii++,t--){
    fscanf(inf,"%d%d",&n,&k);
    
           for(tag=1,i=0;tag==1&&i<n;i++,k>>=1)
                       tag = k&1;                                           
             if(tag)fprintf(ouf,"Case #%d: ON \n",ii); 
            if(!tag)fprintf(ouf,"Case #%d: OFF \n",ii);
    
    
              }
           }
