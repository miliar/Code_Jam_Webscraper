#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <sstream>
#include <set>

using namespace std;

int a[2000004],ans,i,n,m,p,j,w=-1;
int del[2000004];

int gam(int x)
{
    int i,ans=1;
    for (i=0; i<x; i++)ans*=10;
    return ans;
}

void qqff ()
{
     
     int x=m,y=n,xy=0;
     do
     {
         x/=10;
         y/=10;
         xy++;
     }while (x && y);
     if (x<y)m=gam(xy+y);
}
     

int qf(int xx)
{
    set <string> fans;
    stringstream ss;
    string x;
    ss << xx;
    ss >> x;
    fans.insert(x);
    int p,i,L=x.size();
    for (i=0; i<L-1; i++)
    {
        x=x.substr(1)+x[0];
        stringstream s1(x);
        s1 >> p;
        if (p>xx && p<=n)
        {
           fans.insert(x);
           a[p]=1;
           w++;
           del[w]=p;
        }
    }
    L=fans.size();
    for (i=1; i<L; i++)ans+=i;
}

int main()
{
    freopen ("Recycled Numbers.in" , "r" , stdin);
    freopen ("Recycled Numbers.out" , "w" , stdout);
    cin >> p;
    for (j=1; j<=p; j++)
    {
        cin >> m >> n;
        qqff();
        for (i=m; i<=n; i++)
            if (a[i]!=1)
               qf(i);
        cout << "Case #" << j << ": " << ans << endl;
        ans=0;
        for (; w>=0; w--)
            a[del[w]]=del[w]=0;
    }        
}
