#include <stdio.h>
#define FOR(q,n) for(int q=0; q<n; q++)

void solve(int _case) {
    int cnt=0;
    int n,k;
    int b,t;
    scanf("%d %d %d %d",&n,&k,&b,&t);
    int x[100];
    int v[100];
    int stihne[100];
    FOR(q,n) scanf("%d", &x[q]);
    FOR(q,n) scanf("%d", &v[q]);
    FOR(q,n) {
        stihne[q] = (t * (long long int) v[q] >= (long long int) b-x[q]);
    }
    for(int q=n-1; q>=0; q--) {
        if (k==0) break;
        if (stihne[q]) {
            k--;
            for (int w=q; w<n; w++)
                if (!stihne[w]) cnt++;
        }
    }




    if (k==0) {
        printf("Case #%d: %d\n",_case, cnt);
    } else {
        printf("Case #%d: IMPOSSIBLE\n",_case);
    }
}

int main() {
    int t;
    scanf("%d", &t);
    FOR(q,t) solve(q+1);

}
