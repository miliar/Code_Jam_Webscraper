#include <iostream>

using namespace std;
int main()
{
    long pow(long,long);
    long n,t,i=0,j,d,s1,c1=0;
    long t1[7];
    long t2[7];
    int Q;
    cin>>Q;
    int A[Q],B[Q],c[Q];
    for (int p=0;p<Q;p++)
    {
        cin>>A[p]>>B[p];
        c[p]=0;
    }
    for(int p=0;p<Q;p++)
    {

    for(n=A[p];n<=B[p];n++)
    {
        int t3[1000];
        int k=0,l,m;
        t=n;
        d=n;
        for(i=0;t>0;i++)
        {
            t1[i]=d%pow(10,i+1);
            t=t/10;
            t2[i]=t;
        }
        s1=i-1;

        for(j=0;j<=s1;j++)
        {
            t2[j]=t2[j]+(t1[j]*pow(10,s1-j));

        }
        for(j=0;j<=s1;j++)
        {
        if(t2[j]>n)

         {
            if(t2[j]<=B[p])
            {
                ++c[p];
            }

         }

        }
        for(l=0;l<k;l++)
        {
            for(m=l+1;m<k;m++)
            {
                if(t3[l]==t3[m])
                c[p]--;
            }
        }

    }
cout<<"Case #"<<p+1<<" "<<c[p]<<endl;
    }

    return 0;
}
long pow(long a,long b)
{
    long k=1;
    for(long i=1;i<=b;i++)
    {
        k=k*a;
    }
    return k;
}
