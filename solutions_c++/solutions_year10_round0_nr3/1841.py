#include<iostream>
#include<vector>
#include<cstring>

using namespace std;
int r,n,k,a[1111];
vector<int> v;
vector<long long>g;
void findp(){
    int st=0,c[n]; memset(c,0,sizeof(c));
    c[st]=1; v.clear(); g.clear(); v.push_back(0); g.push_back(0LL);
    while(true){
      long long sum=0;
      int temp=st;
      while( sum+a[st] <= k ){ sum+=a[st]; st=(st+1)%n; if( st==temp ) break;}
      g.push_back(sum);
      v.push_back(st);
      if( c[st] ) return ;
      c[st]=1;
    }
}
int main(){   
    freopen("Download A-small.in","r",stdin);  freopen("outut.txt","w",stdout);
    
    
    int t,Case=1;scanf("%d",&t);
    while(t--){
      scanf("%d %d %d",&r,&k,&n);
      for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
      
      findp(); long long psum=0;
    //  for(int i=0;i<v.size();i++) cout<<v[i]<<" "; cout<<endl;
     // for(int i=0;i<v.size();i++) cout<<g[i]<<" "; cout<<endl;
      int ps=0,pe=v.size()-1;
      
      while( v[ps]!=v[pe] ) ps++;
      for(int i=ps;i<pe;i++) psum+=g[1+i]; 
      
     // cout<<ps<<" ;; "<<pe<<" "<<psum<<endl;  
       
      long long sum=0;
      for(int i=0;i<min(ps,r);i++) sum+=g[1+i];
      //cout<<sum<<endl;
      if( r > ps ){
         r-=ps;
         int d=pe-ps;
         sum+=psum*(r/d);/// cout<<sum<<endl;
         if( sum<0 ) cout<<"er"<<endl;
         for(int i=0;i<(r%d);i++) sum+=g[ps+i+1];
      }  
      printf("Case #%d: ",Case);  
      cout<<sum<<endl;
      
      
      Case++; //cout<<endl;
    }
    //while(3);  
}
