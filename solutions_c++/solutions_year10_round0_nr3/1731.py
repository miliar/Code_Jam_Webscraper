#include <iostream>

using namespace std;

int a[1002],g[1002];
unsigned long long res[1000000];

int main()
{
    int j,n,i,k,q,r,t,v,z,f;
    unsigned long long kol,sum;
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    cin>>t;
    for (q=0;q<t;q++)
    {
        cin>>r>>k>>n;
        kol=0;
        for (i=0;i<n;i++)
        {
            a[i]=-1;
            scanf("%d",&g[i]);
        }
        i=0;
        j=0;
        while (r>0)
        {
            sum=0;
            if (a[i]>=0)
            {

                for (v=a[i];v<j;v++)
                {
                  sum=sum+res[v];
                  //cout<<a[i]<<endl;
                }
                //cout<<r<<":::"<<res[a[i]]<<" "<<j<<"==="<<kol<<"!!!"<<sum<<endl;
                kol=kol+(r/(j-a[i]))*sum;
                z=r%(j-a[i]);
                for (v=a[i];v<a[i]+z;v++)
                {
                    kol=kol+res[v];
                }
                break;
            }
            a[i]=j;
            f=i;
            while (sum+g[i]<=k)
            {
                sum=sum+g[i];
                i=(i+1)%n;
                if (i==f) break;
            }
            kol=kol+sum;
            res[j]=sum;
            r--;
            j++;
        }
       printf("Case #%d: ",q+1);
       cout<<kol<<endl;
    }
    return 0;
}
