#include<iostream>
#include<algorithm>
using namespace std;

const int N = 900;
int x [N], y [N];

int main()
{
	freopen("A-large.in.txt", "r", stdin);
	freopen("Alarge.out", "w", stdout);
	int tc, cas = 0, n;
	scanf("%d", &tc);
	while(tc --){
		scanf("%d", &n);
		for(int i = 0; i < n; ++ i) scanf("%d", &x [i]);
		for(int i = 0; i < n; ++ i) scanf("%d", &y [i]);
		sort(x, x + n);
		sort(y, y + n);
		long long res = 0;
		for(int i = 0; i < n; ++ i)
			res += (long long)(x [i]) * y [n - 1 - i];
		printf("Case #%d: %lld\n", ++ cas, res);
	}
	return 0;
}

