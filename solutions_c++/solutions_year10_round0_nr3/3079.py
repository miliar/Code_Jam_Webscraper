#include<iostream>
#include<queue>
using namespace std;

int main()
{
 int n1;
 cin>>n1;
 int r,k,n;
 int z;
 queue<int> x,y;
 for(int j=1;j<=n1;j++){
  while(x.size()) x.pop();
 cin>>r>>k>>n;
  for(int i=1;i<=n;i++)
  { cin>>z;
    x.push(z);
  }
  int total=0,temp;
  while(r--){
    temp=0;
    while((temp+x.front())<=k && x.size()){
      int a=x.front();
      temp+=a;
      x.pop();
      y.push(a);
    }
   total+=temp;
   while(y.size())
   {
      int a=y.front();
      x.push(a);
      y.pop();
   }
  }
   cout<<"Case #"<<j<<": "<<total<<endl;
 }
 return 1;
}
