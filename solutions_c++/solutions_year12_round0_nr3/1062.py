#include <iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
bool vst[2002000];
int getDigit(int n)
{
	int ret = 1;
	while (n) 
		n/=10, ret*=10;
	return ret/10;
}
int process(int n, int a,int b)
{
	vst[n-a] = true;
	int t = getDigit(n);
	int tmp = n;
	int ret = 1;
	n = (n % 10) * t + n / 10;
	while (tmp != n) {
		if (n>=a && n <= b) {
			vst[n-a] = true;
			ret++;
		}
		n = (n % 10) * t + n / 10;
	}
	return ret;
}
int main(int argc, char *argv[]) {
	freopen("C-large.in.txt", "r", stdin);
	freopen("C1.out", "w", stdout);
	int cases, t = 1;
	scanf("%d", &cases);
	while (cases--) {
		int a, b;
		int ret = 0;
		memset(vst, false, sizeof(vst));
		scanf("%d %d", &a, &b);
		for (int i=a; i<=b; i++) {
			if (vst[i-a]) continue;
			int tmp = process(i, a, b);
			ret += ((tmp * (tmp - 1)) / 2);
		}
		printf("Case #%d: %d\n", t++, ret);
	}
	return 0;
}