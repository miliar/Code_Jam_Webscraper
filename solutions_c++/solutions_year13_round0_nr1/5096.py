#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <string.h>
#include <queue>
#include <map>
#include <set>
#include <math.h>
#include <sstream>
using namespace std;

typedef long long ll;
const double pi = acos(-1.0);
const double eps = 1e-8;

const int dx[8]={1,0,-1,0,-1,-1,1,1};
const int dy[8]={0,1,0,-1,1,-1,1,-1};
const int days[13]={0,31,28,31,30,31,30,31,31,30,31,30,31};
const int leap[13]={0,31,29,31,30,31,30,31,31,30,31,30,31};

char s[11][11];
int n,m;

bool chk(int x,int y){
    int ret=1,tx,ty;
    for (int i=0;i<8;++i){
        int now=1;
        tx=x,ty=y;
        while (tx+dx[i]>=0 && tx+dx[i]<4 && ty+dy[i]>=0 && ty+dy[i]<4 && (s[tx+dx[i]][ty+dy[i]]==s[x][y] || s[tx+dx[i]][ty+dy[i]]=='T')){
            ++now;
            tx+=dx[i];
            ty+=dy[i];
        }
        tx=x,ty=y;
        while (tx-dx[i]>=0 && tx-dx[i]<4 && ty-dy[i]>=0 && ty-dy[i]<4 && (s[tx-dx[i]][ty-dy[i]]==s[x][y] || s[tx-dx[i]][ty-dy[i]]=='T')){
            ++now;
            tx-=dx[i];
            ty-=dy[i];
        }
        ret=max(ret,now);
    }
    return (ret==4);
}

int main(){
    int _,cas=0;
    scanf("%d",&_);
    while (_--){
        n=m=0;
        for (int i=0;i<4;++i) scanf("%s",s[i]);
        for (int i=0;i<4;++i)
            for (int j=0;j<4;++j)
                if (s[i][j]!='.'){
                    if (!chk(i,j)) continue;
                    if (s[i][j]=='O') n=1;
                    else n=2;
                }else m=1;
        if (!n){
            if (m) printf("Case #%d: Game has not completed\n",++cas);
            else printf("Case #%d: Draw\n",++cas);
        }else{
            if (n==1) printf("Case #%d: O won\n",++cas);
            else printf("Case #%d: X won\n",++cas);
        }
    }
    return 0;
}
