#include <iostream>

char combine[257][257];
bool opposed[257][257];

int main()
{
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t,n;

	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		for (int j = 0; j < 257; j++)
			for (int k = 0; k < 257; k++) {
				combine[j][k] = 0;
				opposed[j][k] = false;
			}
		int d; 
		scanf("%d", &d);
		char s[200];
		for (int j = 0; j < d; j++) {
            scanf("%s", s);
			combine[s[0]][s[1]] = s[2];
			combine[s[1]][s[0]] = s[2];
		}
		scanf("%d", &d);
		for (int j = 0; j < d; j++) {
            scanf("%s", s);
			opposed[s[0]][s[1]] = true;
			opposed[s[1]][s[0]] = true;
		}
        scanf("%d", &d);
		scanf("%s", s);
		char res[200];
		int len;
		len  = 0;
		for (int j = 0; j < d; j++) {
			if (len > 0) {
				if (combine[res[len - 1]][s[j]] != 0) {
					res[len - 1] = combine[res[len - 1]][s[j]];
				} else {
					bool clear = false;
					for (int k = 0; k < len; k++)
						if (opposed[res[k]][s[j]]) clear = true;
					if (clear) len = 0;
					else {
						res[len] = s[j];
						len++;
					}
				} 
			} else {
				res[len] = s[j];
				len++;
			}
		}
		printf("Case #%d: [", i + 1);
		for (int i = 0; i < len; i++) {
            if (i > 0) printf(", ");
			printf("%c", res[i]);
		}
		printf("]\n");
	}
	return 0;
}