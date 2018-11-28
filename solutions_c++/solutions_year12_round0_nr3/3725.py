#include<cmath>
#include<cstdio>
#include<cctype>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;

#define sqr(a) (a)*(a)
#define cub(a) (a)*(a)*(a)
#define for1(i,a,b) for(i=(a);i<(b);i++)
#define for2(i,a,b) for(i=(a);i>(b);i--)
#define same(a) memset((a),0,sizeof(a));
#define ll long long

int cmpint(const void*a,const void *b)
{
    if(((int*)a)[0]==((int*)b)[0])
      return ((int*)a)[1]-((int*)b)[1];
    return ((int*)a)[0]-((int*)b)[0];
}

char s[1000005];
int a[1000005];
int dis[10]={0};
int ds=0;
int ok(int k){
    int i;
    if(k<0) ds=0;
    else{
        for1(i,0,ds)
          if(dis[i]==k) return 0;
        dis[ds]=k;
        ds++;
        return 1;
    }
    return 0;
}

int main()
{
    int i,j,n,m,k,l,o,p;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    scanf("%d",&p);
    int ts,ans;
    for1(o,1,p+1){
        scanf("%d%d",&k,&l);
        ans=0;
        m=1;n=1;
        while(k>=m*10) {
            m*=10;
            n++;
        }
        for1(i,k,l+1){
            if(m*10==i) {
                m*=10;
                n++;
            }
            ok(-1);
            ts=i;
            for1(j,1,n){
                ts=ts%10*m+ts/10;
                if(ts>=k&&ts<=l&&ts<i&&ts/m>0&&ok(ts))
                 ans++;
            }
        }
        printf("Case #%d: %d\n",o,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
