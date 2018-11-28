#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
char chinachen[800][800];
int YNCA[800][800],YNCB[800][800];
int work(){
    int R,C,D;
    scanf("%d%d%d",&R,&C,&D);
    for(int i=1;i<=R;i++) scanf("%s",chinachen[i]+1);
    for(int i=1;i<=R;i++) YNCA[i][0]=0;
    for(int i=1;i<=R;i++) YNCB[i][0]=0;
    for(int i=1;i<=R;i++){
        for(int j=1;j<=C;j++){
            YNCA[i][j]=YNCA[i][j-1];
            YNCA[i][j]+=chinachen[i][j]-'0';
        }
    }
    for(int j=1;j<=C;j++){
        for(int i=1;i<=R;i++){
            YNCB[i][j]=YNCB[i-1][j];
            YNCB[i][j]+=chinachen[i][j]-'0';
        }
    }
    int ans = 0;
    for(int i=R;i>1;i--){
        for(int j=C;j>1;j--){
            for(int p=2;i-p>=1;p++){
                if(p%2==0){
                    if(p+1<=ans) continue;
                    int rp=0;
                    for(int t=i-p;t<=i;t++){
                        rp+=(i-p/2-t)*(YNCA[t][j]-YNCA[t][j-p-1]);
                    }
                    int tp1=(chinachen[i-p][j-p]-'0'+chinachen[i-p][j]-'0');
                    rp-=(i-p/2-(i-p))*tp1;
                    int tp2=(chinachen[i][j-p]-'0'+chinachen[i][j]-'0');
                    rp-=(i-p/2-i)*tp2;
                    if(rp!=0) continue;
                    rp=0;
                    for(int t=j-p;t<=j;t++){
                        rp+=(j-p/2-t)*(YNCB[i][t]-YNCB[i-p-1][t]);
                    }
                    tp1=(chinachen[i-p][j-p]-'0'+chinachen[i][j-p]-'0');
                    rp-=(i-p/2-(i-p))*tp1;
                    tp2=(chinachen[i-p][j]-'0'+chinachen[i][j]-'0');
                    rp-=(i-p/2-i)*tp2;
                    if(rp!=0) continue;
                    if(p+1>ans) ans=p+1;
                }else {
                    if (p+1<=ans) continue;
                    int rp=0;
                    int chen=(p+1)/2;
                    for(int t=i-p;t<=i;t++,chen==1?chen-=2:chen--){
                        rp+=(chen)*(YNCA[t][j]-YNCA[t][j-p-1]);
                    }
                    int tp1=(chinachen[i-p][j-p]-'0'+chinachen[i-p][j]-'0');
                    rp-=((p+1)/2)*tp1;
                    int tp2=(chinachen[i][j-p]-'0'+chinachen[i][j]-'0');
                    rp-=(-(p+1)/2)*tp2;
                    if(rp!=0) continue;
                    rp=0;
                    chen=(p+1)/2;
                    for(int t=j-p;t<=j;t++,chen==1?chen-=2:chen--){
                        rp+=(chen)*(YNCB[i][t]-YNCB[i-p-1][t]);
                    }
                    tp1=(chinachen[i-p][j-p]-'0'+chinachen[i][j-p]-'0');
                    rp-=((p+1)/2)*tp1;
                    tp2=(chinachen[i-p][j]-'0'+chinachen[i][j]-'0');
                    rp-=(-(p+1)/2)*tp2;
                    if(rp!=0) continue;
                    if(p+1>ans) ans=p+1;
                }
            }
        }
    }
    return ans;
}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++){
        int ans=work();
        if(ans==0) printf("Case #%d: IMPOSSIBLE\n",ca);
        else printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
