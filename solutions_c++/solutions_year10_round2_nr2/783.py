#include<iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

typedef long long int L;

int main()
{
int t,T;
cin>>T;
for(t=1;t<=T;t++)
{
L n,k,b,c;
cin>>n>>k>>b>>c;
L *d = new L [n+1];
L *v= new L [n+1];
for(L i=0;i<n;i++)
cin>>d[i];
double *ti= new double[n+1];
for(L i=0;i<n;i++)
{ cin>>v[i];
if(v[i]==0)
ti[i]=-1;
else
ti[i]=1.0*(1.0*(b-d[i]))/(1.0*v[i]);
}
double *time= new double[n+1];

for(L i=0;i<n;i++)
{
time[n-i-1]=ti[i];
}
L swap=0;
L count=0,initial=-1;
L lc=0;
if(k!=0)
{
for(L i=0;i<n;i++)
{
if(time[i] <= 1.0*c && time[i] >=  0.0 )
{
count++;
//if(count>1)
//swap+=swap+(i-initial-1);
//else 
swap+=lc+(i-initial-1);
lc=lc+(i-initial-1);
initial=i;
}
if(count==k)break;
}
}

if(k==count)
cout<<"Case #"<<t<<": "<<swap<<endl;
else
cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;


}

}
