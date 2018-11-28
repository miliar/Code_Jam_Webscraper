#include<iostream>

using namespace std;
typedef long long int L;
int main()
{
int T,uuuu;
cin>>T;
for(uuuu=1;uuuu<=T;uuuu++)
{
cout<<"Case #"<<uuuu<<": ";
L n;
cin>>n;
L *x=new L [n+1];
L *y=new L [n+1];

for(L i=0;i< n;i++)
cin >> x[i] >> y[i];

for(L i=0;i< n;i++)
{
for( L j=0 ; j < n-1 ; j++)
{
if(x[j] > x[j+1])
{
L temp = x[j];
x[j] =x[j+1];
x[j+1] = temp;

temp = y[j];
y[j] = y [j+1];
y[j+1] = temp;
}

}
}
//for ( L i=0 ; i < n  ; i++)
//cout<<x[i]<<" " <<y[i]<<endl;

L count =0;
for(L i=0;i<n;i++)
{
for(L j=i-1;j>=0;j--)
if(y[i]<y[j]) count++;
}

cout<<count<<endl;

}
}

