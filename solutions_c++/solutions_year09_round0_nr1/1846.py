#include<iostream>
#include<string.h>
#include<vector>
#include<map>
using namespace std;
string x;
int l,d,n,c=0;
vector<string>list;
vector<int>v;
int main()
{
freopen("al.in","r",stdin);    
freopen("al.out","w",stdout);    
cin>>l>>d>>n;
string temp;
for(int i=0;i<d;i++)
{
cin>>temp;
list.push_back(temp);
}
for(int k=0;k<n;k++)
{
cin>>x;
       int nv,p;
       for(int i=0;i<d;i++)
       {
       p=0;
       nv=0;
       for(int j=0;j<x.size();j++)
       {        
                if(x[j]=='(')
                {nv=2;}        
                else
                if(x[j]==')')
                {nv=0;}
                else
                if(nv==0)
                {
                if(x[j]==list[i][p])
                {p++;}
                }
                else
                if(nv==2)
                {if(x[j]==list[i][p])
                {p++;nv=1;}
                }
                else
                if(nv==1)
                {continue;}
       }        
       if(p==l)
       {c++;}
       }
v.push_back(c);
c=0;
}//in


for(int i=0;i<v.size();i++)
{cout<<"Case #"<<i+1<<": "<<v[i]<<endl;}
return 0;    
}
