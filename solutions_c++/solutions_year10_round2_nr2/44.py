#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <ctime>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define SIZE(c) ((int)((c).size()))
#define FOREACH(i,c) for(__typeof((c).begin()) i =(c).begin();i!=(c).end();++i)
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;
typedef long double LD;

#define st first
#define nd second
#define mp make_pair
#define pb push_back

const int NIL = (-1);

int n,k,b,t;
int v[1000];
int x[1000];
int p[1000];
bool f[1000];

bool cmp(const int &a, const int &b) {
    return x[a] > x[b];
}

void scase() {
    scanf("%d%d%d%d",&n,&k,&b,&t);
    for(int i=0;i<n;i++) scanf("%d",&x[i]);
    for(int i=0;i<n;i++) scanf("%d",&v[i]);
    for(int i=0;i<n;i++) p[i] = i;
    sort(p,p+n,cmp);
    for(int i=0;i<n;i++) 
        f[i] = ( (b-x[p[i]]) <= (t*v[p[i]]) );
    int count = 0;
    for(int i=0;i<n;i++) if (f[i]) count++;
    if (count < k) {
        printf("IMPOSSIBLE\n");
        return;
    }
    int swaps = 0;
    int bad = 0;
    int good = 0;
    int it = 0;
    while(good < k) {
        if (f[it]) {
            swaps += bad;
            good++;
            it++;
        } else {
            bad ++;
            it ++;
        }
    }
    printf("%d\n",swaps);

}

int main() {
    int j;
    scanf("%d",&j);
    for(int i=1;i<=j;i++) {
        printf("Case #%d: ",i);
        scase();
    }
    return 0;
}

