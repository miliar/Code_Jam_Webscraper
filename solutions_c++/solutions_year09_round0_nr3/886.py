#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

const char text[] = "welcome to code jam";

char s[777];
char c[777];
int dp[777][55];

int nTC;

int main() {
	gets (s);
	sscanf (s, "%d", &nTC);
	
	for (int tc = 1; tc <= nTC; tc++) {
		gets (s);
		memset (dp, 0, sizeof (dp));
		dp[0][0] = 1;
		for (int i = 0; s[i]; i++)
			dp[i + 1][0] = 1;
		for (int i = 0; s[i]; i++) {
			for (int j = 0; text[j]; j++) {
				if (s[i] == text[j]) {/*
					printf ("(%d dan %d)\n", i, j);
					printf ("dp[%d][%d] += dp[%d][%d] (%d)\n", i + 1, j + 1, i + 1 - 1, j + 1 - 1, dp[i + 1 - 1][j + 1 - 1]);*/
					dp[i + 1][j + 1] += dp[i + 1 - 1][j + 1 - 1];
					dp[i + 1][j + 1] %= 10000;
				}
				dp[i + 1][j + 1] += dp[i + 1 - 1][j + 1];
				dp[i + 1][j + 1] %= 10000;
			}
		}
		/*
		for (int i = 0; s[i]; i++) {
			for (int j = 0; text[j]; j++) {
				printf ("%d ", dp[i + 1][j + 1]);
			}
			printf ("\n");
		}*/
		
		sprintf (c, "%d", dp[strlen (s)][strlen (text)]);
		
		string hasil = c;
		while (hasil.length() < 4)
			hasil = '0' + hasil;
		printf ("Case #%d: ", tc);
		puts (hasil.c_str());
	}
	
	return 0;
}
