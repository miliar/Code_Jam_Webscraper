#include <stdio.h>

int table[100][100];
int set[10000];
char symbol[10000];
char sym = 'a';


int root(int node){
    if(node == set[node])
    return node;
    return root(set[node]);
}

int main(){
    int T,H,W;
    FILE *fo;
    FILE *fw;
    
    fo = fopen("B-large.in","r");
    fw = fopen("SampleWatersheds.out","w");
    fscanf(fo,"%d",&T);
    
    for(int t=0;t<T ;t++){
            printf("%d",T);

            char sym = 'a';
            for(int i=0;i<10000;i++){
                    symbol[i] = 0;
                    set[i] = i;
            }
            fscanf(fo,"%d %d",&H,&W);
            for(int i=0;i<H;i++)
                    for(int j=0;j<W;j++)
                            fscanf(fo,"%d",&table[i][j]);
            for(int i=0;i<H;i++){
                    for(int j=0;j<W;j++){
                            int min = table[i][j],ii=i,jj=j;
                            if(i!=0) 
                                     if(table[i-1][j] < min){
                                                      min = table[i-1][j];
                                                      ii = i-1;
                                                      jj = j;
                                     }
                            if(j!=0) 
                                     if(table[i][j-1] < min){
                                                      min = table[i][j-1];
                                                      ii = i;
                                                      jj = j-1;
                                     }
                            if(j!=W-1) 
                                     if(table[i][j+1] < min){
                                                      min = table[i][j+1];
                                                      ii = i;
                                                      jj = j+1;
                                     }
                            if(i!=H-1) 
                                     if(table[i+1][j] < min){
                                                      min = table[i+1][j];
                                                      ii = i+1;
                                                      jj = j;
                                     }
                            set[i*100+j] = root(ii*100+jj);
                    }
            }

            fprintf(fw,"Case #%d:\n",t+1);
            for(int i=0;i<H;i++){
                    int rt;
                    for(int j=0;j<W;j++){
                            rt = root(i*100+j);
                            if(symbol[rt] == 0)
                                    symbol[rt] = sym++;
                            fprintf(fw,"%c ",symbol[rt]);
                    }
                    fprintf(fw,"\n");
            }
    }
    printf("END");
fclose(fo);
fclose(fw);
return 0;
}
