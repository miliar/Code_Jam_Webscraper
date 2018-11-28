#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <functional>
#include <utility>//pair
#include <iomanip>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl;
#define inf (1<<30)
#define PB push_back
#define MP make_pair
#define mset(x, a) memset(x, (a), sizeof(x))
typedef long long LL;
const double PI = acos(-1.0);
const double eps = 1e-8;
const int INF = 0x3f3f3f3f;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int c,n,num,i,ans,m,t,w=1;
    scanf("%d",&c);
    while(c--)
    {
        scanf("%d",&n);
        m=1<<30;
        t=ans=0;
        for( i=0; i<n; ++i)
        {
            scanf("%d",&num);
            if(m>num) m=num;
            ans+=num; 
            t^=num;
        }
        printf("Case #%d:",w++);
        if(t) printf(" NO\n");
        else printf(" %d\n",ans-m);
    }    
    return 0;
}


