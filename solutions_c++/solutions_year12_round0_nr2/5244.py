#include<string.h>
//#include<conio.h>
#include<fstream.h>
fstream f("date.in", ios::in);
fstream g("date.out", ios::out);
int main()
{ int nrr;
f>>nrr;
for(int k=1;k<=nrr;k++)
{
int n,s,m,v[100],i;
f>>n>>s>>m;
for(i=1;i<=n;i++)
f>>v[i];
int nr=0;
int min_s=m+m-2+m-2;
int min=m+m-1+m-1;
int surp;
int s2=s;
for(i=1;i<=n;i++)
{

if(v[i]>=0&&m==0)
  nr++;
  else if(m==1&&v[i]>=1)   nr++;
  else  if(v[i]>=min&&min>=0)
  nr++;
  else
  if(v[i]>=min_s&&s2>0&&min_s>0)
  {nr++; s2--;}



}
g<<"Case #"<<k<<": "<<nr<<"\n";
}




return 0;
}