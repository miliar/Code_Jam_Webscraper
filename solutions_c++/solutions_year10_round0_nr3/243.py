/*      
 *      Author: Lokesh Agarwal
 */

#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<iomanip>
#include<vector>
#include<list>
#include<set>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define MM 6110
#define min1(p,q) (p>q?q:p)
#define max1(p,q) (p>q?p:q)
int main()
{freopen("C-large.in","rt",stdin);
	freopen("C.txt","wt",stdout);
    int t,v,c,cnt,in,ae=0;
    long r,inr,p,n,k,mm,nn;
    long a[1005];
    int b[1005];
    long long s[1005],ink;
    long long sum;
    scanf("%d",&t);while(t--)
    {cin>>r>>k>>n;
    ae++;
    for(long i=0;i<n;i++)
    {cin>>a[i];
     b[i]=0;}  
     sum=0;  
     p=0;
     c=1;     
     cnt=0;
     in=0;inr=0;ink=0;
    while(1)
    {
   if(c-1==r)
   break;
    
   if(b[cnt]>0)
    {in=cnt;
    ink=sum-s[cnt];
    inr=c-b[cnt];
    break;
      }
    else
    { b[cnt]=c;
    s[cnt]=sum;
   // printf("cnt=%d %d %lld ",cnt,c,sum);    
         p=0;
    v=0;
        while(p+a[cnt]<=k&&v<n)
      { p=p+a[cnt];
       
       //printf("h=%d ",cnt);
       cnt++;
       v++;
    cnt=cnt%n;}
    }sum=sum+p;
    c++;
   
                      }  
              
         // printf("%d %ld %lld\n",in,inr,ink);    
          nn=0;
          mm=(r-c+1);
          if(mm>0)
          {nn=mm%inr;
          mm=mm/inr;
          sum=sum+mm*ink;
          
                  }
                  cnt=in;
          while(nn--)
          {  p=0;
    v=0;
        while(p+a[cnt]<=k&&v<n)
      { p=p+a[cnt];
       
       //printf("h=%d ",cnt);
       cnt++;
       v++;
    cnt=cnt%n;}
    sum=sum+p;
    
                             
}printf("Case #%d: %lld\n",ae,sum);
    }
    //while(1);
return 0;
}
