#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cctype>
#include <stack>
using namespace std;

typedef long long int int64;

#define EPS 10e-9
#define INF 0x3f3f3f3f
#define MAXN 1500

int v[MAXN];

int res[MAXN][2];

int n, m;
int num;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int64 sqr(int64 x) {
	return	x * x;
}

int64 dist(int a, int b) {
	return sqr((int64) res[a][0] - (int64) res[b][0]) + sqr((int64) res[a][1] - (int64) res[b][1]); 	
}

bool tenta(int a, int b) {
	int x, y;
	for (int k = 0; k < 4; k++) {
		x = res[b][0] + dx[k] * (v[b] + v[a]);
		y = res[b][1] + dy[k] * (v[b] + v[a]);
		if (x < 0 || x > n || y < 0 || y > m) {
			continue;	
		}
		res[a][0] = x;
		res[a][1] = y;
		bool erro = false;
		for (int i = a+1; i < num; i++) {
			if (i == b) continue;
			if (dist(a, i) < sqr((int64) v[a] + (int64) v[i])) {
				erro = true;
				break;
			}
		}
		if (!erro) return true;
	}
	return false;	
}

int main()
{	
	int t;
	scanf("%d", &t);
	for (int k = 0; k < t; k++) {
		scanf("%d", &num);
		scanf("%d %d", &n, &m);
		for (int i = 0; i < num; i++) {
			scanf("%d", &v[i]);	
		}
		//sort(v, v + num);
		res[0][0] = 0;
		res[0][1] = 0;
		for (int i = num-2; i >= 0; i--) {
			bool erro = true;
			for (int j = i + 1; j < num; j++) {
				if (tenta(i, j)) {
					//printf("%d %d\n", i, j);
					erro = false;
					break;
				}
			}
			/*if (erro) {
				printf("%d\n", k+1);	
			}*/
		}
		
		/*for (int i = 0; i < num; i++) {
			for (int j = i+1; j < num; j++) {
				if (dist(i, j) < sqr((int64) v[i] + (int64) v[j])) {
					printf("%d\n", k+1);	
				}	
			}	
		}*/
		
		printf("Case #%d:", k+1);
		for (int i = 0; i < num; i++) {
			printf(" %d %d", res[i][0], res[i][1]);	
		}
		printf("\n");
	}	
	return 0;
}