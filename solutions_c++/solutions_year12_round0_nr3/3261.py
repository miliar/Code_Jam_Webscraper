#include<iostream>
#include<cstdio>

using namespace std;
int permut1(int i)
{
    int a,b=0;
    a=i/10;
    b=((i-(a*10))*10+a);
    //cout<<"b="<<b<<endl;
    return b;
}
int permut2(int i)
{
    int a,b=0;
    a=i/100;
    b=((i-(a*100))*10+a);
    //cout<<"b="<<b<<endl;
    return b;

}
int main()
{
   // freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t=0,m=0,n=0,i=0,j=0;
    int a,b=0,count=0,ans=0;
    //int arr[1001];
    cin>>t;
    while(t--)
    {
        ans=0;
        cin>>a>>b;
        if(b>11)
        {
        if(a>11)
        j=a;
        else
        j=12;
        for(i=j;i<=b;i++)
        {
            if(i<100)
            {
                //cout<<"i="<<i<<endl;
                m=permut1(i);
                if(m<=b && i<m)
                {
                ans++;
                //arr[m]=1;
                }
            }
            else
            {
                m=permut2(i);
                if(m<=b && i<m)
                {
                    ans++;
                    //arr[m]=1;
                }
                n=permut2(m);
                if(n<=b && i<n)
                {
                    ans++;
                    //arr[n]=1;
                }
            }
        }
        }
        cout<<"Case #"<<++count<<": "<<ans<<endl;

    }
return 0;
}
