#include <iostream>
#include <cstdio>
using namespace std;

int t;
char a[10][10];
bool xwin, owin, kropka;

void sprawdz_pion(int X){
    int x = 0;
    int o = 0;
    int t = 0;
    
    for(int i=0; i<4; i++){
        if(a[i][X] == 'T') t++;  
        if(a[i][X] == 'X') x++; 
        if(a[i][X] == 'O') o++;
        if(a[i][X] == '.') kropka = true;    
    }
    
    if(x == 4 || (x == 3 && t == 1)) xwin = true;
    if(o == 4 || (o == 3 && t == 1)) owin = true;
}

void sprawdz_poziom(int X){
    int x = 0;
    int o = 0;
    int t = 0;
    
    for(int i=0; i<4; i++){
        if(a[X][i] == 'T') t++;  
        if(a[X][i] == 'X') x++; 
        if(a[X][i] == 'O') o++;
        if(a[X][i] == '.') kropka = true;    
    }
    
    if(x == 4 || (x == 3 && t == 1)) xwin = true;
    if(o == 4 || (o == 3 && t == 1)) owin = true;
}

void sprawdz_ukosy(){
    int x = 0;
    int o = 0;
    int t = 0;
    
    for(int i=0; i<4; i++){
        if(a[i][i] == 'T') t++;  
        if(a[i][i] == 'X') x++; 
        if(a[i][i] == 'O') o++;
        if(a[i][i] == '.') kropka = true;    
    }
    
    if(x == 4 || (x == 3 && t == 1)) xwin = true;
    if(o == 4 || (o == 3 && t == 1)) owin = true;
    
    x = 0;
    o = 0;
    t = 0;
    
    for(int i=0; i<4; i++){
        if(a[i][4-i-1] == 'T') t++;  
        if(a[i][4-i-1] == 'X') x++; 
        if(a[i][4-i-1] == 'O') o++;
        if(a[i][4-i-1] == '.') kropka = true;    
    }
    
    if(x == 4 || (x == 3 && t == 1)) xwin = true;
    if(o == 4 || (o == 3 && t == 1)) owin = true;
}

int main(){
    scanf("%d", &t);
    
    for(int q=0; q<t; q++){
        for(int i=0; i<4; i++)    
            scanf("%s", a[i]);
            
        owin = xwin = kropka = false;
        
        for(int i=0; i<4; i++)
            sprawdz_pion(i);
        for(int i=0; i<4; i++)
            sprawdz_poziom(i);
        sprawdz_ukosy();
        
        if(xwin) {printf("Case #%d: X won\n", q+1); continue; }
        if(owin) {printf("Case #%d: O won\n", q+1); continue; }
        if(kropka) {printf("Case #%d: Game has not completed\n", q+1); continue; }
        printf("Case #%d: Draw\n", q+1);
    }
    
    return 0;    
}
