#include <iostream>
using namespace std;

const char * pattern = "welcome to code jam";
int cnt = 0;

void matcher(int index, const char * s) {
	if (index == 19) {
		cnt ++;
		return ;
	}
	for (int i = 0; s[i]; ++i) {
		if (pattern[index] == s[i]) {
			matcher(index + 1, &s[i + 1]);
		}
	}
}

int main() {
	int n;
	char str[512];
	scanf("%d", &n);
	scanf(" ");
	for (int i = 0; i < n; ++i) {
		gets(str);
		cnt = 0;
		matcher(0, str);
		printf("Case #%d: %04d\n", i + 1, cnt);
	}
	return 0;
}

