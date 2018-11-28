#include<iostream>
#include <sstream>
#include <string>
using namespace std;

string i2string(int i) {
ostringstream buffer;
 buffer << i;
 return buffer.str();
}



int main()
{
int t,n1,n2; cin>>t;
int ctr=0;

for(int i=0;i<t;i++)
{
cin>>n1>>n2;
//cout<<" "<<n1<<" "<<n2<<endl;
ctr=0;
if(n1==n2)
{cout<<"Case #"<<i+1<<": "<<"0"<<endl; continue; }

if(n1<10 && n2<10)
{cout<<"Case #"<<i+1<<": "<<"0"<<endl; continue; }

for(int j=n1;j<=n2;j++)
{

string s1=i2string(j);
for(int k=j+1;k<=n2;k++)
{
string s2=i2string(k);
s2=s2+s2;
//cout<<s2;
if(s2.find(s1)!=string::npos)
ctr++;
}//inner most for



}//middle for


cout<<"Case #"<<i+1<<": "<<ctr<<endl;


}//outer for









return 0;
}

