#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<map>
#include<set>
#include<ctime>
#include<vector>
#define fo(i,u,d) for(int i=u;i<=d;i++)
#define fr(i,u,d) for(int i=u;i>=d;i--)
using namespace std;
int miss[2000];
int a[100][2000];
int minp[1200][1200];
int f[1100][1100][15];
int n;
int wh;

int round;
void init(){
    scanf("%d",&round);
    fo(i,0,(1<<round)-1)scanf("%d",&miss[i]);
    fr(i,round-1,0)
        fo(j,0,(1<<i)-1)scanf("%d",&a[i][j]);
}
int dg(int l,int r,int now){
    if (l==r)return 0;
    if (f[l][r][now]!=-1)return f[l][r][now];
    wh++;
    f[l][r][now]=dg(l,(l+r)/2,now)+dg((l+r)/2+1,r,now)+a[wh-1][l >> (round-wh+1)];
    wh--;
    int k2=1000000000;
    if (now<minp[l][r]){
        wh++;
        int k2=dg(l,(l+r)/2,now+1)+dg((l+r)/2+1,r,now+1);
        wh--;
        if (k2<f[l][r][now])f[l][r][now]=k2;
    }
    //f[l][r][now]=min(k1,k2);
    return f[l][r][now];
}
void work(){
    n=(1<<round);
    fo(i,0,n-1){
        minp[i][i]=miss[i];
        fo(j,i+1,n-1)minp[i][j]=min(minp[i][j-1],miss[j]);
    }
    memset(f,255,sizeof(f));
    wh=0;
    int ans=dg(0,n-1,0);
    printf("%d\n",ans);
}
int main(){
    freopen("bla.in","r",stdin);
    freopen("bla.out","w",stdout);
    int ca;
    scanf("%d",&ca);
    fo(i,1,ca){
        init();
        printf("Case #%d: ",i);
        work();
    }
	return 0;
}
