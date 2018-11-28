#include <iostream>
#include <cstdio>
#define fo(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
long long f[20000],l[20000],d[20000];
long long t,n,dis,ok;
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>t;
    fo(tt,1,t){
        cin>>n;
        fo(i,1,n) scanf("%d%d",&d[i],&l[i]);
        scanf("%d",&dis);
        f[1]=d[1];
        fo(i,2,n){
            f[i]=-1;
            fo(j,1,i-1){
                if (f[j]>=d[i]-d[j] && f[j]>=0){
                    f[i]=max(f[i],min(l[i],d[i]-d[j]));
                }
            }
        }
        ok=0;
        fo(i,1,n){
            if (f[i]>0 && d[i]+f[i]>=dis){
                ok=1;
                break;
            }
        }
        printf("Case #");
        printf("%d",tt);
        printf(": ");
        if (ok==0) printf("NO\n");
        else printf("YES\n");
    }
}
