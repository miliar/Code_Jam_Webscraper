#include<cstdio>
int flag[1100],pim[1100],tol;
void init()
{
    tol=0;
    for(int i=2;i<1100;i++){
        if(!flag[i]) pim[tol++]=i;
        for(int j=0;j<tol&&i*pim[j]<1100;j++){
            flag[i*pim[j]]=1;
            if(i%pim[j]==0) break;
        }
    }
}
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T,ca=0;
    init();
    scanf("%d",&T);
    while(T--){
        int n;
        scanf("%d",&n);
        int ans1=0,ans2=0;
        for(int i=0;i<tol;i++){
            if(pim[i]>n) break;
            ans1++;
            int p=0;
            for(int j=1;j<=n;j++){
                int c=0,t=j;
                while(t%pim[i]==0) { c++; t/=pim[i];}
                if(p<c) p=c;
            }
            ans2+=p;
        }
        if(n!=1) ans2++;
        printf("Case #%d: %d\n",++ca,ans2-ans1);
    }
}
