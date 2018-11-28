#include<iostream>
#include<cstdio>
using namespace std;
main()
{
int t,x,n,i,j;
cin>>t;
for(x=1;x<=t;x++)
{
cin>>n;
char a[n][n+1];
long double wp[n],owp[n],oowp[n],swp[n],rpi[n];
int count[n],wc[n];
for(i=0;i<n;i++)
scanf("%s",a[i]);
//cout<<a[i];}
for(i=0;i<n;i++)
{count[i]=0;wc[i]=0;
for(j=0;j<n;j++)
{
if(a[i][j]!='.') count[i]++;
if(a[i][j]=='1') wc[i]++;
}
//cout<<i<<" "<<wc[i]<<" "<<count[i]<<" ";
wp[i]=(double)(long)wc[i]/count[i];
//cout<<wp[i]<<"\n";
}
for(i=0;i<n;i++)
{swp[i]=0.0;
for(j=0;j<n;j++)
{
if((a[i][j]!='.')&&(a[j][i]=='0'))swp[i]+=(double)wc[j]/(count[j]-1);
else if(a[j][i]=='1'){swp[i]+=(double)(wc[j]-1)/(count[j]-1);}
}
owp[i]=swp[i]/count[i];
//cout<<owp[i]<<"\n";
}
for(i=0;i<n;i++)
{swp[i]=0;
for(j=0;j<n;j++)
{
if(a[i][j]!='.')swp[i]+=owp[j];
}
oowp[i]=swp[i]/count[i];
//cout<<oowp[i]<<"\n";
}
for(i=0;i<n;i++)rpi[i]=(0.25*wp[i])+(0.50*owp[i])+(0.25*oowp[i]);
cout<<"Case #"<<x<<":\n";
for(i=0;i<n;i++)printf("%.7Lf\n",rpi[i]);
}
return 0;
}
