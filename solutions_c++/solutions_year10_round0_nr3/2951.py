#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<bitset>


using namespace std;

long long unsigned int t,n,k,r,a[1000],sum[1000],to[1000],ans;


int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   
   cin>>t;
   for(int prob=0;prob<t;prob++)
   {
           cin>>r>>k>>n;
           for(int i=0;i<n;i++)
           cin>>a[i];
           int j=0;
           ans=0;
           long long unsigned int temp=0;
           for(int i=0;i<n;i++)
           {
                   int ij=j,done=1;
                   while(temp+a[j]<=k && (ij!=j || done==1))
                   {
                       done=0;
                       temp+=a[j];
                       j=(j+1)%n;
                   }
                   sum[i]=temp;
                   temp-=a[i];
                   to[i]=j;
           }
           
           
           j=0;
           for(int i=0;i<r;i++)
           {
                   ans+=sum[j];
                   j=to[j];
           }
           printf("Case #%d: %d\n",prob+1,ans);
   }
                   

   //system("pause");
   return 0;

}
