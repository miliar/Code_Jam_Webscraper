#include<iostream>
using namespace std;
main()
{
int fl,t,x,i,j,m,n;
cin>>t;
for(x=1;x<=t;x++)
{
fl=0;
cin>>m>>n;
char a[m][n+1];
for(i=0;i<m;i++)
cin>>a[i];
for(i=0;i<m;i++)
{
for(j=0;j<n;j++)
{
if((a[i][j]=='#')&&(i<(m-1))&&(j<(n-1)))
{
if((a[i][j+1]=='#')&&(a[i+1][j]=='#')&&(a[i+1][j+1]=='#'))
{a[i][j]='/';a[i+1][j+1]='/';
a[i+1][j]='\\';a[i][j+1]='\\';
}}
}}
for(i=0;i<m;i++)
for(j=0;j<n;j++)
if(a[i][j]=='#'){fl=1;break;}
cout<<"Case #"<<x<<":";
if(fl)cout<<"\nImpossible\n";
else
{
cout<<"\n";
for(i=0;i<m;i++)
cout<<a[i]<<"\n";
}
}
return 0;
}
