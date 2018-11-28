#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long long int64;

char cipher[65];
bool existed[128];

int64 calc(int digit[], int nbit, int base) {
	int64 res = 0;
	for (int i = 0; i < nbit; i++) {
		res = res * base + digit[i];
	}

	return res;
}//calc

void solve() {
	int base = 0;
	int len = strlen(cipher);

	memset(existed, false, sizeof(existed));
	for (int i = 0; cipher[i]; i++) {
		if (!existed[ cipher[i] ]) {
			base++;
			existed[ cipher[i] ] = true;
		}
	}

	int digit[65];
	memset(digit, -1, sizeof(digit[0]) * len);
	char ch = cipher[0];
	for (int i = 0; i < len; i++) {
		if (cipher[i] == ch) digit[i] = 1;
	}

	int j = 0;
	while (j < len && cipher[j] == cipher[0]) j++;
	ch = cipher[j];
	for (int i = j; i < len; i++) {
		if (cipher[i] == ch) digit[i] = 0;
	}
	for (int b = 2; b < base; b++) {
		j = 0;
		while (j < len && digit[j] != -1) j++;
		ch = cipher[j];
		for (int i = j; i < len; i++) {
			if (cipher[i] == ch) digit[i] = b;
		}
	}

	if (base == 1) base = 2;
	cout << calc(digit, len, base) << endl;
}//solve

int main() {
	int nCase;

	scanf("%d", &nCase);
	for (int t = 1; t <= nCase; t++) {
		scanf(" %s", cipher);

		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}
