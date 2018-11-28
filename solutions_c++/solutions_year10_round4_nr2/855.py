#include"iostream"
#include"algorithm"
#include"cstdlib"
using namespace std;
int a[2050];
int fun(int l,int r,int p){
    int res=0;
    int mid=(l+r)/2;
    bool flag=true;
    for(int i=l;i<=r;i++){
       if(a[i]<p){flag=false;break;}
    }
    if(!flag){
              
         res++;
         for(int i=l;i<=r;i++){
            a[i]++;
         }
         res=res+fun(l,mid,p)+fun(mid+1,r,p);
    }
    return res;
}
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("Bsout.txt","w",stdout);
    int T;
    int P;
    int n,pr;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
         scanf("%d",&P);
         n=1<<P;
         for(int j=0;j<n;j++){
            scanf("%d",&a[j]);
         }
         for(int j=1;j<=P;j++){
            for(int k=0;k<(n>>j);k++){
               scanf("%d",&pr);
            }
         }
         printf("Case #%d: %d\n",i,fun(0,n-1,P));
    }
    return 0;
}
