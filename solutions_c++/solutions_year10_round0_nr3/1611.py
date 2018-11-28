#include<iostream>
using namespace std;

long a[1000];
long f[1000];
long c[1000];
long t,r,k,n;
long long ans;

void init(){
     memset(a,0,sizeof(a));
     memset(f,0,sizeof(f));
     scanf("%d%d%d",&r,&k,&n);
     for(int i=0;i<n;i++) scanf("%d",&a[i]);
     for(int i=0;i<n;i++) {
             long sum=0;
             for(int j=0;j<n;j++){
                     if(sum+a[(i+j)%n]<=k){
                         sum+=a[(i+j)%n];
                         f[i]++;
                     }
                     else break;
             }
             c[i]=sum;
     }       
}     

void doit(){
     long start=0;
     ans=0;
     for(int i=1;i<=r;i++){
             ans+=c[start];
             start=(start+f[start])%n;
     }
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);    
    cin>>t;
    for(int i=1;i<=t;i++){
        init();
        doit();
        if(i==0){
                  cout<<r<<' '<<k<<' '<<n<<endl;
                  for(int j=1;j<=n;j++) cout<<a[i]<<' ';
                  cout<<endl;
        }
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
