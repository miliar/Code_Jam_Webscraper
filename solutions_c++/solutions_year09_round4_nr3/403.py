#include<stdio.h>
#include<algorithm>
using namespace std;
struct data{
    int d[25];
    bool operator<(data b)const{
        return d[0]<b.d[0];
    }
}a[110];
int c[210][210],w,used[210];
bool flow(int x,int n){
    int i;
    bool flag=0;
    if(c[x][n]>0){
        c[x][n]--;
        c[n][x]++;
        return 1;
    }
    for(i=1;i<n;i++){
        if(c[x][i]>0&&used[i]!=w){
            used[i]=w;
            flag=flow(i,n);
            if(flag){
                c[x][i]--;
                c[i][x]++;
                return flag;
            }
        }
    }
    return 0;
}
main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T,n,k,t=0,i,j,l,an,r;
    scanf("%d",&T);
    while(T--){
        memset(c,0,sizeof(c));
        an=0;
        t++;
        scanf("%d %d",&n,&k);
        for(i=1;i<=n;i++)
            for(j=0;j<k;j++)scanf("%d",&a[i].d[j]);
        sort(a+1,a+n+1);
        for(i=1;i<=n;i++){
            c[0][i]=c[i+n][n+n+1]=1;
            for(j=1;j<i;j++){
                for(l=0;l<k;l++){
                    if(a[j].d[l]>=a[i].d[l])break;
                }
                if(l==k)
                    c[j][i+n]=1;
            }
        }
        w++;
        while(flow(0,n+n+1))an++,w++;
        printf("Case #%d: %d\n",t,n-an);
    }
}
