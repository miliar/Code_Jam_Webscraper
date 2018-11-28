#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <stack>
#include <algorithm>
using namespace std;

const int N=2000;
int a[N];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //
    int Tests;
    scanf("%d",&Tests);
    for(int Test=1;Test<=Tests;Test++)
    {
        printf("Case #%d: ", Test);
        //
        int n;
        scanf("%d",&n);
        int xr=0,sum=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",a+i);
            xr^=a[i];
            sum+=a[i];
        }
        if(xr>0)
            printf("NO");
        else
            printf("%d",sum-*min_element(a,a+n));
        //
        printf("\n");
    }
    return 0;
}
