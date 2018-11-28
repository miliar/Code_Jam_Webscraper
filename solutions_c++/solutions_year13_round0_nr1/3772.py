#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int x[2][5],y[2][5],d1[2],d2[2],i,j,l=0,t,n;
char c;
cin>>n;
for(t=1;t<=n;t++)
{
for(j=0;j<2;j++) for(i=1;i<=4;i++) x[j][i]=y[j][i]=d1[j]=d2[j]=0;
l=0;
for(i=1;i<=4;i++)
{
for(j=1;j<=4;j++)
{
cin>>c;
if(c!='.') l++;
if(c=='X' || c=='T')
{
x[0][i]++;
y[0][j]++;
if(i+j==5) d1[0]++;
if(i==j) d2[0]++;
}
if(c=='O' || c=='T')
{
x[1][i]++;
y[1][j]++;
if(i+j==5) d1[1]++;
if(i==j) d2[1]++;
}
}
}
cout<<"Case #"<<t<<": ";
for(i=1;i<=4;i++)
{
if(x[0][i]==4 || y[0][i]==4 || d1[0]==4 || d2[0]==4)
{
cout<<"X won";
break;
}
if(x[1][i]==4 || y[1][i]==4 || d1[1]==4 || d2[1]==4)
{
cout<<"O won";
break;
}
}
if(i>4) cout<<(l==16?"Draw":"Game has not completed");
cout<<endl;
}
return 0;
}