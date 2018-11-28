#include <iostream>
#include <cstring>
#include <cmath>
#define N 1100
  using namespace std;
  long long a[N],t[N],c[N];
  long long n,m,r,ans;
  long long hav[N];
  long long sum;
int main(){
  freopen("c.in","r",stdin);freopen("c.out","w",stdout);
  int i,j,k,x,y,test;
  long long tim,num;
  scanf("%d\n",&test);
  for(int tt=1;tt<=test;tt++){
    printf("Case #%d: ",tt);
    cin>>r>>m>>n;
    sum=0;
    for(i=0;i<n;i++){
      cin>>a[i];
      sum=sum+a[i];
      };
    if(sum<=m){
      ans=sum*r;
      cout<<ans<<endl;
      continue;
      };    
    ans=0;
    memset(hav,false,sizeof(hav));
    x=0;i=0;
    hav[0]=true;c[0]=t[0]=0;
    while(true){
      x++;
      if(x>r)break;
      y=0;
      while(y+a[i]<=m){
        y+=a[i];
        i=(i+1)%n;
        };
      ans=ans+y;
      if(hav[i]){ 
        tim=x-c[i];
        num=ans-t[i];
        ans=ans+(r-x)/tim * num;
        x=(r-x)%tim;
        while(x--){
          y=0;
          while(y+a[i]<=m){
            y+=a[i];
            i=(i+1)%n;
            };
          ans=ans+y;
          };
        break;
        }
      else{
        c[i]=x;
        t[i]=ans;
        hav[i]=true;
        };
      };
    cout<<ans<<endl;
    };
}
      
        
      
      
      
      
    
    
    
    
  
