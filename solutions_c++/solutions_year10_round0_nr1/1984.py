#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <complex>
#include <queue>
#include <ctime>
#include <ext/numeric>
#include <ext/hash_map>
#include <ext/hash_set>

using namespace std;
using namespace __gnu_cxx;

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define rep(i,x,n) for(int i = (x) ; i < (n) ; ++i)
#define repit(it,x,n) for(__typeof(x) it = (x) ; it!=(n) ;++it)

int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in","rt",stdin);
    freopen("out.out","wt",stdout);
#endif
    int t,n,k;
    scanf("%d",&t);
    rep(tt,0,t)
    {
        scanf("%d %d",&n,&k);
        int r = 1<<n;
        k++;
        printf("Case #%d: ",tt+1);
        if(k%r==0)
            printf("ON\n");
        else
            printf("OFF\n");
    }
    
    return 0;
}
