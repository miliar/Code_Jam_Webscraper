/*
   NAME : Siwakorn Srisakaokul
   ID : ping128
   LANG : C++
   CONTEST :
   TASK :
*/
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int DP[105][105];
int n,q,T;
int in[105];
int search(int l,int r){
    int ans=1000000,s,ll=100000,rr=-1,a,b;
    for(int i=0;i<q;i++){
        if(in[i]<=r && in[i]>rr && in[i]>=l){ rr=in[i]; a=i; }
        if(in[i]>=l && in[i]<ll && in[i]<=r){ ll=in[i]; b=i; }
    }
    
    if(ll==100000 || rr==-1) return 0;
    if(DP[a][b]!=10000000) return DP[a][b];
    //printf("a");
    int ch=0;
    for(int i=b;i<=a;i++){
       // printf("$$ %d %d %d\n",l,in[i],r);
        s=search(l,in[i]-1)+search(in[i]+1,r)+r-l;
      //  printf("(( %d",s);
        ans=min(s,ans);
    }
    DP[a][b]=ans;
    return ans;
}
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large1.out","w",stdout);
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        scanf("%d %d",&n,&q);
        for(int i=0;i<105;i++)
            for(int j=0;j<105;j++) 
                DP[i][j]=10000000;
        for(int i=0;i<q;i++){ 
            scanf("%d",&in[i]);
        }
        int cost=search(1,n);
        printf("Case #%d: %d\n",t+1,cost);
    }
    return 0;
    
}

