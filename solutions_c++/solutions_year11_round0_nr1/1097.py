#include <stdio.h>
int inst[200][2];
int TO,TB;
int pO,pB;
int N;
int tiempo;
int absoluto(int a){
    if( a < 0)
        return -a;
    return a;
}
int main(){
    int t;
    char aux;
    scanf("%d",&t);
    for(int test = 1;test <=t;test++){
        printf("Case #%d: ",test);
        scanf("%d",&N);
        TO = 0;
        TB = 0;
        pO = 1;
        pB = 1;           
        tiempo = 0;
        for(int i=0;i<N;i++){
            scanf(" %c %d",&aux,&inst[i][1]);
            if( aux=='B'){
                inst[i][0] = 1;
                int ntiempo;
                ntiempo = absoluto(inst[i][1]-pB);
                if( ntiempo < TB){
                    TB = 0;
                    tiempo+=1;
                    TO += 1;
                    
                }else{
                    ntiempo -= TB;
                    TB = 0;
                    tiempo+= ntiempo;
                    TO += ntiempo;
                    tiempo+=1;
                    TO +=1;
                }
                pB = inst[i][1];
            }else{
                inst[i][0] = 0;
                int ntiempo;
                ntiempo = absoluto(inst[i][1]-pO);
                if( ntiempo < TO){
                    TO = 0;
                    tiempo+=1;
                    TB +=1;
                }else{
                    ntiempo -= TO;
                    TO = 0;
                    tiempo += ntiempo;
                    TB += ntiempo;
                    tiempo+=1;
                    TB +=1;
                }
                pO = inst[i][1];
            }
        }
        printf("%d\n",tiempo);
    }
    return 0;
}
