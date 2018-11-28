#include<stdio.h>
#define M 100000000
int T,n;
char r[11][M];
char c,s[99];
bool f(int x,int y){
    r[x][y]=-1;
    int k=y,w=0;
    bool flag;
    while(k>0){
        w+=(k%x)*(k%x);
        k/=x;
    }
    if(r[x][w]==1){
        r[x][y]=1;
        return 1;
    }
    else if(r[x][w]==-1){
        return 0;
    }
    else{
        flag=f(x,w);
        if(flag)r[x][y]=1;
        return flag;
    }
}
main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,a[19],n,t=0;
    for(j=2;j<=10;j++)r[j][1]=1;
    scanf("%d",&T);
    gets(s);
    while(T--){
        n=0;
        while(scanf("%d%c",&a[n++],&c)){
            if(c=='\n')break;
        }
        for(i=2;;i++){
            for(j=0;j<n;j++){
                f(a[j],i);
                if(r[a[j]][i]!=1)break;
            }
            if(j==n)break;
        }
        printf("Case #%d: %d\n",++t,i);
    }
}
