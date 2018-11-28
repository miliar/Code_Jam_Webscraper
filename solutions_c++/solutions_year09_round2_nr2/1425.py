#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<stack>
#include<queue>
#include<cstdlib>
using namespace std;
int don(vector<int> now)
  {
  int ret=0;
  vector<int> dig;
  for(int i=1;i<10;i++)
    while(now[i])
      {dig.push_back(i);now[i]--;}
  while(now[0])
    {
    ret++;
    now[0]--;
    }
  ret++;
  int ans;
  ans=dig[0];
  for(int i=0;i<ret;i++)
    ans*=10;
  for(int i=1;i<dig.size();i++)
    ans=ans*10+dig[i];
  return ans;
  }
  
  int cntdig(int n)
    {
    int ans=0;
    while(n>0)
      {n/=10;ans++;}
     return ans;
     }
int main()
{
int hum=1;
int t;
cin >>t;

while(t--)
  {
  int n;
  cin >>n;
  vector<int> dig;
  for(int i=0;i<10;i++)
    dig.push_back(0);
  int temp=n;
  int num=0;
  while(temp>0)
   {
   dig[temp%10]++;
   temp/=10;
   num++;
   }
  
  n++;
  while(1)
    {
   // cout<<n<<"\n";;
    int p=cntdig(n);
    if(p>num){n=don(dig);break;}
     vector<int> h;
    for(int i=0;i<10;i++)
       h.push_back(0);
    temp=n;
    while(temp>0)
      {
      h[temp%10]++;
      temp/=10;
      }
    if(h==dig)break;
    n++;
    }
  cout<<"Case #"<<hum++ <<": "<<n<<"\n";
  }
return 0;
}
