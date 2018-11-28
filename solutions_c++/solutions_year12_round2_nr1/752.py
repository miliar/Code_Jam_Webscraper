#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long ll;
const int maxn=1000;
const double eps=10e-5;
int a[maxn];
int b[maxn];

int main ()
{
    freopen("aa.in", "r", stdin);
    freopen("aa.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int I=1; I<=cas; ++I)
    {
        int n, sum=0; scanf("%d", &n);
        //printf("%d\n", n);
        for (int i=0; i<n; ++i)
        {
            scanf("%d", a+i);
            //printf("%d ", a[i]);
            sum+=a[i];
            b[i]=a[i];
        }
        ///sum;
        sort(b, b+n);
        int nn=n, tmp=sum;
        for (int i=n-1; i>=0; --i)
        {
            if(((sum+tmp+0.0)/(i+1)-b[i])>eps)
            {
                break;
            }
            tmp-=b[i];
            nn--;
        }
        //printf("%d %d\n", tmp, nn);
        printf("Case #%d:", I);
        for (int i=0; i<n; ++i)
        {
            double ans=((sum+tmp+0.0)/nn-a[i]+0.0)/(sum+0.0)*100;
            if(ans>eps)printf(" %lf", ans);
            else printf(" %0.6lf", 0.0);
        }
        printf("\n");

    }
    return 0;
}
