#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
using namespace std;

bool u[1001];
int g[1001];
int t,r,k,n;

int main(){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);

    scanf("%d",&t);
    for (int ttt=1;ttt<=t;ttt++){
        scanf("%d%d%d",&r,&k,&n);
        for (int i=1;i<=n;i++) scanf("%d",&g[i]);
        int count=0,p=1;
        int sum=0;
        int earn=0;
        while(1){
            memset(u,1,sizeof(u));
            while(sum+g[p]<=k&&u[p]){
                sum+=g[p];
                u[p]=false; p++;
                if (p==n+1) p=1;
            }
            earn=earn+sum;
            count++;
            sum=0;
            if (count==r) break;
        }
        printf("Case #%d: %d\n",ttt,earn);
    }
    return 0;
}
