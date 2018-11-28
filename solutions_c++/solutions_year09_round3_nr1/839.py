#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <climits>

using namespace std;
main()
{
string s;
unsigned long long  int ans;
int i,j,k,l,t,a[50],b[50],f,cnt,final[100];
unsigned long long int arr[100];
cin>>t;
for(i=1;i<=t;i++)
 {
   cin>>s;
   
  j=0;
   while(s[j]==s[j+1]&& j<s.size()-1)
   {
      final[j]=1;

      j++;
   }
  final[j]=1;
  cnt=1;
  j++;
//cout<<j<<endl;
  while(s[j]==s[j+1])
   {
      final[j]=0;

      j++;
   }
  final[j]=0;
  j++;
// cout<<j<<" "<<endl; 
  cnt=2;
  while(j<s.size())
  {  
 int flag=0,index;
      for(k=0;k<j;k++)
       {
         if(s[j]==s[k])
         { flag=1;index=k; break;}
        }

      if(flag==0)
     { final[j]=cnt; cnt++;}
      else
      final[j]=final[index];
       
      j++;
   
  }

//cout<<"here"<<endl;
//for(k=0;k<s.size();k++)
//cout<<final[k]<<endl;

//cout<<"here"<<endl;
  int base;   
  if(cnt>2)
  base=cnt;
  else
  base=2;
ans=0;
arr[0]=1;
for(k=1;k<s.size();k++)
 arr[k]=arr[k-1]*base;
/*
cout<<"here1"<<endl;
for(k=0;k<s.size();k++)
cout<<arr[k]<<endl;
cout<<"here1"<<endl;
*/

for(k=0;k<s.size();k++)
 {
   ans=ans+arr[s.size()-k-1]*final[k];
//cout<<arr[s.size()-k-1]<<" "<<final[k]<<" "<<endl;
 }

cout<<"Case #"<<i<<":"<<" "<<ans<<endl;
 
 }
}
