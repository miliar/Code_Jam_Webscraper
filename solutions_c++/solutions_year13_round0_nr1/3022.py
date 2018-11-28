#include    <iostream>
#include    <cstdio>
#include    <cstdlib>
#include    <cstring>
#include    <cmath>
#include    <algorithm>
#include    <vector>
#include    <list>
#include    <queue>
#include    <stack>
#include    <map>
#include    <set>
#include    <utility>
#include    <climits>
#include    <cfloat>
#include    <cassert>
#define     read(n)         scanf("%d",&n)
#define     read2(n,m)      scanf("%d%d",&n,&m)
#define     read3(n,m,l)    scanf("%d%d%d",&n,&m,&l)
#define     readull(n)      scanf("%llu",&n)
#define     readll(n)       scanf("%lld",&n)
#define     init(mem)       memset(mem,0,sizeof(mem))
#define     ull             unsigned long long int
#define     ll              long long int
#define     vi              vector<int>
#define     vs              vector<string>
using namespace std;
//std::cout.sync_with_stdio(false);


char brd[4][4];
bool chk(char c){
    bool ok;
    int i;
    ok=true;
    for(i=0;i<4;i++){
        if(brd[0][i]==c or brd[0][i]=='T') continue;
        else ok=false;
    }
    if(ok) return true;
    ok=true;
    for(i=0;i<4;i++){
        if(brd[1][i]==c or brd[1][i]=='T') continue;
        else ok=false;
    }
    if(ok) return true;
    ok=true;
    for(i=0;i<4;i++){
        if(brd[2][i]==c or brd[2][i]=='T') continue;
        else ok=false;
    }
    if(ok) return true;
    ok=true;
    for(i=0;i<4;i++){
        if(brd[3][i]==c or brd[3][i]=='T') continue;
        else ok=false;
    }
    if(ok) return true;


    ok=true;
    for(i=0;i<4;i++){
        if(brd[i][0]==c or brd[i][0]=='T') continue;
        else ok=false;
    }
    if(ok) return true;
    ok=true;
    for(i=0;i<4;i++){
        if(brd[i][1]==c or brd[i][1]=='T') continue;
        else ok=false;
    }
    if(ok) return true;
    ok=true;
    for(i=0;i<4;i++){
        if(brd[i][2]==c or brd[i][2]=='T') continue;
        else ok=false;
    }
    if(ok) return true;
    ok=true;
    for(i=0;i<4;i++){
        if(brd[i][3]==c or brd[i][3]=='T') continue;
        else ok=false;
    }
    if(ok) return true;

    ok=true;
    for(i=0;i<4;i++){
        if(brd[i][i]==c or brd[i][i]=='T') continue;
        else ok=false;
    }
    if(ok) return true;
    ok=true;
    for(i=0;i<4;i++){
        if(brd[i][3-i]==c or brd[i][3-i]=='T') continue;
        else ok=false;
    }
    return ok;
}

int main(){
    int t;
    read(t);
    for(int ii=1;ii<=t;ii++){
        for(int i=0;i<4;i++){
            scanf("%s",brd[i]);
        }
        bool X=chk('X');
        bool O=chk('O');
        if(X){
            printf("Case #%d: X won\n",ii);
        }
        else if(O){
            printf("Case #%d: O won\n",ii);
        }
        else{
            bool comp=true;
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                    if(brd[i][j]=='.') comp=false;
                }
            }
            if(comp){
                printf("Case #%d: Draw\n",ii);
            }
            else{
                printf("Case #%d: Game has not completed\n",ii);
            }
        }
    }
    return 0;
}
