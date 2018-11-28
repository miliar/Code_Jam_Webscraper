#include<vector>
#include<fstream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<functional>
#include<iostream>
#include<cstring>
using namespace std;
int main()
{
int t;
freopen("A-large.in.txt","r",stdin);
   freopen("A-small-attempt0.in.out","w",stdout);
     
cin>>t;
for(int tt=1;tt<=t;tt++)
{
long long n,k,p=1,l;
cin>>n>>k;
for(int q=0;q<n;q++)
p*=2;k++;
if(k%p==0)
cout<<"Case #"<<tt<<": ON"<<endl;
else
cout<<"Case #"<<tt<<": OFF"<<endl;
}
return 0;
};