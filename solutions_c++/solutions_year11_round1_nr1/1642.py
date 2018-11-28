#include<iostream>
#include<cmath>
using namespace std;
int main()
{
int tc;
cin>>tc;
for(int h=0;h<tc;h++)
{
double n,pd,pg;
cin>>n>>pd>>pg;
double i=1;
for(i=1;i<=n;i++)
{
int bit=0;
double y=1;

for(y=0;y<=i;y++)
{
double today=(y/i)*100;
//cout<<y<<" "<<i<<endl;
//cout<<today<<endl;
//cout<<today<<endl;
if(today==pd)
{
//double total=(
//cout<<total<<endl;
//double lost=i-y;
//double total=(lost/(100-pg))*100;
if((pg==100 && pd==100) || (pg==0 && pd==0) || (pg!=100 && pg!=0))
{
//cout<<total<<" "<<today<<" "<<i<<endl;
bit=1;
cout<<"Case #"<<h+1<<": Possible"<<endl;
break;
}
}
}


if(bit==1)
break;
}
if(i==n+1)
cout<<"Case #"<<h+1<<": Broken"<<endl;
}
return 0;
}
