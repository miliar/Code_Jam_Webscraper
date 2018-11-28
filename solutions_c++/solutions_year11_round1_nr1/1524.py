#include<iostream>
using namespace std;
int dgy(int a,int b)
{
    int i;
    for (i=a;i>1;i--)
    if (a%i==0&&b%i==0) return i;
    return 1; 
}

int main()
{
    int d,i,t,pd,pg;
    long long n;
    cin>>t;
    for (i=1;i<=t;i++)
    {
        cin>>n>>pd>>pg;
        cout<<"Case #"<<i<<": ";
        if (n<100){
            if (pg==0||pg==100) if (pd==pg) {cout<<"Possible"<<endl;continue;}
            else {cout<<"Broken"<<endl;continue;}
            d=100/dgy(pd,100);
            if (n<d) {cout<<"Broken"<<endl;continue;}
        }
        cout<<"Possible"<<endl;
    }
}
