#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
	int re, len;
	char buf[100];

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		buf[0] = '0';
		scanf("%s", buf + 1);
		len = strlen(buf);
		next_permutation(buf, buf + len);
		printf("Case #%d: ", ri);
		puts(buf + (buf[0] == '0'));
	}

	return 0;
}

