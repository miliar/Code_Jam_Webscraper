#include<iostream>

using namespace std;

int a[1010][2];

int comp(const void *a, const void * b)
{
    return ((int*)a)[0]-((int *)b)[0];
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out4.txt","w",stdout);
    int t,n,i,j,res,cnt=1;
    cin>>t;
    while(t--)
    {
       cin>>n;
       res=0;
       for(i=0;i<n;i++)
           cin>>a[i][0]>>a[i][1];
       qsort(a,n,sizeof(int)*2,comp);
       for(i=0;i<n;i++)
       {
           for(j=i+1;j<n;j++)
           {
                if(a[j][1]<a[i][1])
                   res++;
           }
       }
       cout<<"Case #"<<cnt++<<": "<<res<<endl;
    }
    return 0;
}
