#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int solve(int ctry){
	int N;
	scanf("%d", &N);
	unsigned added = 0, xored = 0, min_val = 0xFFFFFFFF;
	for (int i = 0; i < N; i++){
		unsigned val;
		scanf("%d", &val);
		if (val < min_val) min_val = val;
		xored ^= val;
		added += val;
	};
	if (xored)
		printf("Case #%d: NO\n", ctry);
	else 
		printf("Case #%u: %d\n", ctry, added - min_val);
	return 0;
};


int main(){

	if (freopen("test.in", "rt", stdin)){
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("C-small-attempt0.in", "rt", stdin)){
		freopen("C-small-attempt0.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("C-large.in", "rt", stdin)){
		freopen("C-large.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	return 0;
};

