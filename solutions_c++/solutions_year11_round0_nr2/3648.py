#include <stdio.h>
#include <string.h>

using namespace std;


int comb[100][100];
int opo[100][100];
int T,C,D,N;

char ent[200];
char resp[200];
int size;

int main(){
    scanf(" %d",&T);
    for(int t=0; t<T; t++){
        memset(comb, -1, sizeof(comb));
        memset(opo, 0, sizeof(opo));
        
        scanf(" %d",&C);
        for(int i=0; i<C; i++){
            scanf(" %s",ent);
            comb[ent[0]-'A'][ent[1]-'A'] = ent[2] - 'A';
            comb[ent[1]-'A'][ent[0]-'A'] = ent[2] - 'A';
        }
        
        scanf(" %d",&D);
        for(int i=0; i<D; i++){
            scanf(" %s",ent);
            opo[ent[0]-'A'][ent[1]-'A'] = 1;
            opo[ent[1]-'A'][ent[0]-'A'] = 1;
        }
        
        scanf(" %d",&N);
        scanf(" %s",ent);
        size = 0;
        for(int i=0; i<N; i++){
            if(size == 0){
                resp[size] = ent[i];
                size++;
            }
            else if(comb[ent[i]-'A'][resp[size-1]-'A'] != -1){
                resp[size - 1] = comb[ent[i]-'A'][resp[size-1]-'A'] + 'A';
            }
            else{
                resp[size] = ent[i];
                size++;
                for(int j = 0; j<size-1; j++){
                    if(opo[resp[size-1]-'A'][resp[j]-'A']==1){
                        size = 0;
                        break;
                    }
                }
            }
        }
        
        printf("Case #%d: [",t+1);
        for(int i=0; i<size; i++){
            if(i!=0)printf(", ");
            printf("%c",resp[i]);
        }
        printf("]\n");
    
    }
}
