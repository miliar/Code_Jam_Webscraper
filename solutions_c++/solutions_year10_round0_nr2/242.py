#include<iostream>
using namespace std;

int gcd(int a, int b)
{
	return b ? gcd(b, a % b) : a;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int T, n;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas){
		scanf("%d", &n);
		const int N = 105;
		int t[N], minT = 0x7fffffff, g = 0;
		for(int i = 0; i < n; ++i){
			scanf("%d", &t[i]);
			minT = min(minT, t[i]);
		}
		for(int i = 0; i < n; ++i){
			g = gcd(g, t[i] - minT);
		}
		if(minT %= g) minT = g - minT;		
		printf("Case #%d: %d\n", cas, minT);
	}
	return 0;
}