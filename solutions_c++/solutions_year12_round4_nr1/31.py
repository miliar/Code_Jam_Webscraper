#include<stdio.h>
#include<queue>
#include<string.h>
#define SIZE 11111
using namespace std;
int d[SIZE],l[SIZE],ll[SIZE],rr[SIZE],D,n,used[SIZE],ma[SIZE];
int main(){
    int T,i,j,k,cs=0;
    scanf("%d",&T);
    while(T--){
        memset(ma,0,sizeof(ma));
        memset(used,0,sizeof(used));
        scanf("%d",&n);
        for(i=1;i<=n;i++){
            scanf("%d%d",&d[i],&l[i]);
            ll[i]=rr[i]=i;
        }
        scanf("%d",&D);
        d[n+1]=D;
        queue<int>qq;
        qq.push(1);
        ma[1]=d[1];
        bool flag=0;
        while(!qq.empty()){
            int now=qq.front();qq.pop();
            used[now]=0;
            for(i=rr[now]+1;i<=n+1;i++){
                if(d[i]-d[now]<=ma[now]){
                    rr[now]=i;
                    int tmp=min(l[i],d[i]-d[now]);
                    if(tmp>ma[i]){
                        ma[i]=tmp;
                        if(!used[i]){
                            used[i]=1;
                            qq.push(i);
                        }
                    }
                }
                else break;
            }
            if(rr[now]>=n+1){
                flag=1;
                break;
            }
            for(i=ll[now]-1;i>=1;i--){
                if(d[now]-d[i]<=ma[now]){
                    ll[now]=i;
                    int tmp=min(l[i],d[now]-d[i]);
                    if(tmp>ma[i]){
                        ma[i]=tmp;
                        if(!used[i]){
                            used[i]=1;
                            qq.push(i);
                        }
                    }
                }
                else break;
            }
        }
        printf("Case #%d: %s\n",++cs,flag?"YES":"NO");
    }
    return 0;
}
