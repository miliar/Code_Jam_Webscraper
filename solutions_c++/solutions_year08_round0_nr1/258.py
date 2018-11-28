#include<stdio.h>
#include<string.h>

#include<map>
#include<string>
using namespace std;

typedef unsigned nat;
typedef unsigned char nat8;
typedef unsigned short nat16;

typedef nat8 eng_t;
typedef nat16 count_t;

#define INFINITY 1000000000
#define N_SIZE 128
#define Q_SIZE 1024

char line[4096];

count_t S[N_SIZE][Q_SIZE];
eng_t Q[Q_SIZE];

int main() {
	nat tc, cs, n, q, i, j, k, x, mn;

	scanf("%[^\n]\n", line);
	sscanf(line, "%u", &tc);
	for (cs = 0; cs != tc; ++cs) {
		scanf("%[^\n]\n", line);
		sscanf(line, "%u", &n);

		{
			map<string, nat> keys;
			for (i = 0; i != n; ++i) {
				scanf("%[^\n]\n", line);
				string s(line, line+strlen(line));
				keys[s] = i;
			}

			scanf("%[^\n]\n", line);
			sscanf(line, "%u", &q);
			for (i = 0; i != q; ++i) {
				scanf("%[^\n]\n", line);
				string s(line, line+strlen(line));
				if (keys.find(s) == keys.end())
					Q[i] = n;
				else
					Q[i] = keys[s];
			}
		}

		for (i = 0; i != n; ++i)
			S[i][q] = 0;

		for (j = q; j != 0;) {
			--j;
			for (i = 0; i != n; ++i) {
				if (Q[j] == i) {
					mn = INFINITY;
					for (k = 0; k != n; ++k)
						if (k != i) {
							x = S[k][j+1];
							if (x < mn)
								mn = x;
						}
					S[i][j] = 1+mn;
				}
				else
					S[i][j] = S[i][j+1];
			}
		}

		mn = INFINITY;
		for (i = 0; i != n; ++i) {
			x = S[i][0];
			if (x < mn)
				mn = x;
		}

		printf("Case #%u: %u\n", cs+1, mn);
	}

	return 0;
}


