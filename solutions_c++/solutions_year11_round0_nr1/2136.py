#include <iostream>
#define maxn 111

using namespace std;

int n,a[maxn],o,b,t[maxn],to,tb;
char c[maxn];

void get(void)
{
    cin>>n;
    for (int i=1;i<=n;i++)
        cin>>c[i]>>a[i];
    o=b=1;
    to=tb=0;
}

void print(int nn)
{
    cout<<"Case #"<<nn<<": "<<t[n]<<endl;
}

void sol(void)
{    
    for (int i=1;i<=n;i++)
        if (c[i]=='O')
        {
            t[i]=max(t[i-1]+1,to+abs(a[i]-o)+1);
            to=t[i];
            o=a[i];
        }
        else
        {
            t[i]=max(t[i-1]+1,tb+abs(a[i]-b)+1);
            tb=t[i];
            b=a[i];
        }
}        

int main(void)
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    for (int i=1;i<=T;i++)
    {
        get();
        sol();
        print(i);
    }
    return 0;
}
