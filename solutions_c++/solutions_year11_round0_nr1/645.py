#include<stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int n,p,q;
int d[110],isgo[110],in[110];
int queue[10010];
int head,tail;
int mmap[110][110];
int t,tt;

struct Node{
    char s[2];
    int u;
};
struct Node node[110];

int bfs(){
    for(int i=1;i<=n;i++)
        isgo[i] = 0;
    for(int l=1;l<=n;l++){
        for(int i=1;i<=n;i++)
            if(in[i] == 0 && isgo[i] == 0){
                for(int j=1;j<=n;j++)
                    if(mmap[i][j] != -1 && isgo[j] == 0){
                        in[j] --;
                        d[j] = max(d[j], d[i] + mmap[i][j]);
                    }
                isgo[i] = 1;
                break;
            }
    }
    return d[n];
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    while(t --){
        scanf("%d",&n);
        p = q = 0;

        for(int i=1;i<=n;i++)
            scanf("%s %d",&node[i].s,&node[i].u);

        for(int i=1;i<=n;i++)
            d[i] = 0;
        memset(mmap,-1,sizeof(mmap));
        for(int i=1;i<=n;i++){
            if(node[i].s[0] == 'O'){
                d[i] = node[i].u;
                break;
            }
        }
        for(int i=1;i<=n;i++){
            if(node[i].s[0] == 'B'){
                d[i] = node[i].u;
                break;
            }
        }
        memset(in,0,sizeof(in));
        for(int i=1;i<=n;i++)
            for(int j=i-1;j>=1;j--)
                if(node[i].s[0] == node[j].s[0]){
                    mmap[j][i] = max(mmap[j][i],abs(node[i].u - node[j].u) + 1);
                    in[i] ++;
                    break;
                }
        for(int i=1;i<n;i++){
            mmap[i][i+1] = max(1,mmap[i][i+1]);
            if(node[i].s[0] != node[i+1].s[0])
                in[i+1]++;
        }
        printf("Case #%d: %d\n",++tt,bfs());
    }
    return 0;
}
