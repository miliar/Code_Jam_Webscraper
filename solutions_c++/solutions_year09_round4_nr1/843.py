#include <stdio.h>
#include <time.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <cassert>
using namespace std;

int N = 6;

int input[100];
int a[100];
int ans_slow, ans_fast;
int seen[999999];

void generate(void)
{
	for (int i = 0; i < N; i++) {
		input[i] = rand() % (i + 1);
	}
	random_shuffle(input, input + N);
}

bool solved(void)
{
	for (int i = 0; i < N; i++) if (a[i] > i) return false;
	return true;
}

int code_perm(void)
{
	int r = 0;
	for (int i = 0; i < N; i++) r = r * 6 + a[i];
	return r;
}

void bt(int level)
{
	if (level > ans_slow) return;
	if (solved()) {
		ans_slow = level;
		return;
	}
	int code = code_perm();
	if (seen[code]) return;
	seen[code] = 1;
	for (int i = 0; i < N - 1; i++)
	{
		swap(a[i], a[i + 1]);
		bt(level + 1);
		swap(a[i], a[i + 1]);
	}
	seen[code] = 0;
}

void solve_slow(void)
{
	memset(seen, 0, sizeof(seen));
	ans_slow = 9999;
	memcpy(a, input, sizeof(a));
	bt(0);
}

void solve_fast(void)
{
	ans_fast = 0;
	memcpy(a, input, sizeof(a));
	int i, j;
	i = 0;
	while (i < N) {
		while (i < N && a[i] <= i) i++;
		if (i >= N) break;
		j = i + 1;
		while (j < N && a[j] > i) j++;
		assert(j < N);
		for (int k = j - 1; k >= i; k--) {
			swap(a[k], a[k+1]);
			ans_fast++;
		}
	}
}

int xmain(void)
{
	srand(time(NULL));
	while (1) {
		generate();
		solve_slow();
		solve_fast();
		if (ans_slow != ans_fast) {
			printf("Error! %d vs %d\n", ans_slow, ans_fast);
			break;
		}
		else printf("OK. %d %d\n", ans_slow, ans_fast);
	}
	return 0;
}

int main(void)
{
	//freopen("/home/vesko/gcj/a.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 0; tc < T; tc++) {
		scanf("%d", &N);
		char s[200];
		for (int i = 0; i < N; i++) {
			input[i] = 0;
			scanf("%s", s); 
			for (int j = 0; j < N; j++)
				if (s[j] == '1') input[i] = j;
		}
		solve_fast();
		printf("Case #%d: %d\n", tc + 1, ans_fast);
	}
	return 0;
}

