#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<queue>
#include<map>
using namespace std;
typedef long long int int64;
int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int64 i,j,n,k,m,t,cnt=1;
cin>>t;
char a[1000],ref[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
while(t--)
{
scanf(" %[^\n]s",a);
cout<<"Case #"<<cnt<<": ";
for(i=0;i<strlen(a);i++)if(a[i]!=' ')cout<<(char)(ref[a[i]-97]);else cout<<a[i];
cout<<endl;
cnt++;
}
return 0;
}
