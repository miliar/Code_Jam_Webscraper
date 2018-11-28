#include<iostream>
#include<cstdio>
#include<cstring>
#define f(i,n) for (int i=0;i<n;i++)

using namespace std;

char mapa[5][5],ganador;
bool vacio;


int vertical(){

    f(j,4){
        int o=0,x=0,t=0;
        f(i,4){
            if (mapa[i][j]=='O')o++;
            else if (mapa[i][j]=='X')x++;
            else if (mapa[i][j]=='T')t++;
            else vacio=1;
            
        }
        if (o+t==4 && o>=3){ganador='O'; return 1;}
        else if(x+t==4 && x>=3){ganador='X'; return 1;}
    }   
    return 0;
}
int horizontal(){

    f(i,4){
        int o=0,x=0,t=0;
        f(j,4){
            if (mapa[i][j]=='O')o++;
            else if (mapa[i][j]=='X')x++;
            else if (mapa[i][j]=='T')t++;
            else vacio=1;
            
        }
        if (o+t==4 && o>=3){ganador='O'; return 1;}
        else if(x+t==4 && x>=3){ganador='X'; return 1;}
    }   
    return 0;


}
int diagonal(){

    int o=0,x=0,t=0;
    f(i,4){
        
        if (mapa[i][i]=='O')o++;
        else if (mapa[i][i]=='X')x++;
        else if (mapa[i][i]=='T')t++;
        else vacio=1;
        
    }   
    if (o+t==4 && o>=3){ganador='O'; return 1;}
    else if(x+t==4 && x>=3){ganador='X'; return 1;}
    
    o=0,x=0,t=0;
    f(i,4){
        
        if (mapa[i][3-i]=='O')o++;
        else if (mapa[i][3-i]=='X')x++;
        else if (mapa[i][3-i]=='T')t++;
        else vacio=1;
        
    }   
    if (o+t==4 && o>=3){ganador='O'; return 1;}
    else if(x+t==4 && x>=3){ganador='X'; return 1;}
    
    
    
    
    return 0;
}

void solve(){
   vacio=0;
   if (vertical() || horizontal() || diagonal())printf("%c won\n",ganador);
   else if (vacio) puts("Game has not completed");
   else puts("Draw");


}


int main(){
int n;
scanf("%d",&n);
gets(mapa[0]);
f(t,n){
        f(i,4)gets(mapa[i]);
        //f(i,4)puts(mapa[i]);
        
        printf("Case #%d: ",t+1);
        solve();
        
        gets(mapa[0]);
}
return 0;}
