#include<iostream>
#define INF 2000000000
using namespace std;
int main(void){
  int count=1;
  int t,n,min,now,x,sum;
  for(cin>>t;t>0;--t){
    now=0, min=INF, sum=0;
    cin>>n;
    for(int i=0;i<n;++i){
      cin>>x;
      if(x<min) min=x;
      sum+=x;
      now^=x;
    }
    cout<<"Case #"<<count++<<": ";
    if(now!=0)
      cout<<"NO"<<endl;
    else
      cout<<sum-min<<endl;
  }
  return 0;
}
