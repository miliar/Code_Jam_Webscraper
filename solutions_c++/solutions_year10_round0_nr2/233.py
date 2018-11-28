#include<iostream>
using namespace std;

int c,n;
int t[1010],a[1010];

int gcd(int a,int b)
{
    if(a<b) swap(a,b);
    int cc=a%b;
    while(cc!=0)
    {
        a=b;
        b=cc;
        cc=a%b;
    }
    return b;
}

int main()
{
    freopen("B-small-attempt3.in","r",stdin);
 //   freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&c);
    for(int ct=1;ct<=c;ct++)
    {
        printf("Case #%d: ",ct);
        
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d",&t[i]);
        sort(t,t+n);
        
        int l=1;
        for(int i=1;i<n;i++)
        {
            if(t[i-1]!=t[i])
                t[l++]=t[i];
        }
        n=l;
        if(n==1)
        {
            printf("0\n");
            continue;
        }
        
        for(int i=1;i<n;i++) a[i-1]=t[i]-t[i-1];
        
        int minx=1000000000;
        for(int i=0;i<n-1;i++)
            for(int j=i;j<n-1;j++)
            {
                int gcdij=gcd(a[i],a[j]);
                if(minx>gcdij)
                    minx=gcdij;
            }
        
   //     for(int i=0;i<n-1;i++) printf("%d ",a[i]); printf("\n");
   //     printf("%d\n",minx);
        if(t[0]%minx==0) printf("0\n");
        else printf("%d\n",minx-t[0]%minx);
        
    }
    
    
    return 0;
}
