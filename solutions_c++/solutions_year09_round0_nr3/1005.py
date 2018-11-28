#include <cstdio>
#include <string>

using namespace std;

const string pat = "welcome to code jam";

char w[1000];
int cnt[20];

int main () {
	int tt;
	scanf ("%d\n", &tt);
	for (int it = 1; it <= tt; it++) {
		gets (w);
		memset (cnt, 0, sizeof (cnt));
		cnt[0] = 1;
		for (int i = 0; w[i]; i++) {
			for (int j = 19; j >= 0; j--)
				if (j < 19 && pat[j] == w[i])
					cnt[j + 1] = (cnt[j + 1] + cnt[j]) % 10000;
		}
		printf ("Case #%d: %04d\n", it, cnt[19]);
	}
}