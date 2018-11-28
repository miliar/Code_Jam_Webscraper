#include<iostream>
#include<fstream>
using namespace std;
int main()
{
 long long t,n,i,cnt;
 long long k,j;
 int a[50],f;
 fstream in("input.txt");
 fstream b("output.txt");
 in>>t;
 for(i=0;i<t;i++)
 {
  in>>n;
  in>>k;
  for(j=0;j<n;j++)
   a[j]=0;
  a[0]=1;
  f=0;
  for(j=0;j<k;j++)
  {
   for(cnt=0;cnt<n;cnt++)
   {
    if(a[cnt]==1)
    {
     a[cnt]=2;
     break;
    }
    else if(a[cnt]==2 && cnt==0)
     a[cnt]=1;
    else if(a[cnt]==1)
     a[cnt]=2;
    else if(a[cnt]==2)
    {
     a[cnt]=0;
    }
   } 
   f=0;
   for(cnt=0;cnt<n;cnt++)
   {
    if(a[cnt]==0)
    {
     f=1;
     break;
    }
    else if(a[cnt]==1)
    {
     f=0;
     break;
    }
   }
   if(f==1)
    a[cnt]=1;
  }
 f=1;
 for(cnt=0;cnt<n;cnt++)
 {
  if(a[cnt]!=2)
   f=0;
 }
 if(f==1)
  b<<"Case #"<<i+1<<": ON"<<endl;
 else 
  b<<"Case #"<<i+1<<": OFF"<<endl;
}
 in.close();
 b.close();
 return 0;
}
