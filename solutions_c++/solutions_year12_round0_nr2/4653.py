#include <stdio.h>
#include <string.h>
#include <memory.h>

int test;

int n, s, p;
int t[200];
int ans;
int f[200];
int q;

void Try0() {
	int i, j;
	int flag;
	for (i=1; i<=n; i++) {
		if (f[i]) continue;
		if (t[i] <= 2 && t[i] <= 28) continue; 
		flag = 0;
		for (j=p; j<=10; j++) {
			if (j + j + j == t[i]) flag = 1;
			if (j + j + j - 1 == t[i] && j - 1 >= 0) flag = 1;
			if (j + j + j - 2 == t[i] && j - 1 >= 0) flag = 1;	
		}
		if (flag) {
			f[i] = 1;
			ans++;
		}
		q--;
	}
}

void Try1() {
	int i, j;
	int flag;
	for (i=1; i<=n; i++) {
		if (f[i]) continue;
		flag = 0;
		for (j=p; j<=10; j++) {
			if (j + j + j == t[i]) flag = 1;
			if (j + j + j - 1 == t[i] && j - 1 >= 0) flag = 1;
			if (j + j + j - 2 == t[i] && j - 1 >= 0) flag = 1;	
		}
		if (flag) {
			f[i] = 1;
			q--;
			ans++;
			if (q == 0) return;
		}
	}
}

void Try2() {
	int i, j;
	int flag;
	if (s == 0) return;
	for (i=1; i<=n; i++) {
		if (f[i]) continue;
		flag = 0;
		for (j=p; j<=10; j++) {
			if (j + j + j - 2 == t[i] && j - 2 >= 0) flag = 1;
			if (j + j + j - 3 == t[i] && j - 2 >= 0) flag = 1;
			if (j + j + j - 4 == t[i] && j - 2 >= 0) flag = 1;
		}
		if (flag) {
			f[i] = 1;
			s--;
			ans++;
			if (s == 0) return;
		}
	}
}

int main() {              
	int i, j;
	scanf("%d ",&test);
	for (i=1; i<=test; i++) {
		scanf("%d %d %d", &n, &s, &p);
		for (j=1; j<=n; j++) {
			scanf("%d", &t[j]);
		}
		ans=0;     
		memset(f,0,sizeof(f));
		q = n - s;
		Try0();
		Try1();
		Try2();
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}                                                            