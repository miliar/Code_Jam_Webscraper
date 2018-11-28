#include <cstdio>
#include <cstring>

int main()
{
	int testCases, n;
	char text[205], transTable[36][36];
	bool clearTable[36][36];

	scanf("%d", &testCases);
	for (int t = 1; t <= testCases; ++ t) {
		memset(transTable, 0, sizeof(transTable));
		memset(clearTable, 0, sizeof(clearTable));

		scanf("%d", &n);
		while (n--) {
			scanf("%s", text);
			transTable[text[0] - 'A'][text[1] - 'A'] = text[2];
			transTable[text[1] - 'A'][text[0] - 'A'] = text[2];
		}

		scanf("%d", &n);
		while (n--) {
			scanf("%s", text);
			clearTable[text[0] - 'A'][text[1] - 'A'] = true;
			clearTable[text[1] - 'A'][text[0] - 'A'] = true;
		}

		scanf("%d", &n);
		scanf("%s", text);

		int len = 0;
		char result[205];
		for (int k = 0; k < n; ++ k) {
			if (len && transTable[text[k] - 'A'][result[len - 1] - 'A']) {
				result[len - 1] = transTable[text[k] - 'A'][result[len - 1] - 'A'];
			} else {
				bool clear = false;
				for (int i = 0; !clear && i < len; ++ i)
					clear = clearTable[text[k] - 'A'][result[i] - 'A'];
				if (clear) {
					len = 0;
				} else {
					result[len ++] = text[k];
				}
			}
		}

		printf("Case #%d: [", t);
		if (len) printf("%c", result[0]);
		for (int i = 1; i < len; ++ i)
			printf(", %c", result[i]);
		printf("]\n");
	}
	return 0;
}
