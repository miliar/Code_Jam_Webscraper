#include<iostream>
using namespace std;
long long int pos(long long int a)
{
if(a<0)return -a;
else return a;
}
int main()
{
long long int t;
cin>>t;
for(long long int ttt=1;ttt<=t;ttt++)
{
long long int n;
cin>>n;
long long int ans=0;
long long int O=1,OT=0,B=1,BT=0;
long long int T=0,num;
for(long long int i=0;i<n;i++)
{
char c;
cin>>c>>num;
if(c=='O')
{
long long int time=pos(num-O)+OT;
if(time<=T)
{
T++;
}
else
T=time+1;

OT=T;
O=num;
}
else
{
long long int time=pos(num-B)+BT;
if(time<=T)
{
T++;
}
else
T=time+1;

BT=T;
B=num;
}
//cout<<"B "<<B<<" BT "<<BT<<" O "<<O<<" OT "<<OT<<endl;
}
cout<<"Case #"<<ttt<<": "<<T<<endl;
}


}
