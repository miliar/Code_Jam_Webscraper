#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int n,i,j;
string s;
char c[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
cin>>n;
getline(cin,s);
for(i=1;i<=n;i++)
{
getline(cin,s);
cout<<"Case #"<<i<<": ";
for(j=0;j<s.length();j++)
{
if(s[j]!=' ') cout<<c[s[j]-'a'];
else cout<<' ';
}
cout<<endl;
}
return 0;
}