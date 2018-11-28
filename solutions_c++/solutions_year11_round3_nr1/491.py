#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>
#include <complex>
#define MAXN 105
using namespace std;

char map[MAXN][MAXN];
int main(){
    int T,R,C;
    freopen("A-large.in","r",stdin);
    freopen("aLout.txt","w",stdout);
    scanf("%d",&T);
    for(int k=1;k<=T;k++){
        scanf("%d%d",&R,&C);
        for(int i=0;i<R;i++){
            scanf(" %s",map[i]);
        }
        bool flag=true;
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                if(map[i][j]=='#'){
                    if(j+1>=C || i+1>=R){
                        flag=false;
                        break;
                    }
                    if(map[i][j+1]!='#' || map[i+1][j]!='#' || map[i+1][j+1]!='#'){
                        flag=false;
                        break;
                    }
                    map[i][j]='/';
                    map[i][j+1]='\\';
                    map[i+1][j]='\\';
                    map[i+1][j+1]='/';
                }
            }
            if(!flag)break;
        }
        printf("Case #%d:\n",k);
        if(!flag)printf("Impossible\n");
        else{
            for(int i=0;i<R;i++)printf("%s\n",map[i]);
        }
    }
    return 0;
}
