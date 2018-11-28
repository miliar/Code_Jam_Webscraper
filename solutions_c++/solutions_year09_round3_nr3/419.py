#include<cstdio>
#include<string.h>
#include<algorithm>
using namespace std;
#define INF 2147483600

int n,p,q,qs[10],ans;
bool con[105];

int main(){
    scanf("%d",&n);
    for (int t=1;t<=n;++t){
        ans=INF;
        scanf("%d%d",&p,&q);
        for (int i=1;i<=q;++i) scanf("%d",&qs[i]);
        do{
            int cc=0;
            memset(con,1,sizeof(con));
            for (int i=1;i<=q;++i){
                con[qs[i]]=0;
                for (int l=qs[i]-1;l>=1;--l){
                    if (con[l]) ++cc; else break;
                }
                for (int r=qs[i]+1;r<=p;++r){
                    if (con[r]) ++cc; else break;
                }
            }
            if (cc<ans) ans=cc;
        }while(next_permutation(qs+1,qs+1+q));
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
