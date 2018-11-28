#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;
char ulazni[] = "Awelcome to code jam";
char tren[1000];
int kol[20][2];

int main() {
	int n, ii, dul = strlen(ulazni);
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++) {
		cin.getline(tren, 1000);
		for (int j = 1; j < dul; j++) kol[j][0] = kol[j][1] = 0;
		kol[0][0] = kol[0][1] = 1; ii = 1;
		for (int j = 0; tren[j]; j++) {
			ii = 1-ii;
			for (int k = 1; k < dul; k++) {
				kol[k][ii] = kol[k][1-ii];
				if (ulazni[k] == tren[j]) kol[k][ii] = (kol[k][ii] + kol[k-1][1-ii]) % 1000;
			}
		}
		printf("Case #%d: %04d\n", i+1, kol[dul-1][ii]);
	}

	return 0;
}