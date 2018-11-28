#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <utility>
#include <string>
#include <map>
#include <set>
#define maxn 211
#define eps 1e-6

#define INP "A.in"
#define OUP "A.out"

using namespace std;

int n;
double a[maxn + 1];
double sum;

bool can(double per,int x)
{
    double value = per*sum/100 + a[x];
    double rest =  100 - per;
    for (int i=1;i<=n;i++){
        if (i==x)
            continue;
        if (a[i]<value){
            double cur = (value - a[i])/sum*100;
            rest -= cur;
        }
    }
    return rest<0;
}

int main()
{
    freopen(INP,"r",stdin);
    freopen(OUP,"w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int tt=1;tt<=tc;tt++){
        scanf("%d",&n);
        printf("Case #%d:",tt);
        sum = 0;
        for (int i=1;i<=n;i++)
            scanf("%lf",&a[i]),sum += a[i];
        for (int i=1;i<=n;i++){
            double left = 0,right = 100;
            while (right - left>=eps){
                double mid = (left + right)/2;
                if (can(mid,i))
                    right = mid;
                else
                    left = mid + eps;
            }
            printf(" %.5lf",right);
        }
        printf("\n");
    }

    return 0;
}
