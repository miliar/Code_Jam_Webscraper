#include <iostream>
#include <fstream>
using namespace std;
int f (int a, int b)
{
    int i, j;
    for (i=0;i<100;++i)
    {
        for (j=b;j>=2;--j)
        {
            if (a%j==0 && b%j==0)
            {
                a/=j;
                b/=j;
            }
        }
    }
    return b;
}
int main()
{
    ifstream cin("a.in");
    ofstream cout("a.out");
    int n, i, a, b, c, x;
    cin>>n;
    for (i=0;i<n;++i)
    {
        cin>>a>>b>>c;
        if (c==0)
        {
            if (b==0)
            {
                cout<<"Case #"<<(i+1)<<": ";
                cout<<"Possible"<<endl;
            }
            else
            {
                cout<<"Case #"<<(i+1)<<": ";
                cout<<"Broken"<<endl;
            }
            continue;
        }
        if (c==100 && b!=100)
        {
            cout<<"Case #"<<(i+1)<<": ";
            cout<<"Broken"<<endl;
            continue;
        }
        x=f(b, 100);
        cout<<"Case #"<<(i+1)<<": ";
        if (x<=a)
        {
            cout<<"Possible"<<endl;
        }
        else
        {
            cout<<"Broken"<<endl;
        }
    }
    return 0;
}
