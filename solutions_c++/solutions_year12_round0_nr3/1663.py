#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int nmap[2000001];

int A, B;
int digit;
int how_many_digit(int n)
{
	int ret = 0;
	do {
		ret++;
		n /= 10;
	}while (n);
	return ret;
}
int mypow(int n, int p)
{
	int ret = 1;
	while (p--) {
		ret *= n;
	}
	return ret;
}
int gao(int n)
{
	if (nmap[n]) {
		return 0;
	}

	int tmp = 1;
	int num[10];
	num[0] = n;
	nmap[n] = 1;
	for (int i=0; i<digit-1; i++) {
		int d = n%10;
		n /= 10;
		n += d*mypow(10, digit-1);
		if (n > B || n < A)
			continue;

		int j;
		for (j=0; j<tmp; j++) {
			if (num[j] == n) {
				break;
			}
		}
		if (j == tmp) {
			num[tmp++] = n;
			nmap[n] = 1;
		}
	}
	return tmp*(tmp-1) / 2;
}
int main()
{
	int T;
	cin >> T;
	int ans;
	for (int t=1; t<=T; t++) {
		cin >> A >> B;
		ans = 0;
		digit = how_many_digit(A);
		memset(nmap, 0, sizeof(nmap));
		for (int i=A; i<=B; i++) {
			ans += gao(i);
		}
		printf("Case #%d: %d\n", t, ans);
	}
	
	return 0;
}