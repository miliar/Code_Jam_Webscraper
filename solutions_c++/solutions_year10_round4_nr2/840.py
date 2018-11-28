#include<cstdio>
#include<algorithm>
#include<queue>
#include<stack>
#include<vector>
#include<cstring>
using namespace std;
#define min(x,y) (((x)<(y))?(x):(y))
#define INF (1<<29)

struct node{
       int count[15];
} a[1500];

int T,p,m[1500],TMP;

void dfs(int pos){
     if (pos >= (1<<(p-1))) return;
     
     dfs(pos*2); dfs((pos*2)+1);
     for (int l=0;l<=p;++l){
         for (int r=l;r<=p;++r){
             if ((a[pos*2].count[l]!=-1) && (a[(pos*2)+1].count[r]!=-1)){
                if (a[pos].count[l]==-1) a[pos].count[l]=a[pos*2].count[l] + a[(pos*2)+1].count[r] +1;
                else a[pos].count[l]=min(a[pos].count[l], a[pos*2].count[l] + a[(pos*2)+1].count[r] +1);
             }
         }
     }
     for (int r=0;r<=p;++r){
         for (int l=r;l<=p;++l){
             if ((a[pos*2].count[l]!=-1) && (a[(pos*2)+1].count[r]!=-1)){
                if (a[pos].count[r]==-1) a[pos].count[r]=a[pos*2].count[l] + a[(pos*2)+1].count[r] +1;
                else a[pos].count[r]=min(a[pos].count[r], a[pos*2].count[l] + a[(pos*2)+1].count[r] +1);
             }
         }
     }
     
     for (int l=1;l<=p;++l){
         for (int r=l;r<=p;++r){
             if ((a[pos*2].count[l]!=-1) && (a[(pos*2)+1].count[r]!=-1)){
                if (a[pos].count[l-1]==-1) a[pos].count[l-1]=a[pos*2].count[l] + a[(pos*2)+1].count[r];
                else a[pos].count[l-1]=min(a[pos].count[l-1], a[pos*2].count[l] + a[(pos*2)+1].count[r]);
             }
         }
     }
     for (int r=1;r<=p;++r){
         for (int l=r;l<=p;++l){
             if ((a[pos*2].count[l]!=-1) && (a[(pos*2)+1].count[r]!=-1)){
                if (a[pos].count[r-1]==-1) a[pos].count[r-1]=a[pos*2].count[l] + a[(pos*2)+1].count[r];
                else a[pos].count[r-1]=min(a[pos].count[r-1], a[pos*2].count[l] + a[(pos*2)+1].count[r]);
             }
         }
     }     
}

int main(){
    scanf("%d",&T);
    for (int t=1;t<=T;++t){
        memset(a,-1,sizeof(a));
        
        scanf("%d",&p);
        for (int i=1;i<=(1<<p);++i) scanf("%d",&m[i]);
        for (int i=1;i<(1<<p);++i) scanf("%d",&TMP);
        
        TMP=(1<<(p-1));
        for (int i=1;i<=(1<<(p-1));++i){
            int x1=m[i*2 - 1], x2=m[i*2];
            if (x1 && x2) a[i+TMP-1].count[min(x1-1,x2-1)]=0;
            a[i+TMP-1].count[min(x1,x2)]=1;
        }
        dfs(1);
        
        /*for (int i=1;i<(1<<p);++i){
            for (int j=0;j<p;++j){
                printf("%d ",a[i].count[j]);
            }
            puts("");
        }*/
        
        int ans=INF;
        for (int i=0;i<=p;++i){
            if (a[1].count[i]!=-1) ans=min(ans,a[1].count[i]);
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
