#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int gcd(int a, int b, int *x, int *y)
{
	int r, aa = 1, bb = 1, ab = 0, ba = 0, ra, rb;
	while (b) {
		r = a % b, ra = aa - a / b * ba, rb = ab - a / b * bb;
		a = b, aa = ba, ab = bb;
		b = r, ba = ra, bb = rb;
	}
	*x = aa, *y = ab;
	return a;
}

int rev(int k, int M)
{
	int x, y;
	gcd(k, M, &x, &y);
	if (x < 0) x += M;
	return x;
}

bool p[1000000 + 100];

void initial()
{
	memset(p, true, sizeof(p));
	p[0] = p[1] = false;
	for (int i = 2; i * i <= 1000000; ++i) {
		if (p[i]) {
			for (int j = i + i; j <= 1000000; j += i) {
				p[j] = false;
			}
		}
	}
}

int arr[16];
int d, k;

int check(long long a, long long b, int p)
{
	long long now = arr[0];
	for (int i = 0; i < k - 1; ++i) {
		now *= a;
		now += b;
		now %= p;
		if (now != arr[i + 1]) {
			return -1;
		}
	}
	now *= a;
	now += b;
	now %= p;
	return (int)now;
}

int cal(int p)
{
	if (k == 1) return -2;
	if (arr[0] == arr[1]) return arr[0];
	if (k == 2) {
		int now = -1;
		for (int a = 0; a <= (min(10, p - 1)); ++a) {
			int b = (((long long)arr[1] - (long long)a * arr[0]) % p + p) % p;
			int next = check(a, b, p);
			if (next != -1) {
				if (now == -1) {
					now = next;
				}
				else if (now != next) {
					return -2;
				}
			}
		}
		return now;
	}
	else {
		int da = arr[1] - arr[0];
		if (da < 0) da += p;
		int dy = arr[2] - arr[1];
		if (dy < 0) dy += p;
		int a = ((long long)dy * rev(da, p)) % p;
		int b = (((long long)arr[1] - (long long)a * arr[0]) % p + p) % p;
		return check(a, b, p);
	}
}

int run()
{
	int up = 1;
	scanf("%d %d", &d, &k);
	for (int i = 0; i < d; ++i) {
		up *= 10;
	}
	int down = 0;
	for (int i = 0; i < k; ++i) {
		scanf("%d", arr + i);
		down = max(down, arr[i] + 1);
	}
	int ans = -1;
	for (int i = down; i <= up; ++i) {
		if (!p[i]) continue;
		int ret = cal(i);
		if (ret != -1) {
			if (ret == -2) {
				return -1;
			}
			if (ans == -1) {
				ans = ret;
			}
			else if (ans != ret) {
				return -1;
			}
		}
	}
	return ans;
}

int main()
{
	freopen("A2.in", "r", stdin);
	freopen("A2.txt", "w", stdout);
	initial();
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int ret = run();
		printf("Case #%d: ", i);
		if (ret == -1) {
			puts("I don't know.");
		}
		else {
			printf("%d\n", ret);
		}
	}
	return 0;
}