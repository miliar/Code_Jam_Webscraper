#include <cstdio>
#include <cctype>
#include <string>

#define count Count

using namespace std;

const int maxp = 100;
const int maxn = 100;
const int cmod = 10009;
const int maxc = 26;
const int maxk = 100;

string poly[maxp];
char str[1000];
int count[maxn][maxc];
int P, n, K;
int res[maxk], sum[maxk][100];

void Deal_With(const string &str) {
	//printf("str = %s\n", str.c_str());
	int d = str.length();
	int full = 1 << d;
	//printf("d = %d\n", d);
	int t, i, j, k, l, product;
	for (i = 0; i < full; i++)
		sum[0][i] = 0;
	sum[0][0] = 1;
	for (i = 0; i < K; i++) {
		for (j = 0; j < full; j++) {
			sum[i + 1][j] = 0;
			for (t = 0; t < n; t++)
				for (k = 0; k <= j; k++)
					if ((k & j) == k) {
						product = 1;
						for (l = 0; l < d; l++)
							if (!((1 << l) & k) && ((1 << l) & j)) (product *= count[t][str[l] - 'a']) %= cmod;
						(sum[i + 1][j] += product * (sum[i][k] % cmod)) %= cmod;
					}
			//printf("sum[%d][%d] = %d\n", i + 1, j, sum[i + 1][j]);
		}
	}
	//printf("%d\n", sum[1][full - 1]);
	for (i = 1; i <= K; i++)
		(res[i] += sum[i][full - 1]) %= cmod;
}

void Solve() {
	scanf("%s", str);
	P = 0;
	int i, j;
	string curr = "";
	for (i = 0; str[i]; i++)
		if (isalpha(str[i])) curr = curr + str[i];
		else {
			poly[P++] = curr;
			curr = "";
		}
	if (curr.length()) poly[P++] = curr;
	scanf("%d %d", &K, &n);
	for (i = 0; i < n; i++) {
		scanf("%s", str);
		for (j = 0; j < maxc; j++)
			count[i][j] = 0;
		for (j = 0; str[j]; j++)
			count[i][str[j] - 'a']++;
	}
	for (i = 0; i <= K; i++)
		res[i] = 0;
	for (i = 0; i < P; i++)
		Deal_With(poly[i]);
	for (i = 1; i <= K; i++)
		printf(" %d", res[i]);
	printf("\n");
}

int main() {
	int t, i;
	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		printf("Case #%d:", i);
		Solve();
	}
	return 0;
}
