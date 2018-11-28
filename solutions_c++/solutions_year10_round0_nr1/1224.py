#include<iostream>
#include<cmath>
using namespace std;
int main()
{
long long t;
cin>>t;
long cases=0;
while(t--)
{
unsigned int N,K;
cin>>N;
cin>>K;

bool on=false;
if(K!=0)
{
if(!((K+1)%(unsigned int)pow(2.0,(double)N))) on=true;
//int one=K+1;
//int power=(int)pow(2.0,(double)N);
//cout<<one<<endl<<power<<endl;
}
if(on)
cout<<"Case #"<<++cases<<": ON"<<endl;
else
cout<<"Case #"<<++cases<<": OFF"<<endl;
}
return 0;
}