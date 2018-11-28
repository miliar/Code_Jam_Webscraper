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














