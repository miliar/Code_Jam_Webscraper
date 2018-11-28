#include <stdio.h>
int n,Pd,Pg;
int Gd,D,Gg,G;
int MCD(int a,int b){
    int aux;
    if( a < b){
        aux = a;
        a = b;
        b = aux;
    }
    while( b!=0){
        aux = a%b;
        a = b;
        b = aux;
    }
    return a;
}
void caso(){
    scanf("%d %d %d",&n,&Pd,&Pg);
    if( Pg == 100 && Pd!=100){
        printf("Broken");
        return;
    }
    if( Pg == 0 && Pd!=0  ){
        printf("Broken");
        return;
    }
    int MCDd = MCD(Pd,100);
    Gd = Pd / MCDd;
    D = 100/MCDd;
    int MCDg = MCD(Pg,100);
    if( D > n){
        printf("Broken");
        return;
    }
    Gg = Pg / MCDg;
    G = 100/MCDg;
    
    if( D > n){
        printf("Broken");
        return; 
    }
    printf("Possible");
}
int main(){
    int t;
    scanf("%d",&t);
    for(int i =1;i<=t;i++){
        printf("Case #%d: ",i);
        caso();
        printf("\n");
    }
    return 0;
}
