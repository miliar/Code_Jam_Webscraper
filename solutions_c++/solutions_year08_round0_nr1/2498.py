#include <stdio.h>
#include <map>
#include <string>

using namespace std;

void run(int numb) {
	int s, q;
	//map<string, int> a;
	scanf("%d\n", &s);
	string ss[101];
	for (int i = 0; i < s; i++) {
		string str = "";
		char c;
		while (true) {
			scanf("%c", &c);
			if (c == 10) {
				break;
			}
			if (c == 13) continue;
			//printf("%c", c);
			str = str+c;
			//a[str]
		}

		ss[i] = str;
	}
	string qq[1001];
	scanf("%d\n", &q);
	for (int i = 0; i < q; i++) {
		string str = "";
		char c;
		while (scanf("%c", &c) > 0) {
			if (c == 10) break;
			if (c == 13) continue;
			str = str+c;
			//printf("%c", c);
			//a[str]
		}
		qq[i] = str;
	}
	int f[101][1001];
	for (int i = 0; i < s; i++) {
		if (ss[i] != qq[0]) f[i][0] = 0;
		else f[i][0] = 2000000001;
	}
	for (int i = 1; i < q; i++) {
		for (int t = 0; t < s; t++) {
			int min = 2000000000;
			if (ss[t] == qq[i]) {
				f[t][i] = min+1;
				continue;
		  }
			for (int j = 0; j < s; j++) {
				min = (min > (f[j][i-1]+((t != j) ? 1 : 0))) ? (f[j][i-1]+((t != j) ? 1 : 0) ): min;
			}
			f[t][i] = min;

			/** for (int ii = 0; ii < s; ii++) {
				for (int jj = 0; jj < q; jj++) {
					printf("%d   ", f[ii][jj]);	
				}
				printf("\n");
			}
			printf("\n"); */
    }
	}
	int min = 2000000000;
	for (int i = 0; i < s; i++) {
		min = (min > f[i][q-1]) ? f[i][q-1] : min;
	}
	printf("Case #%d: %d\n", numb, min);
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		run(i+1);
	}

	return 0;
}
