#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
const int maxn = 500 + 10;

int f[30];
char s[maxn];
void work(int &a, const int &b) {
	a = a + b;
	a %= 10000;
}
int main()
{
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int ca = 1; ca <= t; ++ca) {
		gets(s);
		memset(f, 0, sizeof(f));
		f[0] = 1;
		for (int i = 0; s[i]; ++i) {
            //for (int j = 1; j < 20; ++j) printf("%d ", f[j]); printf("\n");
			switch (s[i]) {
				case 'w': work(f[1], f[0]); break;
				case 'e': work(f[2], f[1]); work(f[7], f[6]); work(f[15], f[14]); break;
				case 'l': work(f[3], f[2]); break;
				case 'c': work(f[4], f[3]); work(f[12], f[11]); break;
				case 'o': work(f[5], f[4]); work(f[10], f[9]); work(f[13], f[12]); break;
				case 'm': work(f[6], f[5]); work(f[19], f[18]); break;
				case ' ': work(f[8], f[7]); work(f[11], f[10]); work(f[16], f[15]); break;
				case 't': work(f[9], f[8]); break;
				case 'd': work(f[14], f[13]); break;
				case 'j': work(f[17], f[16]); break;
				case 'a': work(f[18], f[17]); break;
			}
		}
		printf("Case #%d: %04d\n", ca, f[19]);
	}
	return 0;
}
