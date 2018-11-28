#include <stdio.h>
#include <string.h>

char d[5000][16],n[500][15*17+1];
FILE *fp;

int main(){
    int L,D,N,i,j;
    fp = fopen("A-small-attempt0.in", "r");

    
    fscanf(fp,"%d %d %d",&L,&D,&N);
        for(int z=0;z < D;z++)
        fscanf(fp,"%s",d[z]);
        for(int z=0;z < N;z++)
        fscanf(fp,"%s",n[z]);
        
        fclose(fp);
        fp = fopen("A-small.out", "w");

        for(int nn=0;nn<N;nn++){
            int count = 0;
            for(int dd=0;dd<D;dd++){
                int open = 0;
                for(i=0,j=0;i<L;i++){
                    int check = 0;
                    for(;j<strlen(n[nn]);j++){
                        if(open){
                            //printf("O");
                            if(n[nn][j] == ')'){
                                open = 0;
                                j++;
                                break;
                            }
                            else if(n[nn][j] == d[dd][i])
                                check = 1;
                        }
                        else{
                            //printf("_");
                            if(n[nn][j] == '(')
                                open = 1;
                            else if(n[nn][j] == d[dd][i]){
                                j++;
                                check = 1;
                                break;
                            }
                            else{
                                j++;
                                break;
                            }
                        }
                    }
                    if(!check)break;
                }
                if(i == L) count++;
            }
            fprintf(fp,"Case #%d: %d\n",nn+1,count);
        }
        fclose(fp);
return 0;
}
