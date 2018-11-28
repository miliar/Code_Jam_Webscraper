// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

const int MAXN = 200;

int k, map[MAXN][MAXN], l[MAXN], s[MAXN];
bool h[MAXN], z[MAXN];

void init()
{
	int i, j, p = 0;

	scanf("%d", &k);
	for (i=1; i<=k; i++){
		for (j=1; j<=i; j++)
			scanf("%d", &map[i][j*2-1]);
		p++;
		l[p] = 2*i-1;
		s[p] = k+1-i;
	}
	for (i=k-1; i>=1; i--){
		for (j=1; j<=i; j++)
			scanf("%d", &map[k+k-i][j*2-1]);
		p++;
		l[p] = 2*i-1;
		s[p] = k+1-i;
	}
	
}

void work()
{
	int i, j, v, u, stv, stu, best, now, k1, line;

	memset(h, false, sizeof(h));
	memset(z, false, sizeof(h));
	for (i=1; i<=k+k-1; i++){
		h[i] = true;
		v = i-1;
		u = i+1;
		while (v>=1 && u<=k+k-1){
			if (s[v]<s[u]){
				stv = 1+s[u]-s[v];
				stu = 1;
			}
			else
			{
				stv = 1;
				stu = 1+s[v]-s[u];
			}
			while (stv<=l[v] && stu<=l[u]){
				if (map[v][stv]!=map[u][stu]){
					//printf("(%d %d, %d %d)", v, stv, u, stu);
					h[i] = false;
					break;
				}
				stv++;
				stu++;
			}
			if (!h[i]) break;
			v--;
			u++;
		}
		//printf("%d ", h[i]);
	}
	//printf("\n");

	for (i=1; i<=k+k-1; i++){
		z[i] = true;
		v = i-1;
		u = i+1;
		while (v>=1 && u<=k+k-1){
			if (s[v]<s[u]){
				line = s[u];
			}
			else
			{
				line = s[v];
			}
			stv = v-s[line]+1;
			stu = u-s[line]+1;
			//printf("%d->%d %d %d %d|||\n", i, line, s[line], stv, stu);
			while (stv>=1 && stv<=l[line] && stu>=1 && stu<=l[line]){
			//	printf("[%d %d, %d %d]", line, stv, line, stu);
				if (map[line][stv]!=map[line][stu]){
					//printf("(%d %d, %d %d)", stv, v, stu, u);
					z[i] = false;
					break;
				}
				line++;
				stv = v-s[line]+1;
				stu = u-s[line]+1;
			
			}
			if (!z[i]) break;
			v--;
			u++;
		}
		//printf("%d ", z[i]);
	}
	//printf("\n");

	best = -1;
	for (i=1; i<=k+k-1; i++)
		if (h[i])
			for (j=1; j<=k+k-1; j++)
				if (z[j]){
					k1 = abs(i-k)+abs(j-k)+k;
					now = (k1+1)*k1 - k1;
					if (best==-1 || best>now)
						best = now;
				}
	printf("%d\n", best-(k+1)*k+k);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i=0, t;
	scanf("%d", &t);
	while (t--){
		i++;
		printf("Case #%d: ", i);
		init();
		work();
	}

	return 0;
}