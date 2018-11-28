#include<iostream>
#include<algorithm>
#include<climits>
using namespace std;
int main()
{
int T;
//cout<<INT_MAX<<endl;

cin>>T;
for(int cases=1;cases<=T;cases++)
{
int N,K,f=0,count=0;
cin>>N>>K;
string ret;
for(int i=0;i<N;i++)
{
if((K&1)==1) count++;
K>>=1;
}
//cout<<count<<" ....... "<<endl;
if(count==N)
ret="ON";
else ret="OFF";
cout<<"Case #"<<cases<<": "<<ret<<endl;
}

return 0;
}
