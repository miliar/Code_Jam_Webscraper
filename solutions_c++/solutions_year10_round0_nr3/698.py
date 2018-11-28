#include<iostream>
#include<algorithm>
#define maxn 1005
using namespace std;

int visit[maxn],next[maxn],a[maxn];
long long bonus[maxn];

void solve(){
    int i,j,r,k,n,tot,now,len;
    long long sum,ans,circle;
    scanf("%d%d%d",&r,&k,&n);
    sum=0;
    for(i=1;i<=n;++i){
        scanf("%d",&a[i]);
        sum+=a[i];
        next[i]=0;
        visit[i]=0;
    }
    if(sum<=k){
        cout<<sum*r<<endl;
        return;
    }
    i=1;
    tot=0;
    while(visit[i]==0){
        visit[i]=++tot;
        bonus[i]=a[i];
        j=i%n+1;
        while(bonus[i]+a[j]<=k){
            bonus[i]+=a[j];
            j=j%n+1;
        }
        next[i]=j;
        i=j;
    }
    ans=0;
    if(r<visit[i]){
        now=1;
        for(j=1;j<=r;++j){
            ans+=bonus[now];
            now=next[now];
        }
        cout<<ans<<endl;
    }
    now=1;
    while(now!=i){
        ans+=bonus[now];
        now=next[now];
    }
    r-=visit[i]-1;
    circle=bonus[now];
    len=1;
    now=next[now];
    while(now!=i){
        circle+=bonus[now];
        now=next[now];
        ++len;
    }
    ans+=r/len*circle;
    r%=len;
    for(j=1;j<=r;++j){
        ans+=bonus[now];
        now=next[now];
    }
    cout<<ans<<endl;
}

int main(){
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;++i){
        printf("Case #%d: ",i);
        solve();
    }
}
