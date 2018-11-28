#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#define MAX 1010

int n;
int h1[MAX], h2[MAX];

void init(){
	memset(h1, 0, sizeof h1);
	memset(h2, 0, sizeof h2);
	scanf("%d", &n);

	for (int i = 0; i < n; i++){
		int a, b;
		scanf("%d %d", h1 + i, h2 + i);
	}
}
bool is_cross(int i, int j){
	//determine the seg_i cross seg_j
	if ((h1[i] < h1[j] && h2[i] < h2[j]) ||
		(h1[i] > h1[j] && h2[i] > h2[j]))
		return false;
	return true;
}

int solve(){
	int res = 0;
	for (int i = 0; i < n; i++)
		for (int j = i+1; j < n; j++){
			if (is_cross(i, j)) res++;
		}
	return res;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, cases = 1;
	scanf("%d", &t);
	while (cases <= t){
		int res;
		init();
		res = solve();
		printf("Case #%d: %d\n", cases++, res);
	}
	return 0;
}