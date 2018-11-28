#include <cstdio>
#include <vector>
#include <string>

using namespace std;

const int MAX_L = 16;

int L, D, N;
vector<string> dict;

int main()
{
	// freopen("input.txt", "rt", stdin);
	scanf("%d %d %d\n", &L, &D, &N);
	for (int i = 0; i < D; i++) {
		static char line[1024];
		gets(line);
		dict.push_back(line);
	}

	for (int i = 0; i < N; i++) {
		static char line[102400];
		gets(line);

		vector<bool> can_be[MAX_L];
		int start = 0;
		for (int j = 0; j < L; j++) {
			can_be[j] = vector<bool>(26, false);
			if (line[start] == '(') {
				start++;
				while (line[start] != ')')
					can_be[j][ line[start++]-'a' ] = true;
			} else
				can_be[j][ line[start]-'a' ] = true;

			start++;
		}

		int res = 0;
		for (int j = 0; j < D; j++) {
			bool ok = true;
			string &w = dict[j];
			for (int k = 0; k < L; k++)
				if (!can_be[k][ w[k]-'a' ]) {
					ok = false;
					break;
				}
			if (ok)
				res++;
		}

		printf("Case #%d: %d\n", i+1, res);
	}

	return 0;
}
