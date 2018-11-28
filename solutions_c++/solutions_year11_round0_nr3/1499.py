#include<iostream>
#include<stdio.h>
#include<string>
#include<algorithm>
#include<cstring>
using namespace std;
int main()
{
   // freopen("C-small-attempt0.in","r",stdin);
    //freopen("ain.txt","r",stdin);
   // freopen("C-large.in","r",stdin);
  //freopen("A-ans.txt","w",stdout);
  int t,n,i,j,k,sum,cnt;
  int val[1100];
  bool flag;
  cin>>t;
  for(i=1;i<=t;i++)
  {
      cout<<"Case #"<<i<<": ";
      cin>>n;
      sum =0;
      for(j=0;j<n;j++)
      {
          cin>>val[j];
          sum+=val[j];
      }
      flag=true;
      sort(val,val+n);
      for(j=0;j<30;j++)
      {
          cnt=0;
          for(k=0;k<n;k++)
          {
              if(val[k] & (1<<j)) cnt++;
          }
          if(cnt%2)
          {
              flag=false;
              cout<<"NO"<<endl;
              break;
          }
      }
      if(flag) cout<<sum-val[0]<<endl;
  }
}
