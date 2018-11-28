#include <algorithm>
using namespace std;

int n;
int x[1000], y[1000];
int f, r;

int main(){
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
    int cases;  scanf("%d", &cases);
    for (int tc = 1; tc <= cases; tc++){
        scanf("%d", &n);
        for (int i = 0; i < n; i++) scanf("%d", x + i);
        for (int i = 0; i < n; i++) scanf("%d", y + i);
        sort(x, x + n);
        sort(y, y + n);
        f = 0;  r = n - 1;
        int ans = 0;
        int i;
        for (i = 0; i < n; i++)
            if (x[i] < 0) {
                ans += x[i] * y[r];
                r--;    
            } 
            else break;
        for (i = n - 1; i >= 0; i--)
            if (x[i] > 0){
                ans += x[i] * y[f];
                f++;   
            }
            else break;
        printf("Case #%d: %d\n", tc, ans);
    }
    return 0;   
}
