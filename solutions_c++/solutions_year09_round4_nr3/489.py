/* 
 * File:   C.cc
 * Author: GongZhi
 * Problem:
 * Created on 2009年9月27日, 上午1:19
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;
#define V 60
/*
 *
 */
//最大团
//返回最大团大小和一个方案,传入图的大小n和邻接阵mat
//mat[i][j]为布尔量

#define MAXN 60

void clique(int n, int* u, int mat[][MAXN], int size, int& max, int& bb, int* res, int* rr, int* c) {
	int i, j, vn, v[MAXN];
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
	int max = 0, bb, c[MAXN], i, j;
	int vn, v[MAXN], rr[MAXN];
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
int data[V][V];
int g[V][V];
int ans[V][V];
int main() {
    int n,m;
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt10.out","w",stdout);
    int k, i, j;
    int kase, kases = 1;
    scanf("%d", &kase);
    while (kase--) {
        scanf("%d%d", &n, &m);
        memset(g, 0, sizeof (g));
        for (i = 0; i < n; i++)
            for (j = 0; j < m; j++)scanf("%d", &data[i][j]);
        for (i = 0; i < n; i++)
            for (j = 0; j < n; j++) {
                if (i == j)continue;
                for (k = 1; k < m; k++) {
                    if (data[i][k - 1] <= data[j][k - 1] && data[i][k] >= data[j][k])break;
                    if (data[i][k - 1] >= data[j][k - 1] && data[i][k] <= data[j][k])break;
                }
                if (k != m)g[i][j] = g[j][i] = 1;
            }
/*
        for (i = 0; i <= n; i++) {
            for (j = 0; j <= n; j++)printf("%d", g[i][j]);
            printf("\n");
        }
*/      int ret;
        printf("Case #%d: %d\n", kases++, maxclique(n,g,*ans));
    }
    return 0;
}

