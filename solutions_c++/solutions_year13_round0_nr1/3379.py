//Template of CyberKasumi (Jennifer Santoso a.k.a. Liang Qiuxia)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <queue>
using namespace std;

#define LL long long
#define inf 2123123123
#define MOD 1000000007


int a;
int b;
char t[6][6]={0};
bool xwinhori(int row){
    int x=0,o=0,pt=0;
    for (int i=0;i<4;i++){
        if (t[row][i]=='X')x++;
        else if (t[row][i]=='T')pt++;
        else if (t[row][i]=='O')o++;
    }
    if (x==4)return true;
    else if (x==3 && pt==1)return true;
    return false;
}
bool xwinverti(int row){
    int x=0,o=0,pt=0;
    for (int i=0;i<4;i++){
        if (t[i][row]=='X')x++;
        else if (t[i][row]=='T')pt++;
        else if (t[i][row]=='O')o++;
    }
    if (x==4)return true;
    else if (x==3 && pt==1)return true;
    return false;
}
bool xwindiagdown(){
    int x=0,o=0,pt=0;
    for (int i=0;i<4;i++){
        if (t[i][i]=='X')x++;
        else if (t[i][i]=='T')pt++;
        else if (t[i][i]=='O')o++;
    }
    if (x==4)return true;
    else if (x==3 && pt==1)return true;
    return false;
}
bool xwindiagup(){
    int x=0,o=0,pt=0;
    for (int i=0;i<4;i++){
        if (t[i][3-i]=='X')x++;
        else if (t[i][3-i]=='T')pt++;
        else if (t[i][3-i]=='O')o++;
    }
    if (x==4)return true;
    else if (x==3 && pt==1)return true;
    return false;
}
bool owinhori(int row){
    int x=0,o=0,pt=0;
    for (int i=0;i<4;i++){
        if (t[row][i]=='X')x++;
        else if (t[row][i]=='T')pt++;
        else if (t[row][i]=='O')o++;
    }
    if (o==4)return true;
    else if (o==3 && pt==1)return true;
    return false;
}
bool owinverti(int row){
    int x=0,o=0,pt=0;
    for (int i=0;i<4;i++){
        if (t[i][row]=='X')x++;
        else if (t[i][row]=='T')pt++;
        else if (t[i][row]=='O')o++;
    }
    if (o==4)return true;
    else if (o==3 && pt==1)return true;
    return false;
}
bool owindiagdown(){
    int x=0,o=0,pt=0;
    for (int i=0;i<4;i++){
        if (t[i][i]=='X')x++;
        else if (t[i][i]=='T')pt++;
        else if (t[i][i]=='O')o++;
    }
    if (o==4)return true;
    else if (o==3 && pt==1)return true;
    return false;
}
bool owindiagup(){
    int x=0,o=0,pt=0;
    for (int i=0;i<4;i++){
        if (t[i][3-i]=='X')x++;
        else if (t[i][3-i]=='T')pt++;
        else if (t[i][3-i]=='O')o++;
    }
    if (o==4)return true;
    else if (o==3 && pt==1)return true;
    return false;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&a);
    for (int z=1;z<=a;z++){
        gets(t[0]);
        bool complete=true;
        for (int j=0;j<4;j++){
            scanf("%s",t[j]);
            for (int k=0;k<4;k++){
                if (t[j][k]=='.')complete=false;
            }
        }
        //cek
        bool xwin=xwindiagup() || xwindiagdown();
        for (int i=0;i<4;i++){
            xwin=xwin||(xwinhori(i))||(xwinverti(i));
        }
        bool owin=owindiagup() || owindiagdown();
        for (int i=0;i<4;i++){
            owin=owin||(owinhori(i)) || owinverti(i);
        }
        printf("Case #%d: ",z);
        if (xwin && owin)printf("Draw\n");
        else if (complete && !xwin && !owin)printf("Draw\n");
        else if (xwin && !owin)printf("X won\n");
        else if (owin && !xwin)printf("O won\n");
        else printf("Game has not completed\n");
    }
    //while(1);
    return 0;
}
