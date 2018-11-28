#include <cstdio>
#include <string>
using namespace std;

int main() {
	string tmp = "ynficwlbkuomxsevzpdrjgthaq";
	char map[1000];
	map[' '] = ' ';
	for (int i = 0; i < 26; ++i) {
		map[tmp[i]] = 'a'+i;
	}

	int t;
	scanf("%d\n", &t);
	for (int tt = 1; tt <= t; ++tt) {
		printf("Case #%d: ", tt);
		char line[142];
		gets(line);
		for (int i = 0; line[i]; ++i) {
			putchar(map[line[i]]);
		}
		putchar('\n');
	}
}
