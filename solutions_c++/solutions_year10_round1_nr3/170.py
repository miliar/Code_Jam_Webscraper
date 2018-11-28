#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;
int a[1000000];
int get(int x1,int x2){
    int now=0,t,temp,top=0,i;
    while(x2!=x1){
        temp=(x1-1)/x2;
        a[++top]=temp;
        t=x1;
        x1=x2;
        x2=t-x2*temp;
    }
    for(i=top;i>0;--i){
        if(a[i]<1)continue;
        if(a[i]-1>=now)now=a[i];else now=a[i]-1;
    }
    return now;
}
        

void solve(){
    int a1,a2,b1,b2,ans,i,j;
    scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
    ans=0;
    for(i=a1;i<=a2;++i)
        for(j=b1;j<=b2;++j)
            if(get(i,j)!=0){
                ++ans;
                //printf("%d %d\n",i,j);
            }
    printf("%d\n",ans);
}

int main(){
    freopen("gcjc.in","r",stdin);
    freopen("gcjc.out","w",stdout);
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;++i){
        printf("Case #%d: ",i);
        solve();
    }
}

