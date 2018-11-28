#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;
int main()
{
int tc;
cin>>tc;
for(int i=0;i<tc;i++)
{
int n;
cin>>n;
string a[n];
double b[n][2];
for(int j=0;j<n;j++)
{
b[j][0]=0;
b[j][1]=0;
}
for(int j=0;j<n;j++)
{
cin>>a[j];
for(int k=0;k<n;k++)
{
if(a[j][k]=='0')
b[j][0]++;
else if(a[j][k]=='1')
b[j][1]++;
}
}
double wp[n];
for(int i1=0;i1<n;i1++)
{
wp[i1]=(b[i1][1])/(b[i1][1]+b[i1][0]);
}
double owp[n];
for(int y=0;y<n;y++)
{
double temp=0;
double div=0;
for(int x=0;x<n;x++)
{
if(a[y][x]=='.')
continue;
else if(a[y][x]=='1')
{div++;
temp=temp+(b[x][1]/(b[x][1]+b[x][0]-1));
}
else
{div++;
temp=temp+((b[x][1]-1)/(b[x][1]+b[x][0]-1));
}
}
temp=temp/div;
owp[y]=temp;
}
double oowp[n];
for(int j=0;j<n;j++)
{
double temp=0;
double div=0;
//for(int k=0;k<n;k++)
//{
//if(j==k)
//continue;
for(int v=0;v<n;v++)
{
//temp=temp+owp[k];
if(a[j][v]=='.')
continue;
else
{
div++;
temp=temp+owp[v];
}
//}
}
temp=temp/div;
oowp[j]=temp;
}
double rpi[n];
for(int p=0;p<n;p++)
{
//cout<<wp[p]<<" "<<owp[p]<<" "<<oowp[p]<<endl;
rpi[p]=(0.25*wp[p])+(0.50*owp[p])+(0.25*oowp[p]);
}
cout<<"Case #"<<i+1<<":"<<endl;
for(int u=0;u<n;u++)
{
cout<<rpi[u]<<endl;
}
}
return 0;
}

