#include <stdio.h>
#include <memory.h>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
	char m[30] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u',
     'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	char c1[120];
	char c2[120];
	int cases;
	char c;
	scanf("%d%c", &cases, &c);
	for (int p = 1; p <= cases; p++) {
		gets(c1);
		for (int i = 0; i < strlen(c1); i++) {
			if (c1[i] != ' ') c2[i] = m[c1[i] - 'a'];
			else c2[i] = c1[i];
		}
		printf("Case #%d: ", p);
        for (int i = 0; i < strlen(c1); i++)
			printf("%c", c2[i]);
		printf("\n");
	}
	return 0;
}
	
