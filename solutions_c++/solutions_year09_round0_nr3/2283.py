#include <cstdio>
#include <cstring>
#include <iostream>

int dp[530][25];

const char *string = "welcome to code jam";
char line[533];

int main(int argc, char **argv) {
	int T;
	scanf("%d", &T);
	fgets(line, 530, stdin);
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		fgets(line, 530, stdin);
		dp[0][0] = 1;
		for (int k = 0; string[k] != 0; ++k) {
			dp[0][k+1] = 0;
		}
		for (int j = 0; line[j] != 0; ++j) {
			dp[j+1][0] = 1;
			for (int k = 0; string[k] != 0; ++k) {
				dp[j+1][k+1] = dp[j][k+1];
				if (string[k] == line[j]) {
					// std::cerr << "found " << k << " at pos " << j << std::endl;
					dp[j+1][k+1] += dp[j][k];
				}
				dp[j+1][k+1] %= 10000;
			}
			/*
			std::cerr << "pos " << j << ": " << dp[j+1][0];
			for (int k = 0; string[k] != 0; ++k) {
				std::cerr << " " << dp[j+1][k+1];
			}
			std::cerr << std::endl;
			*/
		}
		printf("%04d\n", dp[strlen(line)][strlen(string)]);
	}
}
