#include<iostream>
#include<math.h>
#define MAX 10002
using namespace std;
int digit(int a)
{
    int dig=0;
    while(a)
    {
        dig++;
        a/=10;
    }
    return dig;
}
int rec(int n,int m)
{
    int i=0,j=0,k=1,l=0,ll=1;
    for(l=0;l<m;l++)
    k=k*10;
    i=n%k;
    j=n/k;
    l=digit(n)-m;
    for(k=0;k<l;k++)
    ll*=10;
    return (i*ll +j);
}
int main()
{
    int t=0,k=0;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int flag[MAX];
        int a=0,b=0;
        cin>>a>>b;
        int i=0,j=0,ans=0,temp=0,cnt=0;
        for(i=0;i<=1000;i++)
        flag[i]=0;
        temp=a;
        int dig=digit(a);
        if(dig==1)
        {
            cout<<"Case #"<<k<<": 0"<<endl;
            continue;
        }
        for(i=a;i<=b;i++)
        {
            cnt=0;
            if(flag[i]==0)
            {
                flag[i]=1;
                for(j=1;j<dig;j++)
                {
                    if(rec(i,j)>=a && rec(i,j)<=b && i!=rec(i,j) && digit(i)==digit(rec(i,j)))
                    {
                        //cout<<i<<" , "<<rec(i,j)<<endl;
                        flag[rec(i,j)]=1;
                        cnt++;
                    }
                }
                if(cnt==1)
                ans+=cnt;
                else
                ans+=(cnt*(cnt+1))/2;
            }
        }
        cout<<"Case #"<<k<<": "<<ans;
        if(k!=t)
        cout<<endl;
    }
    return 0;
}
