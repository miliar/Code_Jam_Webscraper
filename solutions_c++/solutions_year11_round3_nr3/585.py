#include <stdio.h>
#include <iostream>
using namespace std;

int a[1100];
int t,n,l,h;

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C.txt","w",stdout);
    int i,j,k,ans;
    scanf("%d",&t);
    for(i=1;i<=t;++i){
        scanf("%d%d%d",&n,&l,&h);
        for(j=0;j<n;++j)
            scanf("%d",&a[j]);

        ans=-1;
        for(j=l;j<=h;++j){
            for(k=0;k<n;++k){
                if(j%a[k]!=0&&a[k]%j!=0)
                    break;
            }
            if(k==n){
                ans=j;
                break;
            }
        }
        if(ans==-1)
        cout<<"Case #"<<i<<": NO"<<endl;
        else
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}

