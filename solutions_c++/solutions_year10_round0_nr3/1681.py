#include<iostream>
#include<cstdio>
using namespace std;
int a[2100],g[1100],q[1100],aim[1100],v[1100];
long long s[1100];
int main(){
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int t,n,k,r;
    cin>>t;
    for(int i=1;i<=t;++i){
        scanf("%d%d%d",&r,&k,&n); int sum=0,j=0;
        for(int i=1;i<=n;++i){
            scanf("%d,",&a[i]); a[n+i]=a[i];
            if(sum<=k) sum+=a[i],j=i;
        }
        if(sum<=k) aim[1]=1,g[1]=sum;
        else{
            aim[1]=j; g[1]=sum-a[j];
            for(int i=2;i<=n;++i){
                sum-=a[i-1];
                while(sum<=k) sum+=a[++j];
                aim[i]=(j-1)%n+1;g[i]=sum-a[j];
            }
        }
        memset(v,0,sizeof(v));
        v[1]=1,q[1]=1,s[1]=g[1];
        int e=1,x;
        while(!v[aim[q[e]]]){
            x=aim[q[e]];
            v[x]=++e,q[e]=x,s[e]=s[e-1]+g[x];
        }
//    for(int i=1;i<=e;++i) cout<<q[i]<<" "; cout<<endl;
 //   for(int i=1;i<=n;++i) cout<<s[i]<<" "; cout<<endl;
  //  cout<<v[aim[q[e]]]<<endl;
        x=v[aim[q[e]]]; r-=x-1;
        long long ans=s[e]-s[x-1];
        ans*=r/(e-x+1),r%=(e-x+1);
        ans+=s[r+x-1];
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
} 
