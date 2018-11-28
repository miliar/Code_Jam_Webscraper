#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

char mat[5][5];
bool cmp(char a, char b) {
    if(a=='.'||b=='.') return false;
    if(a==b) return true;
    if(a=='T'||b=='T') return true;
    return false;
}

int main() {
    //freopen("p.txt","r",stdin);
   // freopen("A-small-attempt0.out","w",stdout);
    int t,cs,i,j;
    scanf("%d",&t);
    for(cs=1;cs<=t;cs++) {
        for(i=0;i<4;i++) {
            scanf("%s",mat[i]);
        }
        bool isEnd=true;
        for(i=0;i<4;i++) {
            for(j=0;j<4;j++) {
                if(mat[i][j]=='.') isEnd=false;
            }
        }
        char winChar='N';
        char now='N';
        for(i=0;i<4;i++) {
            for(j=1;j<4;j++) {
                if(mat[i][j]=='X'||mat[i][j]=='O') now=mat[i][j];
                if(!cmp(mat[i][j],mat[i][j-1])) break;
            }
            if(j>=4) {
                winChar=now;
                break;
            }
            for(j=1;j<4;j++) {
                if(mat[j][i]=='X'||mat[j][i]=='O') now=mat[j][i];
                if(!cmp(mat[j][i],mat[j-1][i])) break;
            }
            if(j>=4) {
                winChar=now;
                break;
            }
        }
        for(i=1;i<4;i++) {
            if(mat[i][i]=='X'||mat[i][i]=='O') now=mat[i][i];
            if(!cmp(mat[i][i],mat[i-1][i-1])) break;
        }
        if(i>=4) winChar=now;
        for(i=1;i<4;i++) {
            int nowi=i;
            int nowj=3-i;
            if(mat[nowi][nowj]=='X'||mat[nowi][nowj]=='O') now=mat[nowi][nowj];
            if(!cmp(mat[nowi][nowj],mat[nowi-1][nowj+1])) break;
        }
        if(i>=4) winChar=now;
        if(winChar=='X') printf("Case #%d: X won\n",cs);
        else if(winChar=='O') printf("Case #%d: O won\n",cs);
        else if(isEnd) printf("Case #%d: Draw\n",cs);
        else printf("Case #%d: Game has not completed\n",cs);

    }
    return 0;
}
