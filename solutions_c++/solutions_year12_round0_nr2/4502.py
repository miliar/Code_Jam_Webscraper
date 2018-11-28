#include <stdlib.h>
#include <stdio.h>

int max(int a, int b) {
	if (a > b) return a;
	return b;
};

int min(int a, int b) {
	if (a < b) return a;
	return b;
};



int solve(int ctry){
	int n, s, p, scores[100];
	scanf("%d %d %d", &n, &s, &p);
	for (int i = 0; i < n; i++)
		scanf("%d", scores + i);
	
	// counting good ones and those that would need a "boost"
	int cnt_ok = 0, cnt_boost = 0, lim_ok = max(p*3-2, 0), lim_boost = max(p*3-4, 0);
	for (int i = 0; i < n; i++) {
		if (scores[i] >= lim_ok) {
			cnt_ok++;
			continue;
		};
		if (scores[i] >= lim_boost && (scores[i] >= 2))
			cnt_boost++;
	};
					
	printf("Case #%d: %d\n", ctry, cnt_ok + min(cnt_boost, s));
};


int main(){

	if (freopen("test.in", "rt", stdin)){
//		freopen("A-large-practice.out", "wt", stdout);
		int tries = 0;
		char c;
		scanf("%d%c", &tries, &c);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("B-small-attempt0.in", "rt", stdin)){
		freopen("B-small-attempt0.out", "wt", stdout);
		int tries = 0;
		char c;
		scanf("%d%c", &tries, &c);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("B-large.in", "rt", stdin)){
		freopen("B-large.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	return 0;
};