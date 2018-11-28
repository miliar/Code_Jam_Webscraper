
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
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define ALL(c) (c).begin(),(c).end()
#define FIL(c,n) memset(c,n,sizeof(c))

int main()
{
    freopen("E:\\c.in","r",stdin);
    freopen("E:\\c.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ct=1;ct<=t;ct++)
    {
        int n;
        scanf("%d",&n);
        int a[1010];
        int sum=0,s=0,mina=(1<<30);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            sum^=a[i];
            s+=a[i];
            mina=min(a[i],mina);
        }
        printf("Case #%d: ",ct);
        if(sum)
        {
            puts("NO");
        }
        else
            printf("%d\n",s-mina);
    }
    return 0;
}

