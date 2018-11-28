#include <cstdio>
#include <algorithm>
using namespace std;
const int N = 10*1000;
const int NIL = (-1);
typedef long long LL;

int n;
LL r,k,g[N];
int where[N];
LL cost[N];
int last[N];
LL last_cost[N];

void prep(int q) {
    LL s = 0;
    int i=0;
    while(i<n&&s+g[q+i]<=k) {
        s += g[q+i];
        i++;
    }
    where[q] = (q+i)%n;
    cost[q] = s;
    //printf("where %d = %d\n",q,where[q]);
}

void scase() {
    scanf("%lld%lld%d",&r,&k,&n);
    for(int i=0;i<n;i++) {
        scanf("%lld",&g[i]);
        g[n+i] = g[i];
    }
    for(int i=0;i<n;i++) prep(i);
    for(int i=0;i<n;i++) last[i] = (-1);
    LL result = 0;
    int it = 0;
    int i = 0;
    bool cyc = 1;
    while(r>0) {
        if (last[it]!=NIL && cyc) {
            int d = i - last[it];
            if (r>=d) {
                result += (result-last_cost[it])*(r/d);
                r %= d;
            }
            cyc = 0;
        } else {
            last[it] = i;
            last_cost[it] = result;
            result += cost[it];
            it = where[it];
            i++;
            r--;
        }
    }
    printf("%lld\n",result);
}

int main() {
    int j;
    scanf("%d",&j);
    for(int i=0;i<j;i++) {
        printf("Case #%d: ",i+1);
        scase();
    }
    return 0;
}


    

