#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))
int main(){
   // ifstream cin("C-small-attempt0.in");
  //  ofstream cout("C-small-attempt0.out");
    int t;
    cin>>t;
    
    int cas=1;
    while(t--){
     int n;cin>>n;
     int sum=0,z=0,mv=99999999;
     for(int i=0;i<n;++i){
     int v;
     cin>>v;
     sum+=v;
     z^=v;
     mv=min(mv,v);
     }
     cout<<"Case #"<<cas++<<": ";
     if(z==0)
     cout<<sum-mv<<endl;
     else
     cout<<"NO"<<endl;          
   }
    
    
}
