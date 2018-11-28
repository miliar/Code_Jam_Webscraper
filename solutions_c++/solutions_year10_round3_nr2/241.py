#include<iostream>
using namespace std;

int main()
{
    int t,ti=0,p,c,a,b;
    long long l;
    cin>>t;
    while(t>0)
    {
        t--;ti++;
        cin>>l>>p>>c;
        a=0,b=0;
        while(l*c<p)
        {
            l*=c;a++;
        }
        while(a>0)
        {
            a/=2;b++;
        }
        cout<<"Case #"<<ti<<": "<<b<<endl;
    }
}
