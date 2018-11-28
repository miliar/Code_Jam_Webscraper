#include <cstdio>
#include <iostream>
#include <map>
#include <string>
using namespace std;

int T, C, D, N;

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.txt", "w", stdout);
	scanf("%d", &T);
	for(int s = 1; s <= T; ++s) {
		map<string, char> mp_1;
		map<string, char> mp_2;
		char chs[111], ch;

		scanf("%d", &C);

		for(int i = 0; i < C; ++i) {
			scanf("%s", &chs);
			ch = chs[2];
			chs[2] = '\0';
			mp_1[string(chs)] = ch;
		}
		scanf("%d", &D);
		for(int i = 0; i < D; ++i) {
			scanf("%s", &chs);
			mp_2[string(chs)] = ' ';
		}
		scanf("%d", &N);
		scanf("%s", &chs);
		
		string str = "";
		string tmp = "", tmp2 = "";
		for(int i = 0; i < N; ++i) {
			str += chs[i];
			if(str.length() < 2) continue;
			tmp = str.substr(str.length() - 2, 2);
			tmp2 = "";
			tmp2 += tmp[1];
			tmp2 += tmp[0];
			if(mp_1.find(tmp) == mp_1.end() && mp_1.find(tmp2) == mp_1.end()) {
				for(int i = 0; i < str.length(); ++i) {
					for(int j = i + 1; j < str.length(); ++j) {
						tmp = "";
						tmp += str[i];
						tmp += str[j];
						if(mp_2.find(tmp) != mp_2.end()) {
							str = "";
						} else {
							tmp = "";
							tmp += str[j];
							tmp += str[i];
							if(mp_2.find(tmp) != mp_2.end()) str = "";
						}
					}
				}
			} else {
				if(mp_1.find(tmp) != mp_1.end())
					str[str.length() - 2] = mp_1[tmp];
				else
					str[str.length() - 2] = mp_1[tmp2];
				str = str.substr(0, str.length() - 1);
			}
		}
		N = str.length();
		const char * pchs = str.c_str();
		printf("Case #%d: [", s);
		for(int i = 0; i < N; ++i) {
			putchar(pchs[i]);
			if(i < N - 1) {
				putchar(',');
				putchar(' ');
			}
		}
		puts("]");

	}
	return 0;
}