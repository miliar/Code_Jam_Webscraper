#include<iostream>
using namespace std;
#include<cmath>
int numofdigits(int n)
{
    int c=0;
    while(n>0)
    {
        c++;
        n=n/10;
    }
    return c;
}

bool isrecycle(int x,int y)
{
    int nx=numofdigits(x);
    int ny=numofdigits(y);
    if(nx!=ny || x==y)
        return false;
    int t=y;
    for(int i=0;i<ny;i++)
    {
        //int t=y;
        if(x==t)
            return true;
        t=(t%10)*pow(10,ny-1) + t/10;
    }
    return false;
}

int main() {
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
    int a,b;
    cin>>a>>b;
    int count=0;
    for(int i=a;i<=b;i++)
    {
        for(int j=i+1;j<=b;j++)
        {
            if(isrecycle(i,j))
                count++;
        }
    }
    cout<<"Case #"<<k<<": "<<count<<endl;
    }
}

