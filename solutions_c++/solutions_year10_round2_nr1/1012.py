#include<iostream>
#include<vector>
#include<map>
#include<cmath>
#include<stdio.h>
#include<algorithm>
#include<string>
#include<stack>
#include<queue>

using namespace std;

int main()
{
     int t,i,j,n,m,c,q,l;
     cin>>t;
     map<string,int> map1;
     map<string,string> map2;
     string s,curr;
     for(i=1;i<=t;i++)
     {
          cin>>n>>m;
          c=0;
          map1.clear();
          map2.clear();
          for(j=0;j<n;j++)
          {
               cin>>s;
               q=0;
               l=0;
               curr="";
               while(q<=s.size())
               {
                    if(s[q]=='/' || q==s.size())
                    {
                         if(curr.size()>0) 
                         {
                              map1[curr]=l;
                              map2[curr]=s.substr(0);
                              //cout<<"hello "<<curr<<" "<<j<<" ";
                         }
                         l++;
                         //curr="";
                    }
                    else
                    {
                         curr+=s[q];
                    }
                    q++;
               }
          }
          for(j=0;j<m;j++)
          {
               cin>>s;
               q=0;
               l=0;
               curr="";
               while(q<=s.size())
               {
                    if(s[q]=='/' || q==s.size())
                    {
                         if(curr.size()>0 && map2[curr]!=s.substr(0) && map1[curr]==0)
                         {
                              map1[curr]=l;
                              map2[curr]=s.substr(0);
                              c++;
                              //cout<<map2[curr]<<" ";
                         }
                         l++;
                         //curr="";
                    }
                    else
                    {
                         curr+=s[q];
                    }
                    q++;
               }
          }
          cout<<"Case #"<<i<<": ";
          cout<<c;
          cout<<"\n";
     }
     //system("pause");
     return 0;
}
