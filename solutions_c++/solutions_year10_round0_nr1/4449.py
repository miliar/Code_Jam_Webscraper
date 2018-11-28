#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <string>
#include <math.h>

using namespace std;

int a[100][100];

int main()
{
    int i,j,m,n,k;
    int ii,nn,cas;
    
    freopen("A-small-attempt4.in","r",stdin);
    freopen("A-small-attempt3.out","w",stdout);
    
    scanf("%d",&nn);
    for(i=1;i<=nn;i++)
    {
                      scanf("%d%d",&n,&k);
    int mask=(1<<n)-1;
        if((k&mask)==mask)
            printf("Case #%d: ON\n",i,cas);
        else
            printf("Case #%d: OFF\n",i,cas);
            }       
    return 0;
}
