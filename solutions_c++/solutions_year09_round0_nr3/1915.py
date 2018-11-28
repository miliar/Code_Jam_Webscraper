#include<iostream>
#include<stdio.h>
#include<string.h>
#include<vector>
#include<sstream>
#include<algorithm>
using namespace std;
string x,w="welcome to code jam";
int c=0;
void func(int pos,int l)
{
if(l==w.size())
{c++;return;}
if(pos==x.size())
{return;}

if(x[pos]==w[l])
{func(pos+1,l+1);}
func(pos+1,l);
return;
}
int main()
{
freopen("wj.in","r",stdin);
freopen("wj.out","w",stdout);
vector<string>ans;
int n;
   cin>>n;
for(int i=0;i<n;i++)
{
    string xy,xz;
    cin>>xy;
    getline(cin,xz);
    x=xy+xz;
    c=0;
    func(0,0);
    stringstream ss;
    string tt="",xx;
    ss<<c;
    ss>>xx;
    if(xx.size()>3)
    {
    for(int j=xx.size()-4;j<xx.size();j++)
    {    
    tt+=xx[j];
    }
    }
    else
    {
    for(int i=0;i<4-xx.size();i++)
    {tt+='0';}
    tt+=xx;
    }
    ans.push_back(tt);
    }
    
for(int i=0;i<ans.size();i++)
{cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;}
return 0;    
}
