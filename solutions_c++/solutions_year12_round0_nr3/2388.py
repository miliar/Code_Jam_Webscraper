#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdio.h>

#include <map>

using namespace std;

#define MAX_LINE 1024

#define RN(v) \
({ \
	char line[MAX_LINE]; \
	RL(line); \
	sscanf(line, "%d", &v); \
})

#define RNN(v, n, line) \
({ \
	int i; \
	char *s = line; \
	char *e; \
	for (i = 0; i < n; i++) { \
		v[i] = strtol(s, &e, 10); \
		s = e; \
	} \
	i; \
})

#define RL(line) \
({ \
	int size = -1; \
	if (fgets(line, sizeof(line), stdin)) {; \
		size = strlen(line) - 1; \
		line[size] = 0; \
	} \
	size; \
})

typedef multimap<int, int> recmap;
//typedef map<int, int> cntmap;

int
recycle(int x, int min, int max, recmap& rec)
{
	if (x <= 11) {
		return 0;
	}

	char str[8+7+30];
	int size = sprintf(str, "%d", x);
	
	int cnt = 0;
	for (int mov = 1; mov < size; mov++) {
		memset(str+size, 0, sizeof(str)-size);
		for (int i = 0; i < size; i++) {
			for (int j = 0; j < mov; j++) {
				str[i+size+j] = str[i+j];
			}

			if (str[i+mov] != '0') {
				int m = atoi(str+(i+mov));
				if (x < m && m <= max) {
					pair<recmap::const_iterator, recmap::const_iterator> pit;
					pit = rec.equal_range(x);
					bool found = false;
					for (; pit.first != pit.second; ++pit.first) {
						if (pit.first->second == m) {
							found = true;
							break;
						}
					}
					if (!found) {
						cnt++;
						rec.insert(pair<int, int>(x, m));
					}
				}
			}
		}
	}

	return cnt;
}

recmap rec;
int
foo(int *G, int size)
{
	int x = 0;
	rec.clear();
	for (int i = G[0]; i <= G[1]; i++) {
		x += recycle(i, G[0], G[1], rec);
	}
	return x;
}

int
main(int argc, char *argv[])
{
	char buff[MAX_LINE];

	int T; // # of test cases
	RN(T);

	for (int i = 0; i < T; i++) {
		RL(buff);
		int G[2];
		RNN(G, 2, buff);

		int x = foo(G, 2);
//printf(">> %d, %d\n", G[0], G[1]);
		printf("Case #%d: %d\n", i + 1, x);
	}
	return 0;
}

