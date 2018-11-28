#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

const string msg = "welcome to code jam";

int n;
char buf[510];
int cache[30][510];

int calc(int p, int q) {
	int &res = cache[p][q];
	if (res != -1) return res;
	if (!p) return res = 1;
	if (!q) return res = 0;
	res = 0;
	if (msg[p - 1] == buf[q - 1]) res += calc(p - 1, q - 1);
	res += calc(p, q - 1);
	res %= 10000;
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++) {
		gets(buf);
		//printf("%s\n", buf);
		memset(cache, 255, sizeof(cache));
		printf("Case #%d: %04d\n", i + 1, calc(msg.size(), strlen(buf)));
	}
	return 0;
}
