#include<iostream>
#include<cmath>
#define MAX 10002
using namespace std;
int digit(int a)
{
    int d=0;
    while(a)
    {
        d++;
        a/=10;
    }
    return d;
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
    int t_cases=0,k=0;
    cin>>t_cases;
    for(k=1;k<=t_cases;k++)
    {
        int flag[MAX];
        int i=0,j=0,ans=0,cnt=0;
        int a,b;
        cin>>a>>b;
        
        for(i=0;i<=1000;i++)
        flag[i]=0;

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
        if(k!=t_cases)
        cout<<endl;
    }
    return 0;
}
