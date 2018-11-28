#include <iostream>
#include <string>
#include <vector>

using namespace std;

void Output(const char *str)
{
	static int x = 0;
	x++;
	printf("Case #%d: %s\n", x, str);
}

void Output(long long ans)
{
	static int x = 0;
	x++;
	printf("Case #%d: %I64d\n", x, ans);
}

void Output(int ans)
{
	static int x = 0;
	x++;
	printf("Case #%d: %d\n", x, ans);
}

int cnm(int n, int m)
{
	int ans = 1;
	int x = m;
	if( x > n-m ) x = n-m;
	for(int i = 1; i <= x; i++) {
		ans = ans*(n-i+1)/i;
		ans %= 100003;
	}
	return ans;
}

int func(int n, int m)
{
	if( n == m+1 || m == 1 ) return 1;
	
	int ans = 0;
	for(int i = 1; i <= m-1; i++) {
		if( n-m-1<m-i-1 ) continue;
		int tmp = ( func(m,i) * cnm(n-m-1,m-i-1) )%100003;
		ans += tmp;
		ans %= 100003;
	}
	return ans;
}

void solve()
{
	int n;
	scanf("%d", &n);

	int ans = 0;
	for(int i = 1; i <= n-1; i++) {
		ans += func(n,i);
		ans %= 100003;
	}
	
	Output(ans);
}

void GCJ2010_R1A_C()
{
	int T;
	scanf("%d", &T);
	while(T--) {
		solve();
	}
}

int main()
{
	GCJ2010_R1A_C();
	return 0;
}

