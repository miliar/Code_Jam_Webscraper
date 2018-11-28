#include <iostream>
#include <cstdio>
using namespace std;
#define MaxN 110
int T;

int getans() {
    int N, S, p, t[MaxN];
    scanf("%d%d%d", &N, &S, &p);
    for (int i = 0; i < N; i++)
        scanf("%d", &t[i]);
    
    int ans = 0;
    
    for (int i = 0; i < N; i++) {
        if (t[i] % 3 == 0) { 
            if (t[i]/3 >= p) ans++;
            else if (t[i] > 0 && t[i]/3+1 >= p && S > 0) {
                S--; ans++;
            }
        }else if (t[i] % 3 == 1) {
            if (t[i]/3+1 >= p) ans++;
            //suprising nepadeda, bet gali buti. (a-1) (a+1) (a+1)
        } else if (t[i] % 3 == 2) {
            if (t[i]/3 + 1 >= p) ans++;
            else if (t[i]/3 + 2 >= p && S > 0) {
                S--; ans++;
            }
        }
    }
    return ans;
}


int main() {
    freopen("B.in", "r", stdin);
    freopen("B.out","w",stdout);
    scanf("%d", &T);
    for (int xxx = 1; xxx <= T; xxx++) {
        printf("Case #%d: %d\n", xxx, getans());
    }
    
    
    
}
