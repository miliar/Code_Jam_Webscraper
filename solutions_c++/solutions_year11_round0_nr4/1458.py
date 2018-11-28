
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
     freopen("E:\\d.in","r",stdin);
     freopen("E:\\d.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int ct=1;ct<=t;ct++)
    {
        int n;
        scanf("%d",&n);
        int a[1010],ans=0;
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
            if(a[i]!=i)
                ans++;
        }
        printf("Case #%d: %d\n",ct,ans);
    }
    return 0;
}

