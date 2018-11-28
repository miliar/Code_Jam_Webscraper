#include<iostream>
#include<queue>
using namespace std;

int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
  int t,cas=1;
  cin>>t;
  while(t--){
      cout<<"Case #"<<cas++<<": ";       
       int r,k,n;
       cin>>r>>k>>n;
       queue<int> q;
       int a,sum=0;
       for(int i=0;i<n&&cin>>a;++i){
        sum+=a;
       q.push(a);
       }
       if(sum<=k)
       cout<<r*sum<<endl;
       else{
       int ans=0;
       for(int i=0;i<r;++i){
          int tmp=0;
          while(true){
            int v=q.front();
            if(tmp+v>k)
            break;    
            else{
              tmp+=v;
              q.pop();
              q.push(v);     
            }        
          }     
          ans+=tmp;
                  }
          cout<<ans<<endl;
          }
       }    
}
