#include<iostream>
#include<cstdlib>
using namespace std;
int main(void){
  int t,x,n,p,pos[2],now,cur,ans,count=1;
  char c;
  for(cin>>t;t>0;--t){
    cin>>n;
    pos[0]=1; pos[1]=1; now=0; cur=-1, ans=0;
    for(int i=0;i<n;++i){
      cin>>c>>p;
      x = (c=='B')?1:0;
      if(x==cur){
        ans+=abs(p-pos[x])+1;
        now+=abs(p-pos[x])+1;
        pos[x]=p;
        cur=x;
      }
      else{
        ans+=max(abs(p-pos[x])-now, 0)+1;
        now=max(abs(p-pos[x])-now, 0)+1;
        pos[x]=p;
        cur=x;
      }
    }
    cout<<"Case #"<<count++<<": "<<ans<<endl;
  }
  return 0;
}
