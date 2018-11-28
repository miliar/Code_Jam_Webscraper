#include <cstdio>

int a, b;

bool isR(int n, int m){
	int len = 1;
	int tmp = n;
	while (tmp /= 10){
		len *= 10;
	}
	tmp = n;
	int x = n;
	while (tmp) {
		tmp /= 10;
		x = (x%10)*len + x/10;
		if (x == m) {
			return true;
		}
	}
	return false;
}

int main(int argc, char const *argv[])
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, sum, x;
	scanf("%d", &t);
	x = 0;
	while (x++ < t) {
		sum = 0;
		scanf("%d %d\n", &a, &b);
		if(a!=b) {
			for (int tmp=a; tmp<b; ++tmp) {
				for (int j=tmp+1; j<=b; ++j) {
					if (isR(tmp, j)) {
						sum ++;
					}
				}
			}
		}
		printf("Case #%d: %d\n", x,sum);
	}
	return 0;
}