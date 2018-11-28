#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 50;
int n;
char a[maxn][maxn];
int f[maxn];

void init() {
    scanf("%d", &n);
    for (int i=0;i<n;i++) {
        scanf("%s", &a[i]);
        f[i] = -1;
        for (int j=0;j<n;j++)
        	if (a[i][j]=='1')
        	    f[i] = j;
    }        
}

void work() {
    int ans = 0;
    for (int i=0;i<n;i++) {
        if (f[i]>i) {
            int max = -1, p = -1;
            for (int j=i+1;j<n;j++)
            	if (f[j]<=i) {
            	    p = j;
            	    break;
            	}
            ans += p - i;
            for (int j=p;j>i;j--)
            	swap(f[j],f[j-1]);
        }
    }
    printf("%d\n", ans);            
}
            
int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int ti=1;ti<=T;ti++) {
        printf("Case #%d: ", ti);
        init();
        work();
    }    
    return 0;
}    
