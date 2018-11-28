#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
using namespace std;

int main()
{

string s;
int t,cas=0;
cin>>t;
while(t--)
{cas++;
cin>>s;
map<char,int>mp;
int i,l,k=0;
l=s.size();
bool bg=true;
mp[s[0]]=1;
k=2;
char c=s[0];
for(i=1;i<l;i++)
{	
  if(s[i]==c)continue;
  if(bg){mp[s[i]]=0;bg=false;}
  else if(mp.count(s[i])>0)	continue;
  else			mp[s[i]]=k++;
}


int bs;
bs=mp.size();
bs=max(bs,2);
long long int ans=0,m=1;
for(i=l-1;i>=0;i--)
{
   ans+=mp[s[i]]*m;
   m*=bs;
}
cout<<"Case #"<<cas<<": ";
cout<<ans<<endl;
}

}