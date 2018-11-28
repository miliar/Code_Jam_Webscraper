#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int adj[200];
int ans[200];
int a[200];
void cal(int k){
    if(ans[k]!=-1)return;
    cal(k-1);
    cal(adj[k]);
    ans[k]= max(ans[k-1],ans[adj[k]]+abs(a[adj[k]]-a[k]))+1;
    //printf("%d %d\n",k,a[adj[k]]);
  //  printf("%d %d\n",k,ans[k]);
}
int main(){
    freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out","w",stdout);
    int kase,kases=1;
    scanf("%d",&kase);
    while(kase--){
        int n;
        scanf("%d",&n);
        memset(ans,-1,sizeof(ans));
        ans[0]=0;
        a[0]=1;
        int lo=0,lb=0;
        for(int i=1;i<=n;i++){           
            char str[100];
            scanf("%s%d",str,&a[i]);
            if(str[0]=='O'){
                adj[i]=lo;
                lo = i;
            }else{
                adj[i]=lb;
                lb=i;
            }
        }
        cal(n);
        printf("Case #%d: %d\n",kases++,ans[n]);
    }
    return 0;
}
