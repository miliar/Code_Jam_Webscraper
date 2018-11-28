#include<iostream.h>
#include<fstream.h>
#include<conio.h>

int inc(int i,int n)
{
  if(i==n-1)
  return 0;
  else
  return ++i;
}
int dec(int i,int n)
{
  if(i==0)
  return n-1;
  else
  return --i;
}

int main()
{
  long r,k,rounds,capacity,grp[1003],sum,in;
  int s,tests,t,i,j,n,start;
  
  ifstream ip("ip.txt");
  ofstream op("op.txt");
  ip>>tests;
  for(t=1;t<=tests;t++)
  {
    sum=0;
    ip>>rounds>>capacity>>n;
    for(i=0;i<n;i++)
    ip>>grp[i];
    i=0;
    for(r=1;r<=rounds;r++)
    {
      in=0;
      start=i;
      /*
for(j=i;j<n;j++)
 cout<<grp[j]<<" ";
 for(j=0;j<i;j++)
 cout<<grp[j]<<" ";
 cout<<" "<<in<<endl;
*/
      do
      {
        in+=grp[i];
        i=inc(i,n);
      }while (in<=capacity&&i!=start);
/*
for(j=i;j<n;j++)
 cout<<grp[j]<<" ";
 for(j=0;j<i;j++)
 cout<<grp[j]<<" ";
 cout<<" "<<in<<endl;
*/
      if(in>capacity)
      {
        i=dec(i,n);
        in-=grp[i];
      }
/* for(j=i;j<n;j++)
 cout<<grp[j]<<" ";
 for(j=0;j<i;j++)
 cout<<grp[j]<<" ";
 cout<<" "<<in<<endl;
*/
      sum+=in;
    }
    op<<"Case #"<<t<<": "<<sum<<endl;
  }
  getch();
  return 1;
}
