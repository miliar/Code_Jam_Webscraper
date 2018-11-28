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
#include <complex>

#include <queue>
using namespace std;

#define FR(i,a,b) for(int i=a;i<b;i++)
#define FOR(i,n) FR(i,0,n)
#define FORI(i,v) FOR(i,(int)v.size())
#define FORALL(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i)
#define BEND(v) v.begin(),v.end()
#define dump(x) cerr << #x << " = " << (x) << endl;
typedef long long ll; typedef long double ld;
int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int tc,n,k,state;
    scanf("%d",&tc);
    for(int i=0;i<tc;i++) {
        scanf("%d%d",&n,&k);
        state = 0;
        //printf("%d %d %d\n",k %(1<<n),(1<<n)-1,k %(1<<n) == (1<<n)-1);
        if( k %(1<<n) == (1<<n)-1 )
            state = 1;
        printf("Case #%d: %s\n",i+1,state?"ON":"OFF");
    }

    return 0;
}

