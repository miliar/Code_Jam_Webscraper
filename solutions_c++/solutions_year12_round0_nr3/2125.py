#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<sstream>
#include<queue>
#include<cstdio>

using namespace std;

const int MX=10000000;

int rec[MX];
int V[MX];

void init()
{
    int i,x,z,d=10;
    for(i=0;i<MX;i++) rec[i]=-1;
    for(i=0;i<=10;i++) rec[i]=i;

    for(i=1;i<MX;i++) if(rec[i]<0)
    {
        while(i>=d*10) d*=10;
        x=i;

        z=0;

        while(z==0)
        {
            z=x%10;
            x=(x/10)+z*d;
        }

        rec[i]=x;
    }

    //for(i=0;i<10000;i++) cout<<i<<" "<<rec[i]<<endl;
}

void test()
{
    int A,B,i,x;
    long long cnt,ans;
    cin>>A>>B;
    cnt=0; ans=0;

    memset(V,0,MX*sizeof(int));

    for(i=A;i<=B;i++) if(!V[i])
    {
        cnt=0; x=i;

        while(!V[x])
        {
            V[x]=1;
            cnt+=(x>=A&&x<=B);
            x=rec[x];
        }
        ans+=(cnt*(cnt-1))/2;
    }

    cout<<ans;

}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    init();

    int i,I;
    cin>>I;

    for(i=0;i<I;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        test();
        cout<<endl;
    }
    return 0;
}
