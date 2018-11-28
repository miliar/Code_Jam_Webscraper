#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 100

char seat[N][N];
int n, m, c[N][1024], mask[N];

int count_bits(int x)
{
	int r;
	for(r = 0; x > 0; r++, x^=x&(-x));
	return r;
}

bool can_place(int r, int v)
{
	if(mask[r-1] & v) return false;
	if((v&(v<<1)) || (v&(v>>1))) return false;
	else return true;
}

bool conflict(int vo, int vn)
{
	if((vn&(vo<<1)) || (vn&(vo>>1))) return true;
	else return false;
}

int main()
{
	int t, index;
	int i, j, k, ct, r;
	scanf("%d", &t);
	for(index = 1; index <= t; index++) {
		scanf("%d%d", &m, &n);
		for(i = 0; i < m; i++) {
			scanf("%s", seat[i]);
			mask[i] = 0;
			for(j = 0; j < n; j++)
				if(seat[i][j] == 'x')
					mask[i] |= 1<<j;
		}
		memset(c, -1, sizeof(c));
		c[0][0] = 0;
		for(i = 1; i <= m; i++) {
			for(j = 0; j < (1<<n); j++) {
				if(!can_place(i, j))
					continue;
 				c[i][j] = 0;
				ct = count_bits(j);
 				for(k = 0; k < (1<<n); k++) {
 					if(c[i-1][k]<0 || conflict(k, j))continue;
 					if(c[i-1][k]+ct > c[i][j])
 						c[i][j] = c[i-1][k] + ct;
 				}
			}
		}
		for(r = 0, i = 0; i < (1<<n); i++)
			if(c[m][i] > r)
				r = c[m][i];
		printf("Case #%d: %d\n", index, r);
	}
	return 0;
}

