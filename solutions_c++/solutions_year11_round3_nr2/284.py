#include <iostream>
#include <cstdio>

using namespace std;

int st[1000001],a[1000],dist[10002];

long long abs(long long x)
{
    if (x>0)
      return x;
    return -x;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    long long t,n,c,T,L,res,t0,i,j,s0,passed,gr,num=0;
    int q;
    cin>>t;
    for (q=0;q<t;q++)
    {
        cin>>L>>T>>n>>c;
        gr=0;
        for (i=0;i<=10000;i++)
          dist[i]=0;
        for (i=0;i<c;i++)
        {
          cin>>a[i];
          gr+=a[i];
        }
        t0=T;
        s0=T/2;
        j=0;
        num=0;
        res=0;
        while (s0>0)
        {
            num++;
            s0-=a[j];
            j=(j+1)%c;
        }
        //cout<<num<<endl;
        /*if (s0<0)
        {
            j--;
            if (j<0)
              j=c-1;
            s0=a[j]+s0;
        }*/
        s0=abs(s0);
        //cout<<num<<endl;
        dist[s0]++;
        for (i=num;i<n;i++)
        {
            dist[a[i%c]]++;
        }
        if (num>n)
        {
            for (i=0;i<n;i++)
            {
                res+=a[i%c];
            }
            printf("Case #%d: ",q+1);
            cout<<2*res<<endl;
            continue;
        }
        //cout<<s0<<endl;
        /*cout<<T<<endl;
        for (i=0;i<20;i++)
          cout<<dist[i]<<" ";
        cout<<endl;*/
        res=0;
        for (i=10000;i>0;i--)
        if (dist[i]>0)
        {
            //cout<<"$"<<endl;
            if (L==0)
            {
                res+=2*dist[i]*i;
                //cout<<"!"<<res<<endl;
            }
            else
            if (L>=dist[i])
            {
                res+=dist[i]*i;
                L=L-dist[i];
                //cout<<"@"<<res<<endl;
            }
            else
            {
                //L=0;
                //cout<<i<<"-"<<dist[i]<<endl;
                res+=i*L+2*i*(dist[i]-L);
                L=0;
                //cout<<"#"<<res<<endl;
            }
        }
        printf("Case #%d: ",q+1);
        cout<<res+T<<endl;
    }
    return 0;
}
