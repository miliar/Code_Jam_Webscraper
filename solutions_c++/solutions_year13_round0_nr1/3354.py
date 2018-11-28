/*******************************************************************
** AUTHOR   : Wenzheng jiang
** EMAIL    : jwzh.hi@gmail.com 
** OS       : ArchLinux 
** EDITER   : VIM
******************************************************************/
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
using namespace std;

#define pf(x) printf("%d\n",x)
#define pf2(x,y) printf("%d %d\n",x,y)
#define pf3(x,y,z) printf("%d %d %d\n",x,y,z)
#define pf4(x,y,z,k)printf("%d %d %d %d\n",x,y,z,k)
#define sf(x) scanf("%d",&x)
#define sf2(x,y) scanf("%d%d",&x,&y)
#define sf3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define sf4(x,y,z,k) scanf("%d%d%d%d",&x,&y,&z,&k)
typedef long long ll;
double const eps = 1e-6;
const int inf = 0x3fffffff;
const int size = 100000 + 5;

enum state{XW,OW,Draw,NG};
char mat[5][5];
#define UPDATE(c) if(c == 'X') nx++; \
            else if(c == 'O') no++;\
            else if(c == 'T') nt++;
#define RETURN  if(nx == 4 || (nx == 3 && nt == 1)) return XW; \
                if(no == 4 || (no == 3 && nt == 1)) return OW;
 
state check()
{
    int nx,no,nt;
    bool isfull = true;
    for(int i = 0;i < 4 ; i++){
        nx = 0,no = 0,nt = 0;
        for(int j = 0; j < 4; j++){
            UPDATE(mat[i][j]);    
            if(mat[i][j] == '.') isfull = false;
        }
        RETURN;
       nx = 0,no = 0,nt = 0;
        for(int j = 0; j < 4; j++){
            UPDATE(mat[j][i]);
        }
        RETURN;
    }
    nx = 0,no = 0,nt = 0;
    for(int i = 0; i < 4; i++) UPDATE(mat[i][i]);
    RETURN;
    nx = 0,no = 0,nt = 0;
    for(int i = 0; i < 4; i++) UPDATE(mat[i][3-i]);
    RETURN;
    if(isfull) return Draw;
    return NG;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,ncase = 0;
    sf(t);
    while(t--){
        for(int i = 0; i < 4; i++) 
            scanf("%s",mat[i]);
        state st = check();
        printf("Case #%d: ",++ncase);
        switch(st){
            case XW: puts("X won");break;
            case OW: puts("O won");break;
            case NG: puts("Game has not completed");break;
            case Draw: puts("Draw");break;
        }
    }
        
}


