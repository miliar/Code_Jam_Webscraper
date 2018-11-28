#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
    FILE* fin = fopen("A-large.in","r");
    FILE* fout= fopen("A-large.out","w");
    
    long long nLL,n;
    int t,pd,pg,i,j,k,temp;
    
    fscanf(fin,"%d",&t);
    
    for (i=1;i<=t;++i){
       fscanf (fin,"%lld %d %d",&nLL,&pd,&pg);
       
       //fprintf(fout,"n= %lld pd= %d pg =%d ",nLL,pd,pg);
       n = nLL;
        temp = -1;
        for (j=1;j<=n;++j){
            if ( pd*j % 100==0 ){
                 temp = 0;
                 break;
            }    
        }          
                    
        if (pg  == 100 && pd != 100) temp = -1;
        if (pg == 0 && pd !=0) temp = -1;
        
        fprintf(fout,"Case #%d: ",i);
        
        
        
        if (temp == 0) fprintf(fout,"Possible\n");
        else fprintf(fout,"Broken\n");
    }
    return 0;
}
        
