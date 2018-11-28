#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>

#define rep(i, n) for (int i = 0; i < n; i++)
#define INT_INF 0x3f3f3f3f

using namespace std;

char words[5010][20];
int poss[100][30];

int main() {
	int L, D, N;
	scanf("%d %d %d", &L, &D, &N);
	
	rep(i, D) {
		scanf("%s", words[i]);
	}
	
	char pat[5000];
	rep(i, N) {
		scanf("%s", pat);

		memset(poss, 0, sizeof(poss));
		bool open = false;
		int patsize = 0;

		rep(j, strlen(pat)) {
			if (pat[j] == '(') open = true;
			else if (pat[j] == ')') {
				open = false;
				patsize++;
			}
			else {
				poss[patsize][pat[j]-'a'] = 1;

				if (!open) patsize++;
			}
		}
		
		int res = 0;
		rep(j, D) {
			if (patsize == L) {
				bool valid = true;

				rep(k, L) {
					if (!poss[k][words[j][k]-'a']) {
						valid = false;
						break;
					}
				}

				if (valid) res++;
			}
		}

		printf("Case #%d: %d\n", i+1, res);
	}
}

