#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int MOD = 10000;
const char *WELCOME = "welcome to code jam";
int PD[510][25];
char buf[510];

int main() {
	int N;
	scanf(" %d", &N);
	for (int _42=1; _42 <= N; _42++) {
		memset(PD, 0, sizeof(PD));
		scanf(" %[^\n]", buf);
		int sz = strlen(buf);

		PD[0][0] = 1;
		for (int k=1; k <= strlen(WELCOME); k++) {
			for (int i=1; i <= sz; i++) {
				if (WELCOME[k-1] == buf[i-1]) {
					for (int j=0; j < i; j++) {
						PD[i][k] += PD[j][k-1];
						PD[i][k] %= MOD;
					}
				}
			}
		}

		int ans=0;
		for (int i=0; i <= sz; i++) {
			ans += PD[i][strlen(WELCOME)];
			ans %= MOD;
		}
		printf("Case #%d: %04d\n", _42, ans);
	}

	return 0;
}
