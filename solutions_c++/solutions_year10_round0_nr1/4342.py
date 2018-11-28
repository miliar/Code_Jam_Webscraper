#include <iostream>
#include <vector>

using namespace std;

int t;
unsigned int long iterations;

int run(register int no) {
	// OFF == 0
	// ON == 1
	// Power and states
	register int p[30] = { 0 };
	register int s[30] = { 0 };

	p[0] = 1;
	for (register unsigned long int i = 0; i < iterations; ++i) {
		for (int j = 0; j < no; ++j) {
			if (p[j]) {
				if (s[j])
					s[j] = 0;
				else
					s[j] = 1;
			} else
				break;

		}
		for (int i = 0; i < no; ++i) {
			if (p[i] && s[i]) {
				p[i + 1] = 1;
			} else
				p[i + 1] = 0;
		}
	}
	for (int var = 0; var < no; ++var) {
		if (p[var] && s[var])
			continue;
		else
			return 0;
	}
	return 1;
}
int main() {
	register int i = 0, flag = 0;
	int no;
	freopen("D:\i.in", "r", stdin);
	freopen("D:\o.in", "w", stdout);
	scanf("%d",&t);
	for (i = 0; i < t; ++i) {
		scanf("%d", &no);
		scanf("%u", &iterations);
		flag = run(no);
		if (flag)
			printf("Case #%d: ON\n", i + 1);
		else
			printf("Case #%d: OFF\n", i + 1);
	}
	fflush(stdout);
	return 0;
}
