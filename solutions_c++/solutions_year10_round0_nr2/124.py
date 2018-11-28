#include<cstdio>
#include<iostream>
#include"bigint.h"
using namespace std;

biguint a[1000];
char buf[100];

string work()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", buf);
		a[i] = buf;
	}
	sort(a, a + n);
	n=unique(a,a+n)-a;
	biguint d = a[1] - a[0], ans = 0;
	for (int i = 2; i < n; i++)
		d = gcd(d, a[i] - a[i-1]);
	for (int i = 0; i < n; i++) {
		biguint t = d - a[i] % d;
		if (t > ans && t != d)
			ans = t;
	}
	return ans;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
		cout << "Case #" << i << ": " << work() << endl;
}
