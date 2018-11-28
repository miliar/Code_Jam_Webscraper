#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#define Q 1000
#define S 100

int opt[Q+1][S+1];
char engine[S+1][110];
char search[Q+1][110];
int q,s;

struct Query{
    int index;
    int eng;
    int step;
}que[1000000];
    
void input_engine(int k){
    for(int i=0;;i++){
        scanf("%c",&engine[k][i]);
        if(engine[k][i]=='\n'){
            engine[k][i]=0;
            break;
        }    
    }        
    return ;
}  

void input_search(int k){
    for(int i=0;;i++){
        scanf("%c",&search[k][i]);
        if(search[k][i]=='\n'){
            search[k][i]=0;
            break;
        }    
    }        
    return ;
}


int main(){
    int k,z;
    int i,j,l;
    for(scanf("%d",&z),k=0; k<z; k++){
        scanf("%d",&s);
        for(;;){
            char ch;
            scanf("%c",&ch);
            if(ch=='\n')  break;
        }
        //printf("OK");    
        for(i=0;i<s;i++){
            input_engine(i);
        }
        //printf("OK");
        scanf("%d",&q);
        for(;;){
            char ch;
            scanf("%c",&ch);
            if(ch=='\n')  break;
        }    
        for(i=0;i<q;i++){
            input_search(i);
        }        
        //printf("OK");
        memset(opt,-1,sizeof(opt));
                  
        for(i=0;i<q;i++){
            for(j=0;j<s;j++){
                if(strcmp(search[i],engine[j])==0)  continue;
                if(i==0){
                    if(strcmp(search[i],engine[j])!=0){
                        opt[i][j]=0;
                    }    
                    //else  opt[i][j]=-1;
                }        
                else{
                    for(l=0;l<s;l++){
                        if(opt[i-1][l]>=0){
                            if(l==j){
                                if(opt[i][j]==-1||opt[i][j]>opt[i-1][l]){
                                    opt[i][j] = opt[i-1][l];
                                }    
                            }
                            else{
                                if(opt[i][j]==-1||opt[i][j]>opt[i-1][l]+1){
                                    opt[i][j] = opt[i-1][l]+1;
                                }    
                            }    
                        }        
                    }    
                }
                //printf("opt[%d][%d]=%d\n",i,j,opt[i][j]);    
            }    
        }
        
        int ret = -1;
        for(i=0; i<s; i++){
            if(opt[q-1][i]<0)  continue;
            if(ret==-1||ret>opt[q-1][i]){
                ret = opt[q-1][i];
            }    
        }     
        printf("Case #%d: %d\n",k+1,ret);   
    }    
    return 0;
}    
