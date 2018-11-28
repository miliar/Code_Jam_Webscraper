#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int func(int N, int S, int p, int *t)
{
	int y = 0;
	int i;
	int p0;
	int p1;
	int p2;

	p0 = p;
	p1 = p - 1;
	if(p1 < 0) {
		p1 = 0;
	}
	p2 = p - 2;
	if(p2 < 0) {
		p2 = 0;
	}

	for(i = 0; i < N; i++) {
		if(t[i] >= p0 + p1 * 2) {
			y++;
		} else if(t[i] >= p0 + p2 * 2) {
			if(S) {
				y++;
				S--;
			}
		}

	}

	return y;
}


int main(int argc, char *argv[])
{
	char line[512];
	char *s;
	int T = -1;
	int n = 0;

	while((s = fgets(line, sizeof(line), stdin)) != NULL) {
		int N;
		int S;
		int p;
		int t[100];
		int i;
		int y = 0;

		if(T < 0) {
			T = atoi(line);
			continue;
		}

		sscanf(s, "%d", &N);

		s = strchr(s, ' ');
		if(s == NULL) {
			fprintf(stderr, "error %d\n", __LINE__);
			break;
		}
		s++;
		sscanf(s, "%d", &S);

		s = strchr(s, ' ');
		if(s == NULL) {
			fprintf(stderr, "error %d\n", __LINE__);
			break;
		}
		s++;
		sscanf(s, "%d", &p);

		for(i = 0; i < N; i++) {
			s = strchr(s, ' ');
			if(s == NULL) {
				fprintf(stderr, "error %d(%d:%d/%d:%d)\n", __LINE__, n, i, N, t[i - 2]);
				break;
			}
			s++;
			sscanf(s, "%d", &t[i]);
		}
		if(i != N) {
			break;
		}

		y = func(N, S, p, t);
		n++;

		printf("Case #%d: %d\n", n, y);

		if(n >= T) {
			break;
		}
	}

	return 0;
}
