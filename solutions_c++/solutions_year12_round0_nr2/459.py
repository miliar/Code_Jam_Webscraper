#include<cstdio>

int ca,i,ans,p,t,s,n,a;
int main(){
    //freopen("b.in","r",stdin);
    //freopen("b.out","w",stdout);
    scanf("%d\n",&t);
    ca=0;
    for (ca=1;ca<=t;ca++){
        printf("Case #%d: ",ca);
        scanf("%d%d%d",&n,&s,&p);
        ans=0;
        for (i=1;i<=n;i++){
            scanf("%d",&a);
            if (a>=p*3-2) ans++;
            else if (a>=p*3-4&&s>0&&a!=0) {s--; ans++;}
        }
        printf("%d\n",ans);
    }
    return 0;
}
