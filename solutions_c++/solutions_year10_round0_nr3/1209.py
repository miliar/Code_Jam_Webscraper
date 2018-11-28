#include <iostream>
#include <cstring>

using namespace std;

int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    int r,k,n;
    cin>>r>>k>>n;
    int next[1000];
    long long w[1000];
    long long g[1001];
    int v[1000];
    memset(v,255,sizeof(v));

    g[0]=0;
    for(int j=1;j<=n;j++){
      cin>>g[j];
      g[j]+=g[j-1];
    }
    if(k>g[n])k=g[n];
    for(int j=0,l=n*(k/g[n]);j<n;j++){
      while(g[l%n]+g[n]*(l/n)-g[j]<=k)
        l++;
      next[j]=--l;
    }
    v[0]=0;
    w[0]=0;
    int j=0;
    for(;v[next[j]%n]==-1;j=next[j]%n){
      v[next[j]%n]=v[j]+1;
      w[next[j]%n]=w[j]+g[next[j]%n]+g[n]*(next[j]/n)-g[j];
    }
    int nv=v[j]+1-v[next[j]%n];
    long long ans=w[next[j]%n];
    r-=v[next[j]%n];
    int a=r/nv;
    ans+=(w[j]+g[next[j]%n]+g[n]*(next[j]/n)-g[j]-ans)*a;
    r-=nv*a;
    for(j=next[j]%n;r--;j=next[j]%n)
      ans+=g[next[j]%n]+g[n]*(next[j]/n)-g[j];
    
    cout<<"Case #"<<i<<": "<<ans<<endl;
  }
}

