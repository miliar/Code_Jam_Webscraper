#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int len, ndict, nTC;

char dict[5005][18];
char s[5005];
bool can[18][255];

int main() {
	scanf ("%d%d%d", &len, &ndict, &nTC);
	
	for (int i = 0; i < ndict; i++) {
		scanf ("%s", dict[i]);
	}
	
	for (int tc = 1; tc <= nTC; tc++) {
		scanf ("%s", s);
		memset (can, 0, sizeof (can));
		for (int i = 0, x = 0; s[i]; i++) {
			if (s[i] == '(') {
				i++;
				while (s[i] != ')') {
					can[x][s[i]] = true;
					i++;
				}
			} else
				can[x][s[i]] = true;
			x++;
		}
		
		int ctr = 0;
		
		for (int i = 0; i < ndict; i++) {
			int plus = 1;
			for (int j = 0; dict[i][j]; j++)
				if (!can[j][dict[i][j]])
					plus = 0;
			ctr += plus;
		}
		
		printf ("Case #%d: %d\n", tc, ctr);
	}
	
	return 0;
}
