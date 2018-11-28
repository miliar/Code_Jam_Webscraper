
#include<iostream>
using namespace std;

int main()
{    int b[1005];
   long a[1005];
    int t,v,c,cnt,in,ae=0;
    long long sum;
    long long s[1005],ink;
    long r,inr,p,n,k,mm,nn;
    scanf("%d",&t);while(t--)
    {cin>>r>>k>>n;
    ae++;
    for(long i=0;i<n;i++)
    {cin>>a[i];
     c=1;     
     cnt=0;
     b[i]=0;}  
     p=0;
     sum=0;  
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
         p=0;
    v=0;
        while(p+a[cnt]<=k&&v<n)
      { p=p+a[cnt];
       v++;
       cnt++;
    cnt=cnt%n;}
    }sum=sum+p;
    c++;
   
                      }  
          nn=0;
          mm=(r-c+1);
          if(mm>0)
          {nn=mm%inr;
          mm=mm/inr;
          sum=sum+mm*ink;
          
                  }
                  cnt=in;
          while(nn--)
          {   v=0;
   p=0;
        while(p+a[cnt]<=k&&v<n)
      { p=p+a[cnt];
       v++;
       cnt++;
    cnt=cnt%n;}
    sum=sum+p;
    
                             
}printf("Case #%d: %lld\n",ae,sum);
    }
return 0;
}
