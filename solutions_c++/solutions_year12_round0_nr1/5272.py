#include <cstdio>
#include <cstring>

using namespace std;

char* forr[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char* eng[3] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};

char corr[26];

char tmp[256];
char res[256];

int main() {

	memset(corr, 0, sizeof(corr));

	corr['q' - 'a'] = 'z';
	corr['z' - 'a'] = 'q';

	for (int i = 0; i < 3; i++) {

		int l = strlen(forr[i]);
		for (int j = 0; j < l; j++) {
			if (forr[i][j] >= 'a' && forr[i][j] <= 'z') {
				corr[forr[i][j] - 'a'] = eng[i][j];
			}
		}
	}

	for (int i = 0; i < 26; i++) {
		printf("%c -> %c\n", 'a' + i, corr[i]);
	}

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tt;
	scanf("%d ", &tt);
	for (int i = 1; i <= tt; i++) {
		fgets(tmp, 256, stdin);
		int l = strlen(tmp);
		for (int j = 0; j < l; j++) {
			if (tmp[j] >= 'a' && tmp[j] <= 'z') {
				res[j] = corr[tmp[j] - 'a'];
			}
			else {
				res[j] = tmp[j];
			}
		}
		res[l] = 0;
		printf("Case #%d: %s", i, res);
	}

	return 0;
}
