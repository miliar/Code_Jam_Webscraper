#include<algorithm>
#include<cstdio>
#include<algorithm>

using namespace std;

int testcases;

int K, len;

char str[2000], backup[2000];

int ans;

bool used[100];

int order[100];

void solve(int);

int main() {
	
	FILE *fin = fopen("D-small-attempt0.in", "r");
	
	FILE *fout = fopen("D-small-attempt0.out", "w");
	
	fscanf(fin, "%d", &testcases);
	
	for (int cases = 1; cases <= testcases; cases++) {
		
		fscanf(fin, "%d", &K);
		
		fscanf(fin, "%s", str + 1);
		
		strcpy(backup + 1, str + 1);
		
		len = strlen(str + 1);
		
		ans = (int) 2e9;
		
		memset(used, 0, sizeof used);
		
		solve(1);
		
		fprintf(fout, "Case #%d: %d\n", cases, ans);
	}
	
	return 0;
}

void solve(int depth) {
	
	if (depth > K) {
		
		for (int turn = 1; turn <= len / K; turn++) {
			
			int start = K * (turn -1);
			
			for (int i = 1; i <= K; i++) str[start + i] = backup[start + order[i]];
		}
		
		int tmp = 0;
		
		for (int i = 1; i <= len; i++) if (i == 1 || str[i] != str[i - 1]) ++tmp;
		
		if (tmp < ans) ans = tmp;
		
		return;
	}
	
	for (int i = 1; i <= K; i++) if (!used[i]) {
		
		order[depth] = i;
		
		used[i] = true;
		
		solve(depth + 1);
		
		used[i] = false;
	}
}
