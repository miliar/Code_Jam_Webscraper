#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
 int test;
 cin>>test;
 int c=0;
 while(test--)
 {
  c++;
  int i,n,s,p,val,ans=0;
  vector <int> v;
  cin>>n>>s>>p;
  for(i=0;i<n;i++)
  {
   cin>>val;
   if(val==0)
    continue;
   if(p*3 > val+2)
   {
    v.push_back(val);
   }
   else
    ans++;
  }

  for(i=0;i<v.size();i++)
  {
  if(s&&((v[i]) == (p*3)-3 || (v[i]) == (p*3)-4))
    {
     ans++;
     s--;
   }
  }
  
 cout<<"Case #"<<c<<": ";  
  if(p==0)
   cout<<n<<"\n";
  else
   cout<<ans<<"\n";
 }
 return 0;
}
