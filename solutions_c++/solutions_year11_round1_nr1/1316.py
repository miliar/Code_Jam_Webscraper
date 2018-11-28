#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int n,pg,pd,q,t,f,i,j;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    for (q=0;q<t;q++)
    {
        cin>>n>>pd>>pg;
        f=0;
        for (i=1;i<=min(100,n);i++)
          for (j=0;j<=i;j++)
            if (100*j%i==0 && 100*j/i==pd)
              f=1;
        if (f && !(pd>0 && pg==0) && !(pd<100 && pg==100))
          printf("Case #%d: Possible\n",q+1);
        else
          printf("Case #%d: Broken\n",q+1);
    }
    return 0;
}
