#include<iostream>
#include<stdio.h>
using namespace std;
FILE *in,*o;
int main()
{
 int t,a[500],n,s,p,i,j,x,y;
in=fopen("input.in","r");
    o=fopen("output.txt","w");
 //cin>>t;
 fscanf(in,"%d",&t);
 for(i=1;i<=t;i++)
 {
   fscanf(in,"%d%d%d",&n,&s,&p);
 // cin>>n>>s>>p;
  x=n;
  y=p;

  for(j=0;j<n;j++)
  {
   fscanf(in,"%d",&a[j]);
  }
  if(p==1)
   y=-1;

 for(j=0;j<n;j++)
 {
  if(a[j]<(p*3))
  {
   if(a[j]!=(3*p-2) && a[j]!=(3*p-1))
   {
    if(s==0)
     x--;

    else if(s!=0)
     if(a[j]!=(3*y-4) && a[j]!=(3*y-3))
      x--;
     else
      s--;
    }
  }
 }
 fprintf(o,"Case #%d: %d\n",i,x);
 //cout<<"Case #"<<i<<": "<<x<<"\n";
 }
}
