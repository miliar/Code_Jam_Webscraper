#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int a[40][40];
bool b[40][40];
char str[210];

int ToIndex(char ch){
    return ch-'A'+1;
}

int ans[210];

int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    int t,n,m;
    scanf("%d",&t);
    for (int cas = 1; cas <= t; ++cas ){
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        scanf("%d",&n);
        while( n-- ){
            scanf("%s",str);
            int x = ToIndex(str[0]);
            int y = ToIndex(str[1]);
            a[x][y] = a[y][x] = ToIndex(str[2]);
        }
        scanf("%d",&m);
        while( m-- ){
            scanf("%s",str);
            int x = ToIndex(str[0]);
            int y = ToIndex(str[1]);
            b[x][y] = b[y][x] = true;
        }
        scanf("%d%s",&n,str);
       // printf("%d %s\n",n,str);
        int idx = 1;
        ans[idx] = ToIndex(str[0]);
        for (int i = 1; i < n; ++i){
            if( idx > 0 && a[ToIndex(str[i])][ans[idx]] ){
                ans[idx] = a[ToIndex(str[i])][ans[idx]];
            }else{
                ans[++idx] = ToIndex(str[i]);
                for (int j = 1; j < idx; ++j)
                    if( b[ToIndex(str[i])][ans[j]] ){
                        idx = 0;
                        break;
                    }
            }
        }
        printf("Case #%d: ",cas);
        printf("[");
        for (int i = 1; i <= idx; ++i){
            if( i > 1 ) printf(", ");
            printf("%c",ans[i]+'A'-1);
        }
        printf("]\n");
    }
    return 0;
}
