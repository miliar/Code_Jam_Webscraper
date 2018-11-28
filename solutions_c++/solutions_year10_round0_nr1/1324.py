#include<iostream>
#include<vector>


using namespace std;

int n,k;

bool init(){

  int two=1;
  cin>>n>>k;

  for(int i=0;i<n;i++)
  {
  two*=2;
  }
  
  k%=two;   
  for(int i=0;i<n;i++)
  if((k&(1<<i))==0) return false;

  return true;
}

int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);

int t; cin>>t;


for(int i=1;i<=t;i++)
{cout<<"Case #"<<i<<": ";

  if(init()) cout<<"ON";
  else cout<<"OFF";
  
  cout<<endl;
}


return 0;}