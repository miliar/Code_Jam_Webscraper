#include<iostream>
#include<map>
#include<vector>
#include<cmath>
using namespace std;

int gcd(int a,int b)
{
  if(b==0) return a;
  else return gcd(b,a%b);
}

int main()
{
  int nt;
  cin>>nt;
  for(int cas=1;cas<=nt;cas++)
  {
     bool imposib=true;
     int n,l,h;
     cin>>n>>l>>h;
     vector<int> v;
     map<int,bool> m;
     map<int,bool> m2;
     int x;
     int ans;
     unsigned long long lcm=1;
     for(int i=0;i<n;i++)
     {
       cin>>x;
       v.push_back(x);
     }
     for(int i=l;i<=h;i++){
     int cnt=0;
      for(int j=0;j<v.size();j++)
        if(i%v[j]==0 || v[j]%i==0)
         cnt++;
        else break;
      if(cnt==v.size())
      {
        ans=i;
        imposib=false;
        break;
      }
     }

     cout<<"Case #"<<cas<<": ";
     if(imposib)
      cout<<"NO"<<endl;
     else
       cout<<ans<<endl;
  }
  return 0;
 
}
