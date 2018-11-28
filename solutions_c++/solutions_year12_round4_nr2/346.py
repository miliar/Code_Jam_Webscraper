#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

#define MAXN 2000

int n, test;
double x, y, w, l, height;
double r[MAXN], resx[MAXN], resy[MAXN];
int key[MAXN];

bool cmp(int a, int b) {
	return r[a] > r[b];
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &test);
	for (int t=1; t<=test; ++t){
		scanf("%d%lf%lf", &n, &w, &l);
		for (int i=0; i<n; ++i){
			scanf("%lf", &r[i]);
			key[i] = i;
		}
		sort(key, key+n, cmp);
		height = 0;
		x = -r[key[0]];
		y = -r[key[0]];
		for (int i=0; i<n; ++i){
			if (x + r[key[i]] > w + 1e-9){
				y += height;
				if (y<=0) y = r[key[0]];
				x = -r[key[i]];
				height = 0;
			}
			resx[key[i]] = max(0.0, x + r[key[i]]);
			resy[key[i]] = max(0.0, y + r[key[i]]);
			if (resx[key[i]] > w || resy[key[i]] > l){
				printf("FAIL ");
			}
			x = resx[key[i]] + r[key[i]];
			height = max(height, 2 * r[key[i]]);
		}
		printf("Case #%d:", t);
		for (int i=0; i<n; ++i)
			printf(" %.8lf %.8lf", resx[i], resy[i]);
		printf("\n");
	}
	return 0;
}