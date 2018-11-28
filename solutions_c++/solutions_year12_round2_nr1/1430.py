#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

const double eps=1e-8;

#define MEM(a) memset(a,0,sizeof(a));
#define FOR(i,n) for(int i=0;i<n;i++)

double a[201],b[201];

int main()
{
    //freopen("A-small-attempt2.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,cnt=0;
    scanf("%d",&t);
    double x,n;
    while(t--)
    {
        cnt++;
        scanf("%lf",&n);
        x=0.0;
        FOR(i,n)
        {
            scanf("%lf",&a[i]);
            x+=a[i];
        }
        FOR(i,n)
        {
            b[i]=(2.0*x-n*a[i])/(n*x);
        }/*
        FOR(i,n)
        {
            printf("%f ",b[i]);
        }
        printf("\n");*/
        double tem=x,count=0.0;
        FOR(i,n)
        {
            if(b[i]<=0.0)
            {
                b[i]=0.0;
                tem-=a[i];
                count+=1.0;
            }
        }
        FOR(i,n)
        {
            if(b[i]!=0.0)
            {
                b[i]=(x-(n-count)*a[i]+tem)/(x*(n-count));
            }
        }
        printf("Case #%d: ",cnt);
        FOR(i,n)
        {
            if(i!=n-1)
                printf("%f ",b[i]*100.0);
            else
                printf("%f\n",b[i]*100.0);
        }
    }
    return 0;
}
