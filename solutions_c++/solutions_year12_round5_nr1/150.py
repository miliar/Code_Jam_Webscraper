#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define debug(args...) fprintf(stderr,args);

typedef long long lint;
typedef pair<int,int> pii;

const int INF = 0x3f3f3f3f;
const lint LINF = 0x3f3f3f3f3f3f3f3fll;
const int MAXN = 1010;

int l[MAXN],p[MAXN];
int ord[MAXN], ans[MAXN];

bool cmp(int a,int b) {
    if(p[a]*l[b] == p[b]*l[a]) return a<b;
    return p[a]*l[b] > p[b]*l[a];
}

int main() {
    int T,n;
    scanf("%d",&T);
    for(int t=1;t<=T;++t) {
        printf("Case #%d: ",t);
        scanf("%d",&n);
        for(int a=0;a<n;++a) scanf("%d",&l[a]);
        for(int a=0;a<n;++a) scanf("%d",&p[a]);
        for(int a=0;a<n;++a) ord[a] = a;
        sort(ord,ord+n,cmp);
        for(int a=0;a<n;++a) printf("%d%c",ord[a],a==n-1?'\n':' ');
    }            
    return 0;
}
