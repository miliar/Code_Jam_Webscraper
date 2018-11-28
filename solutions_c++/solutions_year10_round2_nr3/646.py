#include <iostream>

using namespace std;

int a[100],b[100],n,kol;

void write()
{
    int uk=0,i,j,k;
    for (i=2;i<=n;i++)
      if (a[i])
      {
          uk++;
          b[uk]=i;
      }
   int f=0;
   i=1;
   while (i<uk)
   {
       i=b[i];
   }
   if (i==uk)
   {
       kol++;
      /* for (k=1;k<=uk;k++)
         cout<<b[k]<<" ";
       cout<<endl;*/
   }
}

void bin(int t)
{
    if (t==n) write(); else
    {
        for (int j=0;j<2;j++)
        {
            a[t]=j;
            bin(t+1);
        }
    }
}

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int i,k,j,q,t;
    cin>>t;
    for (q=0;q<t;q++)
    {
        kol=0;
        cin>>n;
        a[n]=1;
        bin(2);
        printf("Case #%d: ",q+1);
        cout<<kol%100003<<endl;
    }
    return 0;
}
