#include<iostream>

using namespace std;
int main()
{
    int n,k,test,i,m;
    freopen("A_large.in","r",stdin);
    freopen("A_large_out.txt","w",stdout);
    cin>>test;
    for(i=1;i<=test;i++)
    {
        cin>>n>>k;
        m=(1<<n)-1;
        n=(1<<n);
        k=k%n;
        if(k==m)
            cout<<"Case #"<<i<<": ON"<<endl;
        else
            cout<<"Case #"<<i<<": OFF"<<endl;
    }

    return 0;
}
