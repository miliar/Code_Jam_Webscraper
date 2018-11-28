#include<iostream>
#include<cstdlib>
#include<fstream>

using namespace std;

int gcd(int n, int m)
{
    if (m==0)
        return n;
    else
        return gcd(m, n % m);
}

int main()
{
    //ifstream cin("A-large.in");
   // ofstream cout("A-large.out");
    int ts;
    cin>>ts;
    for (int ti=0; ti<ts; ti++)
    {
        long long n;
        int d,g,m;
        cin>>n>>d>>g;
        cout<<"Case #"<<ti+1<<": ";
        if ((g==0)&&(d>0))
        {
            cout<<"Broken"<<endl;
            continue;
        }
        if ((g==100)&&(d<100))
        {
            cout<<"Broken"<<endl;
            continue;
        }
        m=100/gcd(d,100);
        if (m<=n)
            cout<<"Possible"<<endl;
        else
            cout<<"Broken"<<endl;
    }
    return 0;
}
