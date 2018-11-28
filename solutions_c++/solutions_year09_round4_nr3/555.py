#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 20;
const int maxk = 30;
int g[maxn][maxn], a[maxn][maxk], w[1<<maxn], f[1<<maxn];
int n, k, found, c, color[maxn], ans;

int legal(int a1, int a2, int b1, int b2) {
    if (b1 > a1 && b2 > a2) return 1;
    if (b1 < a1 && b2 < a2) return 1;
    return 0;
}
     
void getg(int x, int y) {
    for (int i=0;i<k-1;i++)
        if ( ! legal(a[x][i], a[x][i+1], a[y][i], a[y][i+1])) {
            g[x][y] = 1;
            return;
        }
    g[x][y] = 0;
}    
            
void init() {
    scanf("%d%d", &n, &k);
    for (int i=0;i<n;i++)
    	for (int j=0;j<k;j++)
     		scanf("%d", &a[i][j]);
    for (int i=0;i<n;i++)
    	for (int j=0;j<n;j++)
     		getg(i,j);
    for (int st=1;st<(1<<n);st++) {
        w[st] = 1;
        for (int x=0;x<n;x++)
        	if (st&(1<<x))
        		for (int y=0;y<n;y++)
        			if (x!=y)
        			if (st&(1<<y))
        				if (g[x][y]) w[st] = 0;
 }
}
            
void work() {
    f[0] = 0;
    for (int i=1;i<(1<<n);i++) f[i] = n;
    for (int i=1;i<(1<<n);i++) {
        for (int j=i;j>0;j=(j-1)&i) 
        	if (w[j])
        		if (f[i-j]+1<f[i]) f[i] = f[i-j]+1;
    }
    printf("%d\n", f[(1<<n)-1]);
}
           
int main() {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int ti=1;ti<=T;ti++) {
        printf("Case #%d: ", ti);
        fprintf(stderr,"Doing %d\n", ti);
        init();
        work();
    }
    return 0;
}
        
