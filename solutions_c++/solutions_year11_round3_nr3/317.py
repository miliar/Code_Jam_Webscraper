#include<iostream>
#include<vector>
using namespace std;
vector<int>data;
int N,L,H,T;
int temp;
int ans;
int main()
{

bool find;
cin>>T;
for(int q=0;q<T;q++)
{
  cin>>N>>L>>H;
  for(int i=0;i<N;i++)
  { 
    cin>>temp;
    data.push_back(temp);
  }
  
  for(int i=L;i<=H;i++)
  {
  find=false;
   for(int j=0;j<data.size();j++)
    {
     temp=data.at(j);
      if(i>=temp && i%temp==0) 
       find=true;
      else if(i<=temp && temp%i==0)
       find=true;
      else
      {find=false;
       break;
      }
    } 
    if(find)
    {
     ans=i;
     break;
    }
  }
  
cout<<"Case #"<<q+1<<": ";
if(find)
 cout<<ans<<endl;
else
 cout<<"NO"<<endl;

data.clear();
}

return 0;
}
