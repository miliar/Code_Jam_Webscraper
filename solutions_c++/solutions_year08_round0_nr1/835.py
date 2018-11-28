#include<stdio.h>
#include<iostream>
#include<map>
#include<string>
using namespace std;
int main()
{
  int t,l=0;
  cin>>t;
  while(t--)
  {
      l++;
     map<string,int> m;
     map<string,int> ::iterator cu;
     string s;
     int k,n,i,q,ans=0,no=0,f=0;
     cin>>n;
     scanf("\n");
     for(i=0;i<n;i++)
     {
       getline(cin,s);
       m.insert(make_pair(s,0));
     }
     cu=m.begin();
     k=cu->second;
     s=cu->first;
    // cout<<endl<<k<<" "<<s<<endl;
     cin>>q;
     scanf("\n");
     while(q--)
     {
        getline(cin,s);
        cu=m.find(s);
        k=cu->second;
        if(k==f)
        {
           no++;
           cu->second=(cu->second+1)%2;
           if(no==n)
           {
              f=(f+1)%2;
              cu->second=(cu->second+1)%2;
              ans++;
              no=1;
           }
         }
      }
        
     cout<<"Case #"<<l<<": "<<ans<<endl;
     }
  
 }
