#include <fstream>
#include <iostream>
#include<cmath>

using namespace std;

int main()
{   freopen("A-large.in","r",stdin);
	freopen("A-largeout.txt","w",stdout);

    int k,t,n,x,j,i,mask;
    cin>>t;

    for(int i=1;i<=t;i++)
    {x=1;
    cin>>n>>k;
    mask=1;
    for(j=1;j<=n;j++)
    {x=(k&mask)?(x):0;
    mask<<=1;
    }
    (x==1)?printf("Case #%d: ON\n",i):printf("Case #%d: OFF\n",i);

    }
    return 0;

}
