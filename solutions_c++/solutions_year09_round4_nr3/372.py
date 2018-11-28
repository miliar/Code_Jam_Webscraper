#include <stdio.h>

const int MAXN = 100 + 10;
const int maxk = 25 + 10;

int p[MAXN][maxk], mat[MAXN][MAXN], tmp[MAXN], n, k;

void clique(int n, int* u, int mat[][MAXN], int size, int& max, int& bb, int* res, int* rr, int* c) {
	int i, j, vn, v[MAXN] = {0};
	if (n) {
		if (size + c[u[0]] <= max) return;
		for (i = 0; i < n + size - max && i < n; ++ i) {
			for (j = i + 1, vn = 0; j < n; ++ j)
				if (mat[u[i]][u[j]])
					v[vn ++] = u[j];
			rr[size] = u[i];
			clique(vn, v, mat, size + 1, max, bb, res, rr, c);
			if (bb) return;
		}
	} else if (size > max) {
		max = size;
		for (i = 0; i < size; ++ i)
			res[i] = rr[i];
		bb = 1;
	}
}

int maxclique(int n, int mat[][MAXN], int *ret) {
	int max = 0, bb, c[MAXN] = {0}, i, j;
	int vn, v[MAXN] = {0}, rr[MAXN] = {0};
	for (c[i = n - 1] = 0; i >= 0; -- i) {
		for (vn = 0, j = i + 1; j < n; ++ j)
			if (mat[i][j])
				v[vn ++] = j;
		bb = 0;
		rr[0] = i;
		clique(vn, v, mat, 1, max, bb, ret, rr, c);
		c[i] = max;
	}
	return max;
}

int main(void)
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    
    int tot;
    scanf("%d", &tot);
    for (int cas = 1; cas <= tot; ++cas) {
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; ++i)
        for (int j = 0; j < k; ++j)
            scanf("%d", &p[i][j]);
        
        for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) if (i != j) {
            mat[i][j] = 0;
            
            for (int t = 0; t < k; ++t)
                if (p[i][t] == p[j][t]) mat[i][j] = 1;
            
            if (mat[i][j]) continue;
            
            for (int t = 0; t+1 < k; ++t) {
                if (p[i][t]<p[j][t] && p[i][t+1]>p[j][t+1]) mat[i][j] = 1;
                if (p[i][t]>p[j][t] && p[i][t+1]<p[j][t+1]) mat[i][j] = 1;
            }
        }
        
        int res;
        res = maxclique(n, mat, tmp);
        printf("Case #%d: %d\n", cas, res);
    }
    return 0;
}
