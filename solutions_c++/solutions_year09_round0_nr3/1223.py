#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <deque>
using namespace std;

string f="welcome to code jam";

void ncase(int x)
{
 string s;
 getline(cin,s);
 int a[24][500];
 for(int i=0;i<f.size();i++)
  for(int j=0;j<s.size();j++)
  a[i][j]=0;
 for(int i=0;i<f.size();i++)
  for(int j=0;j<s.size();j++)
   if(f[i]==s[j])a[i][j]=1;
   else a[i][j]=0;
   

 for(int i=f.size()-2;i>=0;i--)
   for(int j=0;j<s.size();j++)
    if(a[i][j]!=0)
    {int t=0;
     for(int k=j+1;k<s.size();k++)
      t=(t+a[i+1][k])%10000;
     a[i][j]=t;
    }
 
 /*for(int i=0;i<f.size();i++)
  {for(int j=0;j<s.size();j++)
    cout<<a[i][j]<<" ";
   cout<<endl;
   }*/
 
 int sol=0;
 for(int i=0;i<s.size();i++)
  sol=(sol+a[0][i])%10000;
 cout<<"Case #"<<x<<": ";
 if(sol<1000)cout<<"0";
 if(sol<100)cout<<"0";
 if(sol<10)cout<<"0";
 cout<<sol<<endl;                    
}

int main()
{
    int n;
    cin>>n;
    cin.ignore(256,'\n');
    for(int i=0;i<n;i++)
     ncase(i+1);
     return 0;
     
}
