#include <stdio.h>
#include <iostream>
using namespace std;
int j;
int t0;
int r,k,n;
__int64 s[1100];
int a[1100],link[1100];
int main()
{
    freopen("c3.in","r",stdin);
    freopen("c3.out","w",stdout);
    scanf("%d",&t0);
    for (int t1=1;t1<=t0;t1++)
    {
        scanf("%d%d%d",&r,&k,&n);
        for (int i=0;i<n;i++) scanf("%d",&a[i]),a[i+n]=a[i];
        for (int i=0;i<n;i++)
        {            
            s[i]=0;
            for (j=i;j<i+n;j++)
            {
                if (s[i]+a[j]<=k) s[i]+=a[j]; else break;
        
            }
            link[i]=j%n;
        }
        __int64 ans=0;
        j=0;
        for (;r>0;r--)
        {
            ans+=s[j];           
            j=link[j] ;          
        }              
        cout<<"Case #"<<t1<<": "<<ans<<endl;  
    }
}
