#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 2000002;

int T, l;
int a, b, ans, top, _10;
char ins[20], tmp[20];
int h[N], sig[N];

void calc() {
	int x = a, p = 0;
	while (x)
		p++,	x /= 10;
	for (_10 = 1; p--;)
		_10 *= 10;
	_10 /= 10;
}

int main() {
	freopen("input.txt", "r", stdin);	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; ans = top = 0, i <= T; i++) {
        scanf("%d%d", &a, &b);
        calc();
        memset(h, 0, sizeof h);
        for (int j = a, now, MIN; MIN = 2000000000, j <= b; j++) {
			sprintf(ins, "%d", j);
			
			if (j == 12)
				j = 12;
				
			if (j == 21)
				j = 21;
			
			l = strlen(ins);
			tmp[0] = now = 0;
			strcat(tmp, ins);
			strcat(ins, tmp);
			for (int k = 0; k < l; k++)
				now = now * 10 + ins[k] - '0';
			MIN = now;
			for (int k = l; k < (l << 1); k++)
				if (now = (now - (ins[k] - '0') * _10) * 10 + ins[k] - '0', now < MIN)
					MIN = now;
			if (++h[MIN] == 1)
				sig[++top] = MIN;
		}
		for (int j = 1, y; y = sig[j], j <= top; j++)
			ans += ((h[y] * (h[y] - 1)) >> 1);
        printf("Case #%d: %d\n", i, ans);
    }
	fclose(stdin);	fclose(stdout);
	return 0;
}
