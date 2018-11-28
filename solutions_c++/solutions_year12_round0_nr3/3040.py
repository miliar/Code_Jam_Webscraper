#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

const int p[9] = {1, 10, 100, 1000, 10000, 10000, 100000, 100000, 1000000};
int a[20];

int get_len(int n)
{
	int len = 0;
	while (n > 0) {
		++len;
		n /= 10;
	}
	return len;
}

int calc(int n, int Lim) {
	int len = get_len(n);
	int tmp = 0;
	
	int X, Y, now, c = 0;
	bool bj;
	for (int i = 1; i <= len-1; i++) {
		X = n / p[i];
		Y = n % p[i];
		now = Y * p[len - i] + X;
		if (now>n && now<=Lim && get_len(now)==len) {
			bj = true;
			for (int k = 1; k <= c; k++)
				if (a[k] == now) {
					bj = false;
					break;
				}
			if (bj) {
				++tmp;
				a[++c] = now;
			}
		}
	}

	return tmp;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int TextN, TT = 0, A, B, Ans;
	scanf("%d", &TextN);
	while (TextN--) {
		scanf("%d%d", &A, &B);
		Ans = 0;
		for (int i = A; i <= B; i++) 
			Ans += calc(i, B);
		printf("Case #%d: %d\n", ++TT, Ans);
	}
}