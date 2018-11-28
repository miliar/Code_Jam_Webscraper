#include <stdio.h>
#include <list>

using namespace std;

int main() {

	int T;

	scanf("%d", &T);

	for (int t = 1; t <= T; t++) {
		char lookup[26][26];
		list<char> conflicts[26];
		int count[26];
		for (int i = 0; i < 26; i++) {
			for (int j = 0; j < 26; j++) {
				lookup[i][j] = 0;
			}
			count[i] = 0;
		}

		int C,D,N;
		scanf("%d", &C);
		for (int i = 0; i < C; i++) {
			char in[4];
			scanf("%s", in);
			lookup[in[0]-'A'][in[1]-'A'] = in[2];
			lookup[in[1]-'A'][in[0]-'A'] = in[2];
		}

		scanf("%d", &D);
		for (int i = 0; i < D; i++) {
			char in[3];
			scanf("%s", in);
			conflicts[in[0]-'A'].push_back(in[1]);
			conflicts[in[1]-'A'].push_back(in[0]);
		}

		char invoke[101];
		scanf("%d", &N);
		scanf("%s", invoke);

		int len = 0;
		char result[101];

		for (int i = 0; i < N; i++) {
			result[len] = invoke[i];
			len++;

			if (len >= 2) {
				char found = lookup[result[len - 1] - 'A'][result[len - 2] - 'A'];
				if (found != 0) {
					count[result[len - 1]-'A']--;
					count[result[len - 2]-'A']--;
					result[len - 2] = found;
					len--;
				}
				count[result[len - 1]-'A']++;

				list<char>* conflict = &conflicts[result[len-1]-'A'];
				for (list<char>::iterator iter = conflict->begin(); iter != conflict->end(); iter++) {
					if (count[*iter-'A'] > 0) {
						len = 0;
						for (int i = 0; i < 26; i++) {
							count[i] = 0;
						}
					}
				}
			} else {
				count[result[len - 1]-'A']++;
			}
		}

		printf("Case #%d: [", t);
		for (int i = 0; i < len; i++) {
			if (i > 0) {
				printf(", ");
			}
			printf("%c", result[i]);
		}
		printf("]\n");
	}

	return 0;
}
