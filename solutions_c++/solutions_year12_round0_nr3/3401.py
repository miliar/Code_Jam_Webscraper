#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
using namespace std;
int A[2000001],a,b;
long long int cnt;
void find(int x)
{
       if(x<10)
       return;
       int temp,dig=0,rec_no=0;
       temp=x;
       while(temp>0)
       {
               ++dig;
               temp/=10;
       }
       --dig;
       int k=pow(10,dig);
       for(int i=0,j=10;i<dig;i++,j*=10,k/=10)
       {
               rec_no=((x%j)*k)+(x/j);
               if(rec_no>=a&&rec_no<=b&&rec_no!=x)
               {
                 A[rec_no]++;
               }
       }
}

int main()
{
   freopen("3.txt","r",(stdin));
   freopen("output.txt","w",(stdout));
       int t,no=0;
       scanf("%d ",&t);

       while(t--)
       {
               no++;
               for(int i=0;i<1001;i++)
               A[i]=0;
               cnt=0;
               scanf("%d%d",&a,&b);
               for(int i=a;i<=b;i++)
               {
                       find(i);
               }
               for(int i=a;i<=b;i++)
               {
                       cnt+=A[i];
               }
               printf("Case #%d: %lld\n",no,(cnt/2));
       }
return 0;
}
