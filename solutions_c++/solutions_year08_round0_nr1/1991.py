#include<iostream>
#include<vector>
#include<string>
#include<map>
using namespace std;
int main()
{
 int t,x=0;
 cin>>t;
 fflush(stdin);
 while(t--)
 {
  int min=0,n,q,count=0;
  string cur;
  cin>>n;
  fflush(stdin);
  x++;
  vector<string>v(n);
  for(int i=0;i<n;i++)
  getline(cin,v[i]);
  cin>>q;
  vector<string> s(q);
  fflush(stdin);
  for(int i=0;i<q;i++)
  getline(cin,s[i]);
  vector<bool>flag(n,false);
  for(int i=0;i<q;i++)
  {
   bool found;
   for(int j=0;j<n;j++)
   if(v[j]==s[i])
   {
    flag[j]=true;
    break;
    } 
   found=true;
   for(int j=0;j<n;j++)
   {
    if(!flag[j])
    {
     found=false;
     break;
     }
    }
   if(found)
   {
    for(int j=0;j<n;j++)
    flag[j]=false;
    min++;
    for(int j=0;j<n;j++)
    if(v[j]==s[i])
    {
     flag[j]=true;
     break;
     }
    }
   }
  cout<<"Case #"<<x<<": "<<min<<endl;
  }
 return 0;
 }
