#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    char str[105][105];
    double a[105],b[105],c[105];
    int p[105],q[105];
    int c1,n,i,j,k=1;
    double t;
    scanf("%d",&c1);
    while(c1--)
    {
        scanf("%d",&n);
        for( i=0; i<n; ++i)
        {
            scanf("%s",str[i]);
        }
        for( i=0; i<n; ++i)
        {
            p[i]=q[i]=0;
            for( j=0; j<n; ++j)
            {
                if(str[i][j]!='.')
                {
                    p[i]++;
                    if(str[i][j]=='1') q[i]++;
                }
            }
            a[i]=q[i]*1.0/p[i];
        }
        for( i=0; i<n; ++i)
        {
            t=0;
            for( j=0; j<n; ++j)
            {
                if(str[i][j]!='.')
                {
                    if(str[j][i]=='1')
                    {
                        t+=(q[j]-1)*1.0/(p[j]-1);
                    }
                    else
                    {
                        t+=(q[j])*1.0/(p[j]-1);
                    }
                }
            } 
            b[i]=t/p[i];
        }
        for( i=0; i<n; ++i)
        {
            t=0;
            for( j=0; j<n; ++j) 
            {
                if(str[i][j]!='.')
                {
                    t+=b[j];
                }
            }
            c[i]=t/p[i];
        }
        printf("Case #%d:\n",k++);
        for( i=0; i<n; ++i)
        {
            printf("%.9lf\n",0.25*a[i]+0.5*b[i]+0.25*c[i]);
        }
    }
    return 0;
}









