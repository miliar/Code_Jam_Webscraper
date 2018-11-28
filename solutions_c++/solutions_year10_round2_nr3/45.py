#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
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

const LL P = 100003;

map<PII,LL> C;

LL choose(int n, int k) {
    PII id = PII(n,k);
    if (C.count(id)) return C[id];
    if (k>n || k<0) {
        C[id] = 0;
    } else if (k==0||k==n) {
        C[id] = 1;
    } else {
        C[id] = (choose(n-1,k-1)+choose(n-1,k))%P;
    }
    return C[id];
}

map<PII,LL> D;

LL dp(int n, int size) {
    PII id = PII(n,size);
    if (D.count(id)) return D[id];
    if (n==size+1) {
        D[id] = 1;
    } else if (n==1) {
        D[id] = (size==0);
    } else if (size==1) {
        D[id] = 1;
    } else {
        D[id] = 0;
        for(int i=1;i<size;i++) 
            D[id] = (D[id] + dp(size,i)*choose(n-size-1,size-i-1))%P;
    }
    return D[id];
}
        
LL result(int n) {
    LL z = 0;
    for(int i=1;i<n;i++) z = (z+dp(n,i))%P;
    return z;
}

void scase() {
    int n;
    scanf("%d",&n);
    printf("%lld\n",result(n));
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

