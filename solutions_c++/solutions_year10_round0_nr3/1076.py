#include <stdio.h>
#include <algorithm>
#define FOR(q,n) for(int q=0;q<n;q++)

#define INF  (1ll<<60)
#define MAX 10000
long long int data[MAX];
long long int sums[MAX];

void solve(int _case) {
    long long int r,k,n;
    scanf("%lld %lld %lld",&r,&k,&n);
    FOR(q,n) scanf("%lld", &data[q]);
    FOR(q,MAX) sums[q]=INF;
    sums[0]=0;
    FOR(q,n) sums[q+1] = sums[q] + data[q];
    FOR(q,n) sums[n+q+1] = sums[n+q] + data[q];
    // mam prefixova suma
    // sucet <i,j) = sums[j] - sums[i]

    long long int cost=0;
    int current_start = 0;
    FOR(q,r) { // make round
        long long int start = sums[current_start]; // tolkoto mame na
        // zaciatku
        long long int max = start + k; // toto je maximum, co si
        // mozeme dovolit najst
        // t.j., mozem najst max, nemozem najst max+1
        // t.j. hladam (lower_bound(max+1)-1)
        long long int pos = std::lower_bound(sums, sums+MAX, max+1) - sums;
        pos--;
        if (pos<0) continue;
        // ok, teraz to musime checknut
        pos = std::min(pos, current_start+n);
        cost += sums[pos] - start;

        current_start = pos %n;
    }

    printf("Case #%d: %lld\n",_case,cost);
}

int main(){
 int t;
 scanf("%d",&t);
 FOR(q,t) solve(q+1);
}

