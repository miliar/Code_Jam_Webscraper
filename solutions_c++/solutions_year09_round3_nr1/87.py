#include <cstdio>

using namespace std;
char value[250];
char ulaz[70];
int n;
long long sol;

int main() {
	scanf("%d", &n);
	for (int ii = 0; ii < n; ii++) {
		scanf("%s", ulaz);
		printf("Case #%d: ", ii+1);
		//if (ulaz[1] == 0) {printf("0\n"); continue;}
		long long base = 0;
		for (int i = 0; i < 250; i++) value[i] = 0;
		for (int i = 0; ulaz[i] != 0; i++) value[ ulaz[i] ] = 1;
		for (int i = 0; i < 250; i++) {base += value[i]; value[i] = -1;}
		value[ ulaz[0] ] = 1;
		if (base==1) base = 2;
		int tmp = 0;
		sol = 0;
		for (int i = 0; ulaz[i] != 0; i++) {
			if (value[ ulaz[i] ] == -1) {
				value[ ulaz[i] ] = tmp++;
				if (tmp == 1) tmp = 2;
			}
			sol = sol*base + value[ ulaz[i] ];
		}
		printf("%lld\n", sol);
	}

	return 0;
}