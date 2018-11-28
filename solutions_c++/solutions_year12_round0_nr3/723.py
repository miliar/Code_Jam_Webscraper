#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;
int main()
{
   // freopen("C-large.in","r",stdin);
  //  freopen("C-large.out","w",stdout);
   int T,A,B,m,n;
   int a[10],hash[100000];
   cin>>T;
   for(int i=1;i<=T;i++)
   {
       int cnt,count=0;
       cin>>A>>B;
       for(int j=A;j<=B;j++)
       {
           int temp=j;
           int sum=10;
           cnt=1;
           while(temp%sum!=temp)
           {
               a[cnt++]=temp%sum;
               sum*=10;
           }
           int cnt1=0;
           for(int k=1;k<cnt;k++)
           {
               int tmp=a[k]*(int)pow(10,cnt-k)+temp/(int)pow(10,k);
               if(tmp>=A&&tmp>temp&&tmp<=B)
                   {
                       int s;
                       for(s=0;s<cnt1;s++)
                       {
                           if(hash[s]==tmp)
                           break;
                       }
                       if(s==cnt1)
                       {
                           hash[cnt1++]=tmp;
                           count++;
                       }
                   }
           }
       }
       cout<<"Case #"<<i<<": "<<count<<endl;
   }
   return 0;
}
