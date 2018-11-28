#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
 int t;
 cin>>t;
 int cases=0;
 while(t--&&++cases)
 {
  int i,n,s,p,temp,sum=0;
  vector <int> v1;
  cin>>n>>s>>p;
  for(i=0;i<n;i++)
  {
   cin>>temp;
   if(temp==0)
    continue;
   if(p*3 > temp+2 )
   {
    v1.push_back(temp);
   }
   else
    sum++;
  }
  for(i=0;i<v1.size();i++)
  {
  if(s&&((v1[i]) == (p*3)-3 || (v1[i]) == (p*3)-4))
    {
     sum++;
     s--;
   }
  }
  
 cout<<"Case #"<<cases<<": ";  
  if(p==0)
   cout<<n<<"\n";
   else
   cout<<sum<<"\n";
 }
 return 0;
}
