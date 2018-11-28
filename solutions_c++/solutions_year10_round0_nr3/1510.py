#include<cstdio>
#include<cstring>

using namespace std;

const int N=2000;

int T,test;
int r,m,n;
int i,j,k;
int a[N],b[N],c[N];
int v[N];
long long ans,t;

int main(){
    scanf("%d",&T);
    for(test=1;test<=T;++test){
        scanf("%d%d%d",&r,&m,&n);
        k=m;
        for(i=0;i<n;++i){
            scanf("%d",&a[i]);
            if(k>=0) k-=a[i];
        }
        if(k>=0){
            ans=(long long)(m-k)*r;
            printf("Case #%d: %I64d\n",test,ans);
            continue;
        }
        memset(v,0,sizeof(v));
        v[0]=1;
        b[1]=0;
        for(i=1;;++i){
            k=0;
            for(j=b[i];;){
                if(k+a[j]>m) break;
                k+=a[j];
                ++j;
                if(j==n) j=0;
            }
            c[i]=k;
            if(v[j]){
                k=v[j];
                break;
            }
            v[j]=i+1;
            b[i+1]=j;
        }
        ans=0;
        if(r>=k){
            for(j=1;j<k;++j) ans+=c[j];
            r=r-k+1;
        }
        else{
            for(j=1;j<=r;++j) ans+=c[j];
            printf("Case #%d: %I64d\n",test,ans);
            continue;
        }
        t=0;
        for(j=k;j<=i;++j) t+=c[j];
        ans=ans+t*(r/(i-k+1));
        for(j=r%(i-k+1);j>=1;--j) ans+=c[j+k-1];
        printf("Case #%d: %I64d\n",test,ans);
    }
}
