#include<iostream>
using namespace std;
int main()
{
int a;
cin>>a;
long long n,k,count;
count=1;
while(a--)
{
cin>>n>>k;
long long z=k+1;
while(n)
{
if(z%2==0)
z=z/2;
else
break;
n--;
}
if(n==0)
cout<<"Case #"<<count<<": ON"<<endl;
else
cout<<"Case #"<<count<<": OFF"<<endl;
count++;
}
return 0;
}
