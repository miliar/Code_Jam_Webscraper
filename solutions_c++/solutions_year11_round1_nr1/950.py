#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <utility>
#include <algorithm>

using namespace std;

long long hgcd(long long a, long long b)
{
        if(b == 0)
        {
                return a;
        }
        else
        {
                return hgcd(b, a % b);
        }
}

int main()
{
    int t;
   
    cin>>t;
     long long n,pd,pg;
    for(int ii=1; ii<=t; ii++)
    {
       
        cin>>n>>pd>>pg;
              
        cout<<"Case #"<<ii<<": ";
	if (pg==0 && pd>0)
	{
            cout<<"Broken\n";
	    continue;
        }
        if (pg==100 && pd!=100)
	{
            cout<<"Broken\n";
            continue;
        }
        if (pd == 100)
	{
            cout<<"Possible\n";
            continue;
        }
       
        if (pd<100 && pg<100)
	{
            long long gcd=hgcd(pd,100);
            pd/=gcd;
            long long resto=100/gcd;
            if(resto<=n && resto>pd ) cout<<"Possible\n";
            else cout<<"Broken\n";
        }
    }
   
    return 0;
}