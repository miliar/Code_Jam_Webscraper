#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <map>
#include <string>

using namespace std;
struct Com{
    char base[2],to;
}com[40];
struct Disp{
    char a,b;
}dis[30];
int t,c,d,n;
char tmp[105],ans[105];
int main(int argc, char** argv) {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(int v = 1;v <= t; ++v){
        scanf("%d",&c);
        for(int i = 0;i < c; ++i){
            scanf("%s",tmp);
            com[i].base[0] = tmp[0],com[i].base[1] = tmp[1];
            com[i].to = tmp[2];
        }
        scanf("%d",&d);
        for(int i = 0;i < d; ++i){
            scanf("%s",tmp);
            dis[i].a = tmp[0],dis[i].b = tmp[1];
        }
        scanf("%d%s",&n,tmp);
        int len = 0;
        for(int i = 0;i < n; ++i){
            ans[len++] = tmp[i];
            if(len == 1) ans[len++] = tmp[++i];
            if(i >= n){len -- ;break;}
            bool flag = false;
            for(int ic = 0;ic < c; ++ic){
                if((com[ic].base[0] == ans[len-2] && com[ic].base[1] == ans[len-1]) ||
                       (com[ic].base[1] == ans[len-2] && com[ic].base[0] == ans[len-1]) ){
                    ans[len-2] = com[ic].to;len = len-1;flag = true;
                    break;
                }
            }
            if(flag) continue;
            for(int id = 0;id < d; ++id){
                if(dis[id].b == ans[len-1]){
                    int j = len-2;
                    for(;j >= 0; --j)
                        if(ans[j] == dis[id].a) {flag = true;len = 0;break;}
                }
                if(dis[id].a == ans[len-1]){
                    int j = len-2;
                    for(;j >= 0; --j)
                        if(ans[j] == dis[id].b) {flag = true;len = 0;break;}
                }
            }
            if(flag) continue;
        }
        printf("Case #%d: [",v);
        if(len == 0) printf("]\n");
        else if(len == 1) printf("%c]\n",ans[0]);
        else{
            for(int i = 0;i < len - 1; ++i){
                printf("%c, ",ans[i]);
            }
            printf("%c]\n",ans[len-1]);
        }
    }
    return 0;
}

