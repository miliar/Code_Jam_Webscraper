#include <stdio.h>

int T, N;

int bot[200];
int pos[200];

int getNextO(int i){
    for(int j=i; j<N;j++){
        if(bot[j] == 'O'){
            return pos[j];
        }
    }
    return -1; 
}

int getNextB(int i){
    for(int j=i; j<N;j++){
        if(bot[j] == 'B'){
            return pos[j];
        }
    }
    return -1; 
}

int main(){
    scanf(" %d",&T);
    for(int t=0; t<T; t++){
        scanf(" %d", &N);
        for(int i=0; i<N; i++){
            scanf(" %c %d",&bot[i],&pos[i]);
        }
        
        
        int po = 1;
        int pb = 1;
        int time = 0;
        for(int i=0; i<N; i++){
            int no = getNextO(i);
            int nb = getNextB(i);
            while(true){
                time++;
                if(bot[i] == 'B'){
                    if(no > po) po++;
                    if(no < po) po--;
                    if(pos[i] == pb){
                        break;
                    }
                    else if(pos[i] < pb){
                        pb--;
                    }
                    else{
                        pb++;
                    }
                }
                if(bot[i] == 'O'){
                    if(nb > pb) pb++;
                    if(nb < pb) pb--;
                    if(pos[i] == po){
                        break;
                    }
                    else if(pos[i] < po){
                        po--;
                    }
                    else{
                        po++;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",t+1, time);
    
    }

}
