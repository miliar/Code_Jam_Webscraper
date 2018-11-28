#include<iostream>
#include<cmath>
using namespace std;

int i,n,num[3],a,b,c,t,tt,k,ans;

FILE *in,*out;

int gcd(int a,int b)
{
    if (a%b==0)
        return b;
    return gcd(b,a%b);
}

int gcd(int a,int b,int c)
{
    return gcd(gcd(a,b),c);
}

int main()
{
    //in=freopen("B-small.in","r",stdin);
    in=freopen("B-small-attempt0.in","r",stdin);
    out=freopen("B-small.txt","w",stdout);
    cin>>t;
    for (tt=1;tt<=t;tt++)
    {
        cin>>n;
        for (i=0;i<n;i++)
            cin>>num[i];
        if (num[0]==num[1])
        {
            num[1]=num[2];
            n=2;
        }
        if (num[0]==num[2])
            n=2;
        if (num[1]==num[2])
            n=2;
        if (n==3)
        {
            a=abs(num[0]-num[1]);
            b=abs(num[1]-num[2]);
            c=abs(num[2]-num[0]);
            k=gcd(a,b,c);
        }
        else
            k=abs(num[0]-num[1]);
        i=0;
        ans=0;
        while (i<n)
        {
            if (num[i]%k!=0)
                break;
            i++;
        }
        if (i!=n)
            ans=k-num[0]%k;
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    fclose(in);
    fclose(out);
    return 0;
}
        
        
        
