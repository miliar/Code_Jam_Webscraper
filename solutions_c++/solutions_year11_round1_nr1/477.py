#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

typedef long long llong;

llong n,t,pd,pg,c,g;

llong gcd(llong a,llong b) {
    return b?gcd(b,a%b):a;
}

int main() {
    //freopen("D:\\A-small-attempt0.in","r",stdin);
    //freopen("D:\\A-small-attempt0.out","w",stdout);
    scanf("%lld",&t);
    for (c=1;c<=t;++c) {
        scanf("%lld%lld%lld",&n,&pd,&pg);
        g=gcd(pd,100);
        if (100/g<=n && !(pd<100 && pg==100) && !(pd>0 && pg==0))
            printf("Case #%d: Possible\n",c);
        else
            printf("Case #%d: Broken\n",c);
    }
    return 0;
}
