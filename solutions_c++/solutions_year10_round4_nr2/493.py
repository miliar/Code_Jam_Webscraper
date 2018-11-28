#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<stdlib.h>
#define SIZE 13 
#define MAX 700000000
using namespace std;
int t,a[4096],v[2048][2048];
int two[SIZE],N;
int Min(int x,int y){return x<y?x:y;}
void dfs(int x,int y,int d[]){
    int i,j,k;
    //printf("%d %d\n",x,y);
    if(x+1==y){
        k=Min(a[x],a[y]);
        k=Min(k,N);
        for(i=0;i<=N;i++)d[i]=MAX;
        if(k==0)
            d[0]=v[x][y];
        else{
            d[k-1]=0;
            d[k]=v[x][y];
        }
        return;
    }
    int d1[SIZE],d2[SIZE];
    for(i=0;i<=N;i++)d[i]=MAX;
    dfs(x,(x+y)/2,d1);
    dfs((x+y)/2+1,y,d2);
    for(i=0;i<=N;i++){
        for(j=0;j<=N;j++){
            k=Min(i,j);
            d[k]=Min(d[k],d1[i]+d2[j]+v[x][y]);
            if(k)
                d[k-1]=Min(d[k-1],d1[i]+d2[j]);
        }
    }
}
main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,an,i,j;
    int d[SIZE];
    two[0]=1;
    for(i=1;i<SIZE;i++)two[i]=two[i-1]*2;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&N);
        for(i=0;i<two[N];i++)scanf("%d",&a[i]);
        for(i=1;i<=N;i++){
            for(j=0;j<two[N];j+=two[i])
                scanf("%d",&v[j][j+two[i]-1]);
        }
        dfs(0,two[N]-1,d);
        an=MAX;
        for(i=0;i<=N;i++)an=Min(an,d[i]);
        printf("Case #%d: %d\n",++t,an);
    }
}
