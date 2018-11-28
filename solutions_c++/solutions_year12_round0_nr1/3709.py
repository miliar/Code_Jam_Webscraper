#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

string encry[] = {
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv",
	"zq"
};
string decry[] = {
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up",
	"qz"
};

char f[26];

int main() {
	int test;
	char str[128];
	for (int i = 0; i < 4; i ++) {
		for (int j = 0; j < encry[i].size(); j ++) {
			if (encry[i][j] != ' ') f[encry[i][j] - 'a'] = decry[i][j];
		}
	}
	scanf("%d", &test);
	gets(str);
	for (int i = 0; i < test; i++) {
		gets(str);
		int len = strlen(str);
		for (int j = 0; j < len; j ++) {
			if (str[j] != ' ') str[j] = f[str[j] - 'a'];
		}
		printf("Case #%d: %s\n", i + 1, str);
	}
	return 0;
}
