#include <iostream>
#include <cmath>
using namespace std;
const double eps=1e-6;

const int N = 1000;

int n;

int a[N];
int b[N];
int result = 0;

    void inputing()
    {
        scanf("%d",&n);
        for ( int i=0;i<n;i++ )
        scanf("%d%d",&a[i],&b[i]);
    }

    void work()
    {
        int i,j;
        result = 0;
        for ( i=0;i<n;i++ )
            for ( j=i+1;j<n;j++ )
            {
                int temp = (a[i] - a[j])*( b[i] - b[j] );
                if ( temp < 0 )
                result++;
            }
    }

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int i,cas;
    scanf("%d",&cas);
    for ( i=1;i<=cas;i++ )
    {
        inputing();
        work();
        printf("Case #%d: %d\n",i,result);
    }

    return 0;
}

