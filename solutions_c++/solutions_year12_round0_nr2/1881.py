#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
using namespace std;
int t,t1,n,s,p,ans;
int a[10001];

int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&t);
    t1=t;
    getchar();
    while (t--){
        printf("Case #%d: ",t1-t);
        scanf("%d%d%d",&n,&s,&p);
        ans=0;
        for (int i=1;i<=n;i++){
            scanf("%d",&a[i]);
            if (a[i]==0 && a[i]>=p) ans++;
               else
                 if (a[i]!=0 && a[i]==1 && a[i]>=p) ans++;
                    else if (a[i]!=0 && a[i]!=1){
                      int x=(a[i]+2)/3;
                      if (x>=p) ans++;
                      else{
                          x=(a[i]+1)/3;x++;
                          if (x>=p && s>0){
                               s--;
                               ans++;
                          }
                     }
                  }
        }
        printf("%d\n",ans);
    }
}
