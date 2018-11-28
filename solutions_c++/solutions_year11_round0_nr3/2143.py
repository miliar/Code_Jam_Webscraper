#include <iostream>
#include <algorithm>
#define INF 1000000000
#define maxn 1111

using namespace std;

int n,a[maxn];
long long s,fmax;

void get(void)
{
    cin>>n;
    s=0;
    for (int i=1;i<=n;i++)
    {
        cin>>a[i];
        s+=a[i];
    }
}

bool pred(int x,int y)
{
    return x>y;
}

void sol(void)
{
    fmax=-INF;
    sort(a+1,a+n+1,pred);
    int p=0;
    s=0;
    for (int i=1;i<=n;i++)
    {
        s+=a[i];
        p^=a[i];
    }
    if (p==0) fmax=s-(long long)a[n];
}

void print(int nn)
{
    cout<<"Case #"<<nn<<": ";
    if (fmax>0) cout<<fmax;
    else cout<<"NO";
    cout<<endl;
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
