#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
int a[1111111],b[1111111],l,c,i,j,k,n,m;
long long t;
bool cmp(const long long &a,const long long &b)
{
     return a>b;
}
int main()
{
    int T,p=0;
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B.out","w",stdout);
    cin>>T;
    while (T--)
    {p++;
       cin>>l>>t>>n>>c;
       for (i=0;i<c;i++)
       scanf("%d",&a[i]);
       long long q1=0;
       for (i=1;i<=n;i++)
       {
           b[i]=a[q1]*2;
           q1++;
           q1%=c;
       }
       long long sum=0;
       long long p1=0;
       i=1;
       if (t>0)
       for (i=1;i<=n;i++)
       {
           sum+=b[i];
           if (sum>t)
           {
             b[i]=sum-t;
             sum=t;
             break;
           }
       }
       sort(b+i,b+n+1,cmp);
       int fuck=i;
       for (i,j=0;i<=n&&j<l;i++,j++)
       {
           b[i]/=2;
       }
       for (i=fuck;i<=n;i++)
       sum+=b[i];
       printf("Case #%d: ",p);
       cout<<sum<<endl;
    }
}
    
