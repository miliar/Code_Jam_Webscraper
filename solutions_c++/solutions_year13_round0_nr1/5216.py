#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define For(Q,W) for(int Q=0;Q<W;Q++)
#define Forl(Q,W) for(long long Q=0;Q<W;Q++)
#define LLD long long
#define pfnl printf("\n")

//#define debug
#ifdef debug
#define db(EE) cout<<EE<<" "
#define dbn(EE) cout<<EE<<" "<<endl;
#else
#define db(EE) 
#define dbn(EE) 
#endif

bool ok(char co, char kto){ return(co==kto || co=='T');}

void solve(int test){
char pole[4][4];

For(i,4)
For(j,4){
scanf(" %c ",&pole[i][j]);
}

bool ov=false;

For(i,4){
bool ok1=true;
bool ok2=true;
For(j,4){
if(pole[i][j]=='.'||pole[i][j]=='X') ok1=false;	
if(pole[j][i]=='.'||pole[j][i]=='X') ok2=false;	
}

ov=ov||ok1;
ov=ov||ok2;
}

bool xv=false;

For(i,4){
bool ok1=true;
bool ok2=true;
For(j,4){
if(pole[i][j]=='.'||pole[i][j]=='O') ok1=false;	
if(pole[j][i]=='.'||pole[j][i]=='O') ok2=false;	
}

xv=xv||ok1;
xv=xv||ok2;
}

bool bod=false;
For(i,4)
For(j,4){
if(pole[i][j]=='.') bod=true;
}

bool ouh1=true;
For(i,4) ouh1=ouh1&&ok(pole[i][i],'O');

ov=ov||ouh1;

ouh1=true;
For(i,4) ouh1=ouh1&&ok(pole[3-i][i],'O');

ov=ov||ouh1;

bool xuh1=true;
For(i,4) xuh1=xuh1&&ok(pole[i][i],'X');

xv=xv||xuh1;

xuh1=true;
For(i,4) xuh1=xuh1&&ok(pole[3-i][i],'X');

xv=xv||xuh1;





printf("Case #%d: ",test);

if(ov) printf("O won");
else if(xv) printf("X won");
else if(bod)printf("Game has not completed");
else printf("Draw");

printf("\n");
}


int main(){

int t;
scanf("%d",&t);

For(i,t){
solve(i+1);
}

return 0;
}
