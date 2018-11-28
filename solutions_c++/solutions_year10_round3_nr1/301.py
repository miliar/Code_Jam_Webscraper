#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
struct f
{
    int a,b;
}node[1010];
int cmp(const void *c,const void *d)
{
    return (*(struct f*)d).b-(*(struct f*)c).b;
}
int main()
{
   // freopen("in.txt","r",stdin);
   // freopen("A-small-attempt0.in","r",stdin);
   // freopen("A-small-attempt1.in","r",stdin);
    //freopen("A-small-attempt2.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    int t,flag,i,j,ans,n;
    
    scanf("%d",&t);
    for(flag=1;flag<=t;flag++) {
        printf("Case #%d: ",flag);
        scanf("%d",&n);
        for(i=0;i<n;i++) scanf("%d%d",&node[i].a,&node[i].b);
        qsort(node,n,sizeof(node[0]),cmp);
        ans=0;
        for(i=0;i<n;i++) {
            for(j=i+1;j<n;j++) {
                if(node[j].a>node[i].a) ans++;
            }
        }
        printf("%d\n",ans);
    }
    return 0;
}
