#include <iostream>
#include <cstring>
using namespace std;

long long ans;
int a, b, digit;
bool hsh[2000010];
int ten[7] = {1, 10, 100, 1000, 10000, 100000, 1000000};

void process (int x) {
	for (int i = 0; i < digit; i ++) {
		int num = (x % ten[digit - i]) * ten[i] + x / ten[digit - i];
		if (num >= a && num <= b && num > x && !hsh[num]) {
			hsh[num] = true;
		//	printf ("%d %d\n", x, num);
			++ ans;
		}
	}
	for (int i = 0; i < digit; i ++) {
		hsh[(x % ten[digit - i]) * ten[i] + x / ten[digit - i]] = false;
	}
}

int main () {
	int i, j, k, T, ca;
	freopen ("/home/shuo/Desktop/A.in", "r", stdin);
	freopen ("/home/shuo/Desktop/ot", "w", stdout);

	scanf ("%d", &T);
	memset (hsh, false, sizeof (hsh));
	for (ca = 1; ca <= T; ++ ca) {
		scanf ("%d%d", &a, &b);
		ans = 0;
		for (digit = 7; digit >= 1; --digit) if (a / ten[digit-1] != 0) break;
		for (i = a; i <= b; i++)
			process (i);
		printf ("Case #%d: %Ld\n", ca, ans);
	}
	return 0;
}
