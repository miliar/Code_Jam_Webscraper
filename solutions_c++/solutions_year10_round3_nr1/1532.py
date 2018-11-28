#include<iostream.h>
#include<stdio.h>
void main()
{
 long int t,c=0,k,j,x,y,i,n,a[10000],b[10000];
 cin>>t;
 for(i=0;i<t;i++)
  {  cin>>n;
   for(j=0;j<n;j++)
   { cin>>a[j];cin>>b[j];
    }
    x=a[0];y=b[0];c=0;
    for(k=1;k<n;k++)
   {  if(a[k]>x && b[k]>y) {continue;}
      if(a[k]<x && b[k]<y) {continue;}
      c++;
   }
   cout<<"Case #"<<i+1<<": "<<c<<endl;
 }
 }