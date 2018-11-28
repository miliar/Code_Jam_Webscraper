#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int cs,tt = 0;

struct Node{
    int base;
    int st,ed;
};

struct Node node[10010];
int n,x,s,r,t;
double ans,has = 0.0;

bool cmp(Node a, Node b){
    return a.base < b.base;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&cs);
    while(cs --){
        scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
        for(int i=1;i<=n;i++)
            scanf("%d %d %d",&node[i].st,&node[i].ed,&node[i].base);

        node[n+1].st = 0, node[n+1].ed = node[1].st, node[n+1].base = 0;
        for(int i=1;i<n;i++){
            node[n+1+i].st = node[i].ed;
            node[n+1+i].ed = node[i+1].st;
            node[n+1+i].base = 0;
        }
        node[2*n+1].st = node[n].ed, node[2*n+1].ed = x, node[2*n+1].base = 0;

        sort(node + 1, node +1 + 2*n + 1, cmp);

        has = (double)t;
        ans = 0.0;
        for(int i=1;i<=2*n+1;i++){
            if(1.0 * (node[i].ed - node[i].st) / (node[i].base + r) <= has){
                has -= 1.0 * (node[i].ed - node[i].st) / (node[i].base + r);
                ans += 1.0 * (node[i].ed - node[i].st) / (node[i].base + r);
            }else{
                ans += has + (node[i].ed - node[i].st - has * (node[i].base + r)) / (node[i].base + s);
                has = 0;
            }
        }
        printf("Case #%d: %.10lf\n",++tt,ans);
    }
    return 0;
}
