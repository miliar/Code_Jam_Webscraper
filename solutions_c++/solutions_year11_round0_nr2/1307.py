#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
char a[110], b[110];
int d[110][110], c[110][110];

void init() {
    memset(d, 0, sizeof(d));
    memset(c, 0, sizeof(c));
    scanf("%d", &n);
    for(int i=0; i<n; ++i) {
        scanf("%s", a);
        int x = a[0] - 'A';
        int y = a[1] - 'A';
        int z = a[2] - 'A';
        d[x][y] = d[y][x] = z;
    }
    scanf("%d", &n);
    for(int i=0; i<n; ++i) {
        scanf("%s", a);
        int x = a[0] - 'A';
        int y = a[1] - 'A';
        c[x][y] = c[y][x] = -1;
    }
}

void work() {
    scanf("%d%s", &n, a);
    int m = 0, x, y;
    for(int i=0; i<n; ++i) {
        if (0==m) {
            b[m++] = a[i];
            continue;
        }
        x = a[i] - 'A';
        y = b[m-1] - 'A';
        if (d[x][y] > 0) {
            b[m-1] = 'A' + d[x][y];
            continue;
        }
        x = a[i] - 'A';
        int ok = 0;
        for(int j=0; j<m; ++j) {
            y = b[j] - 'A';
            if (c[x][y] < 0) {
                m = 0;
                ok = 1;
                break;
            }
        }
        if (ok) continue;
        b[m++] = a[i];
    }
    printf("[");
    for(int i=0; i<m; ++i) {
        if (i) printf(", ");
        printf("%c", b[i]);
    }
    printf("]\n");
}


int main() {
    int Z;
    scanf("%d", &Z);
    for(int z=0; z<Z; ++z) {
        init();
        printf("Case #%d: ", z+1);
        work();
    }
    return 0;
}
