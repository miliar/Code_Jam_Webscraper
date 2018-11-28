#include<iostream>
#include<fstream>
using namespace std;
int main()
{
 int t;
 long long r,k,euro=0,cnt=0,sum=0;
 long n,i,j,h;
 long long g[100000],temp[100000];
 fstream a("input.txt");
 fstream b("output.txt",ios::out);
 a>>t;
 for(i=0;i<t;i++)
 {
  a>>r;
  a>>k;
  a>>n;
  euro=0;
 cnt=0;
 sum=0;
  for(j=0;j<n;j++)
  {
   a>>g[j];
  }
  for(j=0;j<r;j++)
  {
   cnt=0;
   sum=0;
   while(sum<=k)
   {
    sum=sum+g[cnt];
    if(sum>k || cnt==n-1)
    {
     if(sum>k)
     euro+=(sum-g[cnt]);
     else
     euro+=sum;
     for(h=0;h<cnt;h++)
      temp[h]=g[h];
     for(h=cnt;h<n;h++)
     {
       g[h-cnt]=g[h];
     }
     for(h=0;h<cnt;h++)
     {
      g[n-cnt+h]=temp[h];
     }
     break;
    }
    cnt++;
   }
  }

  b<<"Case #"<<i+1<<": "<<euro<<endl;
 }
 a.close();
 b.close();
 return 0;
}
