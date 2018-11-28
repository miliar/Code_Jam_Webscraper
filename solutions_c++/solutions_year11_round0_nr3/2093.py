#include <iostream>
#include <fstream>

using namespace std;

//#define SMALL
#define LARGE

bool allzero(int *a,int n)
{
  for (int i=0; i<n; i++)
    if(a[i]>0)
      return false;
  return true;
}

int main()
{
#ifdef SMALL
  ifstream datain("C-small-attempt0.in");
  ofstream dataout("C-small-attempt0.out");
#endif
#ifdef LARGE
  ifstream datain("C-large.in");
  ofstream dataout("C-large.out");
#endif
  int a[1010];
  int t,n;
  datain>>t;
  for (int i=1; i<=t; i++)
  {
    int sum=0;
    int min=0x7fffffff;
    datain>>n;
    for (int j=0; j<n; j++)
    {
      datain>>a[j];
      sum+=a[j];
      if(a[j]<min)
        min=a[j];
    }
    bool flag=true;
    while(!allzero(a,n))
    {
      int one=0;
      for(int j=0; j<n; j++)
      {
        if(a[j]!=0)
          if(a[j]%2==1)
          {
            one++;
          }
        a[j]>>=1;
      }
      if(one%2==1)
      {
        flag=false;
        break;
      }
    }
    if(!flag)
    {
      dataout<<"Case #"<<i<<": NO"<<endl;
      continue;
    }
    dataout<<"Case #"<<i<<": "<<sum-min<<endl;
  }
}
