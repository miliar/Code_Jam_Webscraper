#include<iostream>
#include<cstring>
using namespace std;
long long a[1002],r,n,k=0,kk,m=0,b[1002],d[1002],t;
int c[1002],w;
int main(){
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--){
    m=k=0;
    memset(c,0,sizeof(c));
    cin>>r>>kk>>n;
    long long qq=0;
    for(int i=0;i<n;i++){
      cin>>a[i];
      qq+=a[i];
    }
    if(kk>=qq)
      m=r*qq;
    else
    for(int i=0;i<r;i++){
      if(c[k]){
        m+=b[k];
        k=d[k];
      }else{
            long long temp=0,temp1=kk,temp2=k;
            int mark=0;
            c[k]=1;
            if(a[k]>kk)
              break;
            while(!(mark&&k==temp2)&&a[k]<=temp1){
              temp+=a[k];
              temp1-=a[k];
              k=(k+1)%n;
              mark=1;
            }
            m+=temp;
            d[temp2]=k;
            b[temp2]=temp;
            }
    }
    cout<<"Case #"<<++w<<": "<<m<<endl;
    }
    return 0;
}
