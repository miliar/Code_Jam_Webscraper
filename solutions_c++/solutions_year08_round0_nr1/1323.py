#include <string>
#include <cstdio>
using namespace std;

int main()
{
	int N;
	scanf("%d",&N);
	char tmp[150];
	for (int c = 0; c < N; ++c) {
		int S;
		scanf("%d",&S);
		gets(tmp);
		char str[100][150];
		for (int i = 0; i < S; ++i) {
			gets(str[i]);
		}

		int Q;
		scanf("%d", &Q);
		gets(tmp);
		int tab[1000];
		
		for (int i = 0; i < Q; ++i) {
			gets(tmp);
			for (int j = S; --j >= 0;) {
				if ( !strcmp(tmp, str[j]) ) {
					tab[i] = j;
				}
			}
		}

		int cnt = 0;
		int iter = 0;
		bool used[100];
		int numUsed;
		do {
			for (int i = S; --i >=0; )
				used[i] = false;
			numUsed = 0;

			while (iter < Q) {
				if (!used[tab[iter]]) {
					used[tab[iter]] = true;
					++numUsed;
					if (numUsed == S) {
						++cnt;
						break;
					}
				}
				++iter;
			}
		} while (iter < Q);

		printf("Case #%d: %d\n", c + 1, cnt);
	}
	return 0;
}

