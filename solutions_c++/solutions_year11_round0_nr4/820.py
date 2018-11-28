#include <iostream>
#include <algorithm>
#include <vector>

#define FR(i, n) for (int i=0; i<(n); i++)
#define FOR(i, a, b) for (int i=(a); i<=(b); i++)

using namespace std;

int ntest;
double res;
int n, a[1111], d[1111];

void process() {
     cin >> n;
     FOR(i, 1, n) cin >> a[i];
     
     memset(d, 0, sizeof(d));
     res = 0;
     FOR(i, 1, n) if (d[i]==0) {            
            int cnt = 0;
            int j = i;
            while (d[j]==0) {
                  d[j] = 1; cnt++;
                  j = a[j];
            }
            if (cnt==1) continue;
            res += cnt;                        
     }
}

int main() {
    
    freopen("D-large.in", "rt", stdin);
    freopen("d.out", "wt", stdout);
    
    cin >> ntest;
    for (int i=1; i<=ntest; i++) {
        process();           
        printf("Case #%ld: %.6lf\n", i, res);
    }    
    
    return 0;
}
