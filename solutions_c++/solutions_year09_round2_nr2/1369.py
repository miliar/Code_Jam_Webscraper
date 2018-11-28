#include <stdio.h>

FILE *fo;
FILE *fw;

int main(){
    int N,x,table[10],table2[10],ans;
    
    fo = fopen("B-small-attempt0.in","r");
    fw = fopen("B-small-attempt0.out","w");
    
    fscanf(fo,"%d",&N);
    for(int i=1;i<=N;i++){
            fscanf(fo,"%d",&x);
            int y = x;
            for(int k=1;k<10;k++)
                    table[k] = 0;
            while(y > 0){
                    table[y%10]++;
                    y/=10;
            }
            
            for(int j=x+1;1;j++){
                    for(int k=1;k<10;k++)
                    table2[k] = 0;
                    
                    int xx = j;
                    
                    while(xx> 0){
                    table2[xx%10]++;
                    xx/=10;
                    }
                    
                    int check = 1;
                    for(int k=1;k<10&&check;k++){
                                      if(table[k] != table2[k])
                                      check = 0;
                    }
                    
                    if(check){
                              ans = j;
                              break;
                    }
            }        
            fprintf(fw,"Case #%d: %d\n",i,ans);    
    }
//    while(1);
fclose(fo);fclose(fw);
return 0;
}
