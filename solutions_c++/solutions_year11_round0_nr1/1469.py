#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int max(int a, int b){
	if (a > b) return a;
	return b;
};

int solve(int ctry){
	int rez = 0, n, pos[2] = {1,1}, ts[2] = {0,0};
	scanf("%d ", &n);
	for (int i = 0; i < n; i++){
		char col;
		int dest;
		scanf("%c %d ", &col, &dest);
		col = (col == 'O')?0:1;
		ts[col] = 1 + max(ts[col] + abs(dest - pos[col]), ts[col^1]);
		pos[col] = dest;
	};
	rez = max(ts[0], ts[1]);
	printf("Case #%d: %d\n", ctry, rez);
	
};


int main(){

	if (freopen("test.in", "rt", stdin)){
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("A-small-attempt0.in", "rt", stdin)){
		freopen("A-small-attempt0.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("A-large.in", "rt", stdin)){
		freopen("A-large.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	return 0;
};
