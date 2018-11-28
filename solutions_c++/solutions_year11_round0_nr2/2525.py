#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int T, C, D, N;

char comb[300][300];
char buff[1000];
char out[1000];
vector< pair<char, char> > subs;
char contain[300];

int main()
{
	scanf(" %d", &T);
	for(int _42 = 1; _42 <= T; ++_42) {
		memset(comb, 0, sizeof(comb));
		memset(contain, 0, sizeof(contain));
		subs.clear();

		scanf(" %d", &C);
		for(int i = 0; i < C; ++i) {
			scanf(" %s", buff);
			comb[buff[0]][buff[1]] = buff[2];
			comb[buff[1]][buff[0]] = buff[2];
		}

		scanf(" %d", &D);
		for(int i = 0; i < D; ++i) {
			scanf(" %s", buff);
			/*if(buff[1] > buff[0]) {
				char swap = buff[0];
				buff[0] = buff[1];
				buff[1] = swap;
			}*/
			subs.push_back(make_pair(buff[0], buff[1]));
			subs.push_back(make_pair(buff[1], buff[0]));
		}

		scanf(" %d", &N);
		scanf(" %s", buff);


		int len = 1;
		out[0] = buff[0];
		for(int i = 1; i < N; ++i) {
			if(comb[out[len-1]][buff[i]]) {
				out[len-1] = comb[out[len-1]][buff[i]];
			} else {
				int d = 0;
				for(int j = 0; j < subs.size(); ++j) {
					if(subs[j].first == buff[i]) {
						for(int k = 0; k < len; ++k) {
							if(out[k] == subs[j].second) {
								d = 1;
								goto HELL;
							}
						}
					}
				}
HELL:			if(d) {
					len = 0;
				} else {
					out[len++] = buff[i];
				}
			}
		}
		out[len] = '\0';


		printf("Case #%d: [", _42);
		for(int i = 0; i < len; ++i) {
			printf("%s%c", i==0?"":", ", out[i]);
		}
		printf("]\n");
	}
	return 0;
}
