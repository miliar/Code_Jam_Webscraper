#include <cstdio>
#include <map>
#include <string>
#include <vector>
using namespace std;

#define CODE A-large

#define INPUT QUOTE(CODE)".in"
#define OUTPUT QUOTE(CODE)".out"
#define _QUOTE(x) #x
#define QUOTE(x) _QUOTE(x)

#define MAXK 60

int k;
char diam[2*MAXK][2*MAXK];

void read() {
	scanf("%d%*[\n]", &k);
	for (int i = 0; i < 2 * k - 1; ++i)
		scanf("%[^\n]%*[\n]", diam[i]);
	
}

bool versym(int i) {
	for (int j = 0; diam[i][j]; ++j) {
		for (int a = i - 1, b = i + 1; a >= 0 && b < 2 * k - 1 && diam[a][j] && diam[b][j]; --a, ++b)
			if (diam[a][j] != ' ' && diam[b][j] != ' ' && diam[a][j] != diam[b][j])
				return false;
	}
	return true;
}

bool horsym(int j) {
	for (int i = k - 1; i >= 0 && diam[i][j]; --i) {
		for (int a = j - 1, b = j + 1; a >= 0 && diam[i][b]; --a, ++b)
			if (diam[i][a] != ' ' && diam[i][b] != ' ' && diam[i][a] != diam[i][b])
				return false;
	}
	for (int i = k - 1; i < 2 * k - 1 && diam[i][j]; ++i) {
		for (int a = j - 1, b = j + 1; a >= 0 && diam[i][b]; --a, ++b)
			if (diam[i][a] != ' ' && diam[i][b] != ' ' && diam[i][a] != diam[i][b])
				return false;
	}
	return true;
}

int solve() {
	read();
	int v = MAXK, h = MAXK;
	for (int i = 0; i < 2 * k - 1; ++i) {
		if (versym(i) && v > abs(k - 1 - i))
			v = abs(k - 1 - i);
	}
	for (int j = 0; j < 2 * k - 1; ++ j) {
		if (horsym(j) && h > abs(k - 1 - j))
			h = abs(k - 1 - j);
	}
	//printf("%d %d\n", h, v);
	int nk = k + h + v;
	return nk * nk - k * k;
}

int main() {
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i) {
		printf("Case #%d: %d\n", i, solve());
	}
	return 0;
}
