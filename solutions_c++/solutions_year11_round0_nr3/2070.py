#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
long long int test;
cin>>test;
long long int num[10000];
for(long long int ttt=1;ttt<=test;ttt++)
{
cout<<"Case #"<<ttt<<": ";
long long int n;
cin>>n;
for(long long int i=0;i<n;i++)
cin>>num[i];

sort(num,num+n);
long long int x=num[n-1];
long long int sum=num[n-1];
for(long long int i=n-2;i>0;i--)
{
x=x^num[i];
sum+=num[i];
}
if(x==num[0])
cout<<sum<<endl;
else
cout<<"NO"<<endl;
}

}
